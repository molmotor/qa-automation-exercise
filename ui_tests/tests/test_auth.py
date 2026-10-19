from pages.home_page import HomePage

def test_is_new_user_signup_visible(page):
    homepage = HomePage(page)
    homepage.load()
    homepage.click_signup_login()
    assert homepage.is_new_user_signup_showing()