from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.products_page import ProductsPage


def test_search_product(page):
    search_term = "Blue Top"

    home_page = HomePage(page)
    home_page.load()
    assert home_page.is_home_showing()
    home_page.click_products_button()

    products_page = ProductsPage(page)
    expect(products_page.all_products_heading()).to_be_visible()

    products_page.enter_search_term(search_term)
    products_page.click_search_button()
    expect(products_page.searched_products_heading()).to_be_visible()

    names = products_page.product_names()
    assert names, "search returned no products"
    assert all(search_term.lower() in name.lower() for name in names)