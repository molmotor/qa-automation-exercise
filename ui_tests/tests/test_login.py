from uuid import uuid4

from pages.auth_page import AuthPage
from pages.home_page import HomePage

def test_login_user_correct_info(page):
    homepage=HomePage(page)
    homepage.load()
    assert homepage.is_home_showing()

    homepage.click_signup_login()