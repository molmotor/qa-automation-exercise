from uuid import uuid4

import pytest
import requests

from config import BASE_URL


@pytest.fixture
def api_user():
    email = f"api-{uuid4().hex}@example.com"
    password = "Test12345!"

    response = requests.post(
        BASE_URL + "/api/createAccount",
        data={
            "name": "API Test",
            "email": email,
            "password": password,
            "title": "Mr",
            "birth_date": "15",
            "birth_month": "5",
            "birth_year": "1995",
            "firstname": "API",
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
    )
    assert response.json()["responseCode"] == 201, "could not create test user"

    yield {"email": email, "password": password}

    requests.delete(
        BASE_URL + "/api/deleteAccount",
        data={"email": email, "password": password},
    )