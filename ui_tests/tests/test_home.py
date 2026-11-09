from playwright.sync_api import expect

from pages.home_page import HomePage


def test_is_home_visible(page):
    homepage = HomePage(page)
    homepage.load()
    expect(homepage.home_slider()).to_be_visible()
