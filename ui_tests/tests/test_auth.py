from pages.auth_page import AuthPage
from pages.home_page import HomePage


def test_is_new_user_signup_visible(page):
    homepage = HomePage(page)
    homepage.load()
    homepage.click_signup_login()

    auth_page = AuthPage(page)
    assert auth_page.is_new_user_signup_showing()
