import time

from ..locators import LoginLocators
from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage, WaitUntil
from ..test_data import TestData
from selenium.webdriver.common.keys import Keys


class LoginValidationTest(BasePage):

    def enter_phone_number(self):
        """Enter phone number in the input field."""
        WaitUntil.wait_input_phone_field(self)

        phone_field = self.browser.find_element(*LoginLocators.input_number_field_id)

        phone_field.send_keys(TestData.number_phone)

    def click_next_button(self):
        """Click the next button."""
        next_button = self.browser.find_element(*LoginLocators.next_button_css)

        next_button.click()

    def assert_expected_text(self):
        """Assert that the expected text is displayed."""
        WaitUntil.wait_compare_text(self)

        text_element = self.browser.find_element(*LoginLocators.compare_text_xpath)
        actual_text = text_element.text

        assert actual_text == TestData.expected_text, "COMPARE TEXT IS FAILED"
