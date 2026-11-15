"""Shared setup for read-only mall-admin integration tests."""

import os
from dataclasses import dataclass

import pytest
import requests


def pytest_addoption(parser):
    group = parser.getgroup("mall api")
    group.addoption(
        "--base-url",
        default=os.getenv("MALL_BASE_URL", "http://127.0.0.1:8080"),
        help="mall-admin address (or set MALL_BASE_URL)",
    )
    group.addoption(
        "--run-db",
        action="store_true",
        help="run the optional MySQL comparison test",
    )


@dataclass
class ApiClient:
    base_url: str
    session: requests.Session

    def request(self, method, path, *, token=None, **kwargs):
        headers = dict(kwargs.pop("headers", {}))
        if token is not None:
            headers["Authorization"] = token
        try:
            response = self.session.request(
                method,
                f"{self.base_url}{path}",
                headers=headers,
                timeout=(3, 10),
                **kwargs,
            )
        except requests.RequestException as exc:
            pytest.fail(
                f"Cannot reach mall-admin at {self.base_url}: {exc}. "
                "Start the service or pass --base-url.",
                pytrace=False,
            )
        try:
            payload = response.json()
        except ValueError:
            pytest.fail(
                f"{method} {path} returned HTTP {response.status_code} "
                "without a JSON response",
                pytrace=False,
            )
        assert isinstance(payload, dict), f"{method} {path}: expected JSON object"
        assert "code" in payload, f"{method} {path}: missing business code"
        return response, payload


@pytest.fixture(scope="session")
def api(pytestconfig):
    with requests.Session() as session:
        yield ApiClient(pytestconfig.getoption("--base-url").rstrip("/"), session)


@pytest.fixture(scope="session")
def credentials():
    username = os.getenv("MALL_TEST_USERNAME")
    password = os.getenv("MALL_TEST_PASSWORD")
    if not username or not password:
        raise pytest.UsageError(
            "Set MALL_TEST_USERNAME and MALL_TEST_PASSWORD for a test account."
        )
    return username, password


@pytest.fixture(scope="session")
def auth_token(api, credentials):
    username, password = credentials
    response, body = api.request(
        "POST", "/admin/login", json={"username": username, "password": password}
    )
    assert response.status_code == 200
    assert body["code"] == 200, f"Test account could not log in: {body.get('message')}"
    assert isinstance(body.get("data"), dict)
    token = body["data"].get("token")
    token_head = body["data"].get("tokenHead")
    assert isinstance(token, str) and token
    assert isinstance(token_head, str) and token_head
    return token_head + token


@pytest.fixture(scope="session")
def db_connection(pytestconfig):
    if not pytestconfig.getoption("--run-db"):
        pytest.skip("MySQL comparison is opt-in: pass --run-db")
    required = ["MALL_DB_HOST", "MALL_DB_USER", "MALL_DB_PASSWORD", "MALL_DB_NAME"]
    missing = [name for name in required if not os.getenv(name)]
    if missing:
        raise pytest.UsageError(f"Missing database settings: {', '.join(missing)}")
    import pymysql

    connection = pymysql.connect(
        host=os.environ["MALL_DB_HOST"],
        port=int(os.getenv("MALL_DB_PORT", "3306")),
        user=os.environ["MALL_DB_USER"],
        password=os.environ["MALL_DB_PASSWORD"],
        database=os.environ["MALL_DB_NAME"],
        connect_timeout=5,
        read_timeout=5,
        cursorclass=pymysql.cursors.DictCursor,
    )
    try:
        yield connection
    finally:
        connection.close()
