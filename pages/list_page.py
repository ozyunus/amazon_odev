from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ListPage(BasePage):
    ADD_TO_LIST_BUTTON = (By.ID, 'add-to-wishlist-button-submit')
    SHOPPING_LIST = (By.ID, 'huc-list-link')
    LIST_PRODUCT_DETAILS = (By.CSS_SELECTOR, 'h2.a-size-base a[id]')
    SHOPPING_LIST_PRODUCT_DELETE = (By.NAME, 'submit.deleteItem')
    ITEM_UNDO = (By.ID, 'undo-delete')

    def add_to_list(self):
        self.click_element(*self.ADD_TO_LIST_BUTTON)

    def shopping_list(self):
        self.click_element(*self.SHOPPING_LIST)

    def get_list_product_details(self):
        return self.find_element(*self.LIST_PRODUCT_DETAILS).text

    def delete_list_product(self):
        self.click_element(*self.SHOPPING_LIST_PRODUCT_DELETE)

    def item_undo(self):
        return self.find_element(*self.ITEM_UNDO).text
