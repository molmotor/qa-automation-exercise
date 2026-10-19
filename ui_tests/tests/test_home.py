from pages.home_page import HomePage

def test_is_home_visible(page):
    homepage = HomePage(page)
    homepage.load()
    assert homepage.is_home_showing()