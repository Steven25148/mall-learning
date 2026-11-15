"""Authentication and authorization contracts."""

import pytest


pytestmark = pytest.mark.integration


def test_login_returns_usable_token(api, credentials):
    username, password = credentials
    response, body = api.request(
        "POST", "/admin/login", json={"username": username, "password": password}
    )
    assert response.status_code == 200
    assert body["code"] == 200
    assert body["data"]["token"]
    assert body["data"]["tokenHead"]


def test_wrong_password_is_rejected(api, credentials):
    username, _ = credentials
    response, body = api.request(
        "POST", "/admin/login", json={"username": username, "password": "invalid-password-for-test"}
    )
    assert response.status_code == 200
    # The current service raises ApiException for a bad password; the global
    # handler maps it to business code 500. This is a possible API design defect.
    assert body["code"] == 500
    assert body["message"] == "密码不正确"
    assert body.get("data") is None


@pytest.mark.parametrize(
    "token",
    [pytest.param(None, id="missing-token"), pytest.param("Bearer invalid-test-token", id="invalid-token")],
)
def test_protected_product_list_rejects_bad_token(api, token):
    _, body = api.request("GET", "/product/list", token=token, params={"pageNum": 1, "pageSize": 1})
    assert body["code"] == 401
    assert body.get("data") is None


def test_authenticated_identity_matches_login(api, credentials, auth_token):
    username, _ = credentials
    response, body = api.request("GET", "/admin/info", token=auth_token)
    assert response.status_code == 200
    assert body["code"] == 200
    assert body["data"]["username"] == username
