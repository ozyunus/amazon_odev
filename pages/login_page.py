from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_ = (By.ID, 'ap_email')
    CONTINUE_BUTTON = (By.ID, 'continue')
    PASSWORD_ = (By.ID, 'ap_password')
    SIGNIN_BUTTON = (By.ID, 'signInSubmit')
    LOGIN_USER = (By.ID, 'nav-link-accountList-nav-line-1')

    def fill_email_text_box(self, email):
        self.send_text(email, *self.EMAIL_)

    def fill_password_text_box(self, password):
        self.send_text(password, *self.PASSWORD_)

    def click_signin_btn(self):
        self.click_element(*self.SIGNIN_BUTTON)

    def continue_step_btn(self):
        self.click_element(*self.CONTINUE_BUTTON)

    def login_user(self):
        return self.find_element(*self.LOGIN_USER).text
