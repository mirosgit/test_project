import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from ..locators import *
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)


class WaitUntil(BasePage):

    def wait_input_phone_field(self):
        _wait_input_phone_field = WebDriverWait(self.browser, 30)
        _input_phone_field = _wait_input_phone_field.until(EC.visibility_of_element_located(LoginLocators.input_number_field_id))

    def wait_compare_text(self):
        _wait_compare_text = WebDriverWait(self.browser, 30)
        _compare_text = _wait_compare_text.until(EC.visibility_of_element_located(LoginLocators.compare_text_xpath))

