from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    MAIN_PAGE = (By.CLASS_NAME, "main-header-logo")
    LOGIN_HOVER = (By.ID, 'nav-link-accountList-nav-line-1')
    LOGIN_BUTTON = (By.CLASS_NAME, 'nav-action-button')
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    LOGO_TEXT = (By.ID, 'nav-logo-sprites')

    def get_logo_text_name(self):
        return self.find_element(*self.LOGO_TEXT).get_attribute('aria-label')

    def hover_login(self):
        self.hover_element(*self.LOGIN_HOVER)

    def click_login(self):
        self.click_element(*self.LOGIN_BUTTON)

    def click_search(self):
        self.click_element(*self.SEARCH_BUTTON)

    def fill_search_text_box(self, search):
        self.send_text(search, *self.SEARCH_FIELD)
