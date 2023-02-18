import pytest
import time
from selenium import webdriver
from .pages.login_page import LoginValidationTest
from .test_data import TestData
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

NEOBANK_URL = "https://web.neobank.one/"


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(NEOBANK_URL)

    yield driver

    title = driver.title
    assert title == TestData.expected_title_text, f"Title text is not as expected. Actual: {title}"

    driver.quit()


def test_login(browser):

    page = LoginValidationTest(browser, NEOBANK_URL)
    page.enter_phone_number()
    time.sleep(2)
    page.click_next_button()
    page.assert_expected_text()
