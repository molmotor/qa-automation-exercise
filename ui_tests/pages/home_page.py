from config import BASE_URL


class HomePage:
    def __init__(self, page):
        self.page = page

    def load(self):
        self.page.goto(BASE_URL)

    def is_home_showing(self):
        return self.page.locator("#slider-carousel").is_visible()

    def click_signup_login(self):
        self.page.get_by_role('link', name='Signup / Login').click()
