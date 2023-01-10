from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):
    GO_TO_PAGE = (By.CLASS_NAME, 's-pagination-button')
    PAGE_COUNT = (By.CLASS_NAME, 's-pagination-selected')
    SEARCH_RETURN = (By.CLASS_NAME, 'a-text-bold')

    def search_return(self):
        return self.find_element(*self.SEARCH_RETURN).text

    def click_pagination_button(self, index):
        self.find_elements(index, *self.GO_TO_PAGE)

    def get_page_count(self):
        return self.find_element(*self.PAGE_COUNT).get_attribute('aria-label')
