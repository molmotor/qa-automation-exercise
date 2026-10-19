

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://www.automationexercise.com/login")

    def enter_name(self, name):
        field = self.driver.find_element(By.ID, "signup-name")
        field.send_keys(name)

    def enter_email(self, email):
        field = self.driver.find_element(By.ID, "signup-email")
        field.send_keys(email)

    def click_signup_button(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "[data-qa="signup-button]")
        button.click()
        
    def is_enter_account_information_visible(self):
        return self.driver.current_url == "https://www.automationexercise.com/signup"