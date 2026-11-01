class ProductsPage:
    def __init__(self, page):
        self.page = page

    def all_products_heading(self):
        return self.page.get_by_role("heading", name="All Products")

    def enter_search_term(self, product_name):
        self.page.locator("#search_product").fill(product_name)

    def click_search_button(self):
        self.page.locator("#submit_search").click()

    def searched_products_heading(self):
        return self.page.get_by_role("heading", name="Searched Products")

    def product_names(self):
        return self.page.locator(".features_items .productinfo p").all_text_contents()