import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest(unittest.TestCase):
    base_url = 'https://www.amazon.com/'
    wait_time = 10

    def setUp(self):
        option = Options()
        option.add_argument('--start-maximized')
        option.add_argument('--disable-extensions')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
        self.driver.implicitly_wait(self.wait_time)
        self.driver.get(self.base_url)
