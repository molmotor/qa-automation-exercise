from config import AUTH_URL

class AuthPage:
    def __init__(self, page):
        self.page = page

    def load(self):
        self.page.goto(AUTH_URL)

    def enter_name(self, name):
        page.getByRole('Name').fill('molmotor')

    def enter_email(self, email):
        page.getByRole('Email Address').fill('molmotor@gmail.com')

    def click_signup(self):
        