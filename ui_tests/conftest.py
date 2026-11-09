from uuid import uuid4

import pytest
import requests

from config import API_URL


@pytest.fixture(autouse=True)
def block_ads(page):
    blocked = ("googlesyndication", "doubleclick", "googleads")
    page.route(
        "**/*",
        lambda r: r.abort()
        if any(d in r.request.url for d in blocked)
        else r.continue_(),
    )


@pytest.fixture
def registered_user():
    email = f"portfolio-{uuid4().hex}@example.com"
    password = "Test12345!"

    response = requests.post(
        API_URL + "/api/createAccount",
        data={
            "name": "Portfolio Test",
            "email": email,
            "password": password,
            "title": "Mr",
            "birth_date": "15",
            "birth_month": "5",
            "birth_year": "1995",
            "firstname": "Portfolio",
            "lastname": "Test",
            "company": "",
            "address1": "1 Test Street",
            "address2": "",
            "country": "Canada",
            "zipcode": "12345",
            "state": "Ontario",
            "city": "Toronto",
            "mobile_number": "0612345678",
        },
        timeout=10,
    )
    assert response.json()["responseCode"] == 201, "could not create test user"

    yield {"email": email, "password": password}

    requests.delete(
        API_URL + "/api/deleteAccount",
        data={"email": email, "password": password},
        timeout=10,
    )
