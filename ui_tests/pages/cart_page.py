class CartPage:
    def __init__(self, page):
        self.page = page

    def click_view_cart(self):
        self.page.get_by_role("link", name="View Cart").click()

    def is_cart_showing(self):
        return self.page.locator("#cart_info").is_visible()

    def product_rows(self):
        return self.page.locator("#cart_info_table tbody tr")

    def product_quantity(self, row=0):
        return self.product_rows().nth(row).locator(".cart_quantity button")

    def click_proceed_to_checkout(self):
        self.page.get_by_role("link", name="Proceed To Checkout").click()

    def click_register_login(self):
        self.page.get_by_role("link", name="Register / Login").click()
