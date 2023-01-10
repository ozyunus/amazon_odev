import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from pages.home_page import HomePage
from pages.list_page import ListPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.search_page import SearchPage
from tests.base_test import BaseTest


class TestCheckAmazonOdev(BaseTest):
    mail = 'ozyunus@msn.com'
    password = 'Oz18346283'
    search_keyword = 'SAMSUNG'
    login_user_name = 'Hello, yunus'
    website_name = 'Amazon'
    page_name = 'Current page, page 2'
    page_index = 0
    product_index = 2

    def test_check_amazon_odev(self):
        home_page = HomePage(self.driver)
        self.assertEqual(self.website_name, home_page.get_logo_text_name(), 'Website name verified ')
        home_page.hover_login()
        home_page.click_login()

        login_page = LoginPage(self.driver)
        login_page.fill_email_text_box(self.mail)
        login_page.continue_step_btn()
        login_page.fill_password_text_box(self.password)
        login_page.click_signin_btn()
        self.assertEqual(self.login_user_name, login_page.login_user(), 'Signed in')

        home_page.fill_search_text_box(self.search_keyword)
        home_page.click_search()

        search_page = SearchPage(self.driver)
        self.assertIn(self.search_keyword, search_page.search_return(), 'Samsung searched')
        search_page.click_pagination_button(self.page_index)
        self.assertEqual(self.page_name, search_page.get_page_count(), 'On the expected page')

        product_page = ProductPage(self.driver)
        product_page.click_product(self.product_index)
        detail = product_page.get_product_detail()

        list_page = ListPage(self.driver)
        list_page.add_to_list()
        list_page.shopping_list()
        self.assertEqual(detail, list_page.get_list_product_details(), "The selected product is in the list")
        list_page.delete_list_product()
        self.assertTrue(list_page.item_undo(), 'List is empty')

    def tearDown(self):
        self.driver.close()
