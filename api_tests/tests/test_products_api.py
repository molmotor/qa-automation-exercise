import requests

from config import BASE_URL


def test_get_all_products():
    response = requests.get(BASE_URL + "/api/productsList")
    data = response.json()

    assert response.status_code == 200
    assert data["responseCode"] == 200
    assert data["products"], "products list is empty"
    assert data["products"][0]["name"], "first product has no name"


def test_post_to_products_list_is_not_supported():
    response = requests.post(BASE_URL + "/api/productsList")
    data = response.json()

    assert data["responseCode"] == 405
    assert "not supported" in data["message"].lower()


def test_search_product():
    search_term = "Blue Top"
    response = requests.post(
        BASE_URL + "/api/searchProduct",
        data={"search_product": search_term},
    )
    data = response.json()

    assert data["responseCode"] == 200
    assert data["products"], "search returned no products"
    assert all(search_term.lower() in p["name"].lower() for p in data["products"])


def test_search_product_without_parameter():
    response = requests.post(BASE_URL + "/api/searchProduct")
    data = response.json()

    assert data["responseCode"] == 400
    assert "missing" in data["message"].lower()


def test_verify_login_with_valid_credentials(api_user):
    response = requests.post(
        BASE_URL + "/api/verifyLogin",
        data={"email": api_user["email"], "password": api_user["password"]},
    )
    data = response.json()

    assert data["responseCode"] == 200
    assert "user exists" in data["message"].lower()


def test_verify_login_with_invalid_credentials():
    response = requests.post(
        BASE_URL + "/api/verifyLogin",
        data={"email": "nobody@example.com", "password": "wrongpassword"},
    )
    data = response.json()

    assert data["responseCode"] == 404
    assert "not found" in data["message"].lower()