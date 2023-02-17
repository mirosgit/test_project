import time

from ..locators import LoginLocators
from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage,  WaitUntil
from ..test_data import TestData
from selenium.webdriver.common.keys import Keys


class LoginValidationTest(BasePage):

    def input_phone(self):

        WaitUntil.wait_input_phone_field(self)

        _input_number_field = self.browser.find_element(*LoginLocators.input_number_field_id)

        _input_number_field.send_keys(TestData.number_phone)

    def click_next(self):

        _next_button = self.browser.find_element(*LoginLocators.next_button_css)

        _next_button.click()

    def compare_text(self):

        WaitUntil.wait_compare_text(self)

        _compare_text = self.browser.find_element(*LoginLocators.compare_text_xpath).text

        assert _compare_text == TestData.expected_text, "COMPARE TEXT IS FAILED"



