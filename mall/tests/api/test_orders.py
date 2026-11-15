"""Read-only checks for the order query's dynamic SQL conditions."""

import pytest


pytestmark = pytest.mark.integration


def order_page(api, auth_token, **params):
    response, body = api.request("GET", "/order/list", token=auth_token, params=params)
    assert response.status_code == 200
    assert body["code"] == 200, body.get("message")
    page = body["data"]
    assert isinstance(page["list"], list)
    return page


@pytest.fixture(scope="module")
def sample_order(api, auth_token):
    page = order_page(api, auth_token, pageNum=1, pageSize=1)
    if not page["list"]:
        pytest.skip("No order exists in this test environment")
    return page["list"][0]


@pytest.mark.parametrize("field", ["orderSn", "status", "sourceType", "orderType"])
def test_order_filter_matches_every_row(api, auth_token, sample_order, field):
    value = sample_order.get(field)
    if value is None or value == "":
        pytest.skip(f"Sample order has no {field}")
    page = order_page(api, auth_token, pageNum=1, pageSize=10, **{field: value})
    assert page["total"] >= 1
    assert all(item[field] == value for item in page["list"])
    assert all(item["deleteStatus"] == 0 for item in page["list"])


def test_order_detail_agrees_with_list(api, auth_token, sample_order):
    response, body = api.request("GET", f"/order/{sample_order['id']}", token=auth_token)
    assert response.status_code == 200
    assert body["code"] == 200
    detail = body["data"]
    assert detail["id"] == sample_order["id"]
    assert detail["orderSn"] == sample_order["orderSn"]
    assert isinstance(detail["orderItemList"], list)
