from uuid import uuid4

from pages.auth_page import AuthPage
from pages.home_page import HomePage


def test_is_new_user_signup_visible(page):
    homepage = HomePage(page)
    homepage.load()
    homepage.click_signup_login()

    auth_page = AuthPage(page)
    assert auth_page.is_new_user_signup_showing()


def test_signup_advances_to_account_information(page):
    auth_page = AuthPage(page)
    auth_page.load()
    auth_page.enter_name("Portfolio Test")
    auth_page.enter_email(f"portfolio-{uuid4().hex}@example.com")
    auth_page.click_signup()

    assert auth_page.is_account_information_showing()

def test_enter_account_information(page):
    