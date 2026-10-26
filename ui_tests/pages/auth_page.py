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
        return self.page.get_by_role("heading", name="New User Signup!").is_visible()

    def is_account_information_showing(self):
        return self.page.get_by_role(
            "heading", name="Enter Account Information"
        ).is_visible()

    def enter_account_information(
        self,
        password,
        birthday,
        birthmonth,
        birthyear,
        firstname,
        lastname,
        country,
        mobilenumber,
        *,
        address,
        state,
        city,
        zipcode,
        company="",
        address2="",
    ):
        self.page.get_by_label("Mr.").check()
        self.page.locator("[data-qa='password']").fill(password)
        self.page.locator("#days").select_option(birthday)
        self.page.locator("#months").select_option(birthmonth)
        self.page.locator("#years").select_option(birthyear)
        self.page.get_by_label("Sign up for our newsletter!").check()
        self.page.get_by_label("Receive special offers from our partners!").check()
        self.page.locator("[data-qa='first_name']").fill(firstname)
        self.page.locator("[data-qa='last_name']").fill(lastname)
        self.page.locator("[data-qa='company']").fill(company)
        self.page.locator("[data-qa='address']").fill(address)
        self.page.locator("[data-qa='address2']").fill(address2)
        self.page.locator("#country").select_option(label=country)
        self.page.locator("[data-qa='state']").fill(state)
        self.page.locator("[data-qa='city']").fill(city)
        self.page.locator("[data-qa='zipcode']").fill(zipcode)
        self.page.locator("[data-qa='mobile_number']").fill(mobilenumber)

    def click_create_account(self):
        self.page.locator("[data-qa='create-account']").click()

    def is_account_created_showing(self):
        return self.page.locator("[data-qa='account-created']").is_visible()

    def click_continue_button(self):
        self.page.locator("[data-qa='continue-button']").click()

    def logged_in_as_label(self):
        return self.page.get_by_text("Logged in as")

    def click_delete_account_button(self):
        self.page.get_by_role("link", name="Delete Account").click()

    def is_account_deleted_showing(self):
        return self.page.locator("[data-qa='account-deleted']").is_visible()   