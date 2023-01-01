import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class TestCheckAmazonOdev(unittest.TestCase):

    MAIN_PAGE = (By.CLASS_NAME, "main-header-logo")
    LOGIN_HOVER = (By.ID, 'nav-link-accountList-nav-line-1')
    LOGIN_BUTTON = (By.CLASS_NAME, 'nav-action-button')
    EMAIL_ = (By.ID, 'ap_email')
    CONTINUE_BUTTON = (By.ID, 'continue')
    PASSWORD_ = (By.ID, 'ap_password')
    SIGNIN_BUTTON = (By.ID, 'signInSubmit')
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    SEARCH_RETURN = (By.CLASS_NAME, 'a-text-bold')
    LOGIN_USER = (By.ID, 'nav-link-accountList-nav-line-1')
    GO_TO_2_PAGE = (By.CLASS_NAME, 's-pagination-button')
    GO_TO_3_PRODUCT = (By.CLASS_NAME, 'sg-col-12-of-16')
    ADD_TO_LIST_BUTTON = (By.ID, 'add-to-wishlist-button-submit')
    SHOPPING_LIST = (By.ID, 'nav-flyout-wl-items')
    SHOPPING_LIST_PRODUCT_DELETE = (By.ID, 'delete-button-IDKL1I9W6WQCZ')

    base_url = 'https://www.amazon.com/'
    mail = 'ozyunus@msn.com'
    password = 'Oz18346283'
    search_keyword = 'SAMSUNG'

    wait_time = 10

    def setUp(self):
        option = Options()
        option.add_argument('--disable-extensions')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(self.wait_time)
        self.wait = WebDriverWait(self.driver, self.wait_time)

    def test_check_lcw_odev(self):
        self.driver.get(self.base_url)

        element = self.driver.find_element(*self.LOGIN_HOVER)
        ActionChains(self.driver).move_to_element(element).perform()
        self.driver.find_element(*self.LOGIN_BUTTON).click()

        self.driver.find_element(*self.EMAIL_).send_keys(self.mail)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

        self.driver.find_element(*self.PASSWORD_).send_keys(self.password)
        self.driver.find_element(*self.SIGNIN_BUTTON).click()
        time.sleep(5)

        self.assertEqual('Hello, yunus', self.driver.find_element(*self.LOGIN_USER).text)

        self.driver.find_element(*self.SEARCH_FIELD).send_keys(self.search_keyword)
        self.driver.find_element(*self.SEARCH_BUTTON).click()

        self.assertEqual('SAMSUNG', self.driver.find_element(*self.SEARCH_RETURN).text)

        self.driver.find_elements(*self.GO_TO_2_PAGE)[0].click()

        self.driver.find_elements(*self.GO_TO_3_PRODUCT)[5].click()

        self.driver.find_element(*self.ADD_TO_LIST_BUTTON).click()

        element = self.driver.find_element(*self.LOGIN_HOVER)
        ActionChains(self.driver).move_to_element(element).perform()
        self.driver.find_element(*self.SHOPPING_LIST).click()

        self.driver.find_element(*self.SHOPPING_LIST_PRODUCT_DELETE).click()

    def tearDown(self):
        self.driver.close()
