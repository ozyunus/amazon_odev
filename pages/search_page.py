from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):
    GO_TO_2_PAGE = (By.CLASS_NAME, 's-pagination-button')

    def click_2_page(self, index):
        self.find_elements(index, *self.GO_TO_2_PAGE)