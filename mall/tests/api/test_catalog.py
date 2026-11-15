"""Product query, pagination, and database consistency checks."""

import math

import pytest


pytestmark = pytest.mark.integration


def product_page(api, auth_token, **params):
    response, body = api.request("GET", "/product/list", token=auth_token, params=params)
    assert response.status_code == 200
    assert body["code"] == 200, body.get("message")
    page = body["data"]
    assert isinstance(page, dict)
    assert isinstance(page.get("list"), list)
    return page


@pytest.fixture(scope="module")
def sample_product(api, auth_token):
    page = product_page(api, auth_token, pageNum=1, pageSize=1)
    if not page["list"]:
        pytest.skip("No product exists in this test environment")
    return page["list"][0]


@pytest.mark.parametrize("page_size", [1, 3, 7])
def test_product_pagination_contract(api, auth_token, page_size):
    page = product_page(api, auth_token, pageNum=1, pageSize=page_size)
    assert page["pageNum"] == 1
    assert page["pageSize"] == page_size
    assert page["total"] >= 0
    assert page["totalPage"] == math.ceil(page["total"] / page_size)
    assert len(page["list"]) == min(page["total"], page_size)
    assert all(item["deleteStatus"] == 0 for item in page["list"])


def test_page_beyond_last_product_page_is_empty(api, auth_token):
    first = product_page(api, auth_token, pageNum=1, pageSize=2)
    beyond_last = max(1, first["totalPage"] + 1)
    page = product_page(api, auth_token, pageNum=beyond_last, pageSize=2)
    assert page["list"] == []
    assert page["total"] == first["total"]


@pytest.mark.parametrize(
    "field",
    ["productSn", "brandId", "productCategoryId", "publishStatus", "verifyStatus"],
)
def test_product_filter_returns_only_matches(api, auth_token, sample_product, field):
    value = sample_product.get(field)
    if value is None or value == "":
        pytest.skip(f"Sample product has no {field}")
    page = product_page(api, auth_token, pageNum=1, pageSize=10, **{field: value})
    assert page["total"] >= 1
    assert all(item[field] == value for item in page["list"])


def test_product_keyword_matches_name(api, auth_token, sample_product):
    keyword = sample_product["name"][:2]
    page = product_page(api, auth_token, pageNum=1, pageSize=10, keyword=keyword)
    assert page["total"] >= 1
    assert all(keyword in item["name"] for item in page["list"])


@pytest.mark.db
def test_product_api_matches_database(api, auth_token, sample_product, db_connection):
    product_id = sample_product["id"]
    with db_connection.cursor() as cursor:
        cursor.execute(
            "SELECT id, name, product_sn, delete_status FROM pms_product WHERE id = %s",
            (product_id,),
        )
        row = cursor.fetchone()
    assert row is not None
    assert row["delete_status"] == 0
    assert row["name"] == sample_product["name"]
    assert row["product_sn"] == sample_product["productSn"]
