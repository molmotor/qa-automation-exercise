from config import BASE_URL, PROD_URL


class HomePage:
    def __init__(self, page):
        self.page = page

    def load(self):
        self.page.goto(BASE_URL)

    def home_slider(self):
        return self.page.locator("#slider-carousel")

    def click_signup_login(self):
        self.page.get_by_role("link", name="Signup / Login").click()

    def click_products_button(self):
        self.page.goto(PROD_URL)

    def first_product(self):
        return self.page.locator(".features_items .product-image-wrapper").first

    def click_first_product_view(self):
        self.first_product().get_by_role("link", name="View Product").click()

    def add_products_to_cart(self):
        products = self.page.locator(".features_items .product-image-wrapper")
        products.nth(0).locator(".productinfo .add-to-cart").click()
        self.page.get_by_role("button", name="Continue Shopping").click()
        products.nth(1).locator(".productinfo .add-to-cart").click()
        self.page.get_by_role("button", name="Continue Shopping").click()

    def click_cart_button(self):
        self.page.locator("header a[href='/view_cart']").click()