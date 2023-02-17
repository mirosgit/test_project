import pytest
import time
from selenium import webdriver
from .pages.login_page import LoginValidationTest
from .pages.base_page import *
from .test_data import TestData
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

url = "https://web.neobank.one/"


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(url)

    yield driver

    title_name = driver.title

    assert title_name == TestData.expected_title_text, "COMPARE TITLE TEXT IS FAILED"

    driver.quit()


def test_login(browser):

    page = LoginValidationTest(browser, url)
    page.input_phone()
    time.sleep(2)
    page.click_next()
    page.compare_text()
