from uuid import uuid4

import pytest

from pages.auth_page import AuthPage
from utils.data_generator import generate_user


@pytest.fixture
def registered_user(page):
    user = generate_user()
    email = f"portfolio-{uuid4().hex}@example.com"

    auth_page = AuthPage(page)
    auth_page.load()
    auth_page.enter_name("Portfolio Test")
    auth_page.enter_signup_email(email)
    auth_page.click_signup()
    auth_page.enter_account_information(**user)
    auth_page.click_create_account()
    auth_page.click_continue_button()
    auth_page.click_logout()

    return {"email": email, "password": user["password"]}