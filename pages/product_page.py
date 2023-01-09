from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_DETAIL = (By.CSS_SELECTOR, 'span.product-title-word-break')
    PRODUCT_LIST = (By.CSS_SELECTOR, 'span.a-size-medium')

    def get_product_detail(self):
        return self.find_element(*self.PRODUCT_DETAIL).text

    def click_product(self, index):
        self.find_elements(index, *self.PRODUCT_LIST)
