from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ListPage(BasePage):
    PRODUCT_DETAILS = (By.ID, 'productTitle')
    ADD_TO_LIST_BUTTON = (By.ID, 'add-to-wishlist-button-submit')
    SHOPPING_LIST = (By.ID, 'huc-list-link')
    LIST_PRODUCT_DETAILS = (By.CSS_SELECTOR, "h2.a-size-base a[id]")
    SHOPPING_LIST_PRODUCT_DELETE = (By.CSS_SELECTOR, "[name='submit.deleteItem']")

    def get_product_detail(self):
        return self.find_element(*self.PRODUCT_DETAILS).text

    def add_to_list(self):
        self.click_element(*self.ADD_TO_LIST_BUTTON)

    def shopping_list(self):
        self.click_element(*self.SHOPPING_LIST)

    def get_list_product_details(self):
        return self.find_element(*self.LIST_PRODUCT_DETAILS).text

    def delete_list_product(self):
        self.click_element(*self.SHOPPING_LIST_PRODUCT_DELETE)
