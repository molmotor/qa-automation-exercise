from uuid import uuid4

from playwright.sync_api import expect

from pages.auth_page import AuthPage
from pages.home_page import HomePage
from utils.data_generator import generate_user


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
    auth_page.enter_signup_email(f"portfolio-{uuid4().hex}@example.com")
    auth_page.click_signup()

    assert auth_page.is_account_information_showing()


def test_register_user(page):
    user = generate_user()

    auth_page = AuthPage(page)
    auth_page.load()
    auth_page.enter_name("Portfolio Test")
    auth_page.enter_signup_email(f"portfolio-{uuid4().hex}@example.com")
    auth_page.click_signup()
    assert auth_page.is_account_information_showing()

    auth_page.enter_account_information(**user)
    auth_page.click_create_account()
    assert auth_page.is_account_created_showing()

    auth_page.click_continue_button()
    expect(auth_page.logged_in_as_label()).to_be_visible()

    auth_page.click_delete_account_button()
    expect(auth_page.account_deleted_message()).to_be_visible()


def test_login_user(page, registered_user):
    auth_page = AuthPage(page)
    auth_page.load()
    auth_page.enter_login_email(registered_user["email"])
    auth_page.enter_login_password(registered_user["password"])
    auth_page.click_login_button()

    expect(auth_page.logged_in_as_label()).to_be_visible()