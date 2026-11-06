class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def address_details(self):
        return self.page.get_by_role("heading", name="Address Details")

    def review_order(self):
        return self.page.get_by_role("heading", name="Review Your Order")

    def order_rows(self):
        return self.page.locator("#cart_info tbody tr")

    def enter_comment(self, comment):
        self.page.locator("textarea[name='message']").fill(comment)

    def click_place_order(self):
        self.page.get_by_role("link", name="Place Order").click()

    def enter_payment_details(self, name, card_number, cvc, month, year):
        self.page.locator("[data-qa='name-on-card']").fill(name)
        self.page.locator("[data-qa='card-number']").fill(card_number)
        self.page.locator("[data-qa='cvc']").fill(cvc)
        self.page.locator("[data-qa='expiry-month']").fill(month)
        self.page.locator("[data-qa='expiry-year']").fill(year)

    def click_pay_and_confirm_order(self):
        self.page.locator("[data-qa='pay-button']").click()

    def order_placed_message(self):
        return self.page.locator("[data-qa='order-placed']")

    def download_invoice(self):
        return self.page.get_by_role("link", name="Download Invoice")

    def click_continue(self):
        self.page.get_by_role("link", name="Continue").click()
