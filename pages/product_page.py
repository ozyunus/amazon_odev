from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    GO_TO_3_PRODUCT = (By.CSS_SELECTOR, 'span.a-size-medium')

    def click_3_product(self, index):
        self.find_elements(index, *self.GO_TO_3_PRODUCT)
