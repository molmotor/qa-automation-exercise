from config import AUTH_URL


class AuthPage:
    def __init__(self, page):
        self.page = page

    def load(self):
        self.page.goto(AUTH_URL)

    def enter_name(self, name):
        self.page.locator("[data-qa='signup-name']").fill(name)

    def enter_email(self, email):
        self.page.locator("[data-qa='signup-email']").fill(email)

    def click_signup(self):
        self.page.locator("[data-qa='signup-button']").click()

    def is_new_user_signup_showing(self):
        return self.page.get_by_role("heading", name="New user signup!").is_visible()
