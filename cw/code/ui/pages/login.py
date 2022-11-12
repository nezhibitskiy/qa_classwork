from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class LoginPage(BasePage):

    locators = basic_locators.LoginPageLocators()

    def login(self, login, password):
        self.click((self.locators.LOGIN_BUTTON), 10)
        login_input = self.find(self.locators.LOGIN_INPUT, 10)
        self.send_keys(login_input,login)
        password_input = self.find(self.locators.PASSWORD_INPUT, 10)
        self.send_keys(password_input, password)
        self.click((self.locators.PASS_LOGIN_CREDS_BUTTON), 10)