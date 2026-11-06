from uuid import uuid4

from playwright.sync_api import expect

from pages.auth_page import AuthPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from utils.data_generator import generate_user


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


def test_product_quantity_in_cart(page):
    home_page = HomePage(page)
    home_page.load()
    assert home_page.is_home_showing()
    home_page.click_first_product_view()

    products_page = ProductsPage(page)
    assert products_page.is_product_detail_showing()
    products_page.set_quantity(4)
    products_page.click_add_to_cart()

    cart_page = CartPage(page)
    cart_page.click_view_cart()
    assert cart_page.is_cart_showing()
    expect(cart_page.product_quantity()).to_have_text("4")


def test_register_checkout_download_invoice_and_delete_account(page, tmp_path):
    home_page = HomePage(page)
    home_page.load()
    assert home_page.is_home_showing()
    home_page.add_products_to_cart()

    cart_page = CartPage(page)
    cart_page.click_cart_button()
    assert cart_page.is_cart_showing()
    cart_page.click_proceed_to_checkout()
    cart_page.click_register_login()

    user = generate_user()
    auth_page = AuthPage(page)
    auth_page.enter_name("Portfolio Test")
    auth_page.enter_signup_email(f"portfolio-{uuid4().hex}@example.com")
    auth_page.click_signup()
    assert auth_page.is_account_information_showing()
    auth_page.enter_account_information(**user)
    auth_page.click_create_account()
    expect(auth_page.account_created_message()).to_contain_text("ACCOUNT CREATED!")
    auth_page.click_continue_button()
    expect(auth_page.logged_in_as_label()).to_contain_text("Portfolio Test")

    home_page.click_cart_button()
    cart_page.click_proceed_to_checkout()

    checkout_page = CheckoutPage(page)
    expect(checkout_page.address_details()).to_be_visible()
    expect(checkout_page.review_order()).to_be_visible()
    expect(checkout_page.order_rows()).to_have_count(2)
    checkout_page.enter_comment("Please deliver the order carefully.")
    checkout_page.click_place_order()

    checkout_page.enter_payment_details(
        name="Portfolio Test",
        card_number="4111111111111111",
        cvc="123",
        month="12",
        year="2030",
    )
    checkout_page.click_pay_and_confirm_order()
    expect(checkout_page.order_placed_message()).to_contain_text(
        "Your order has been placed successfully!"
    )

    with page.expect_download() as download_info:
        checkout_page.download_invoice().click()
    invoice = download_info.value
    invoice_path = tmp_path / invoice.suggested_filename
    invoice.save_as(invoice_path)
    assert invoice_path.is_file()
    assert invoice_path.stat().st_size > 0

    checkout_page.click_continue()
    auth_page.click_delete_account_button()
    expect(auth_page.account_deleted_message()).to_contain_text("ACCOUNT DELETED!")
    auth_page.click_continue_button()