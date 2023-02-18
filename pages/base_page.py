import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ..locators import *


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)


class WaitUntil(BasePage):

    def wait_input_phone_field(self, timeout=30):
        wait = WebDriverWait(self.browser, timeout)
        input_phone_field = wait.until(EC.visibility_of_element_located(LoginLocators.input_number_field_id),
                                       f"Could not find input phone field within {timeout} seconds")
        return input_phone_field

    def wait_compare_text(self, timeout=30):
        wait = WebDriverWait(self.browser, timeout)
        compare_text = wait.until(EC.visibility_of_element_located(LoginLocators.compare_text_xpath),
                                  f"Could not find compare text within {timeout} seconds")
        return compare_text
