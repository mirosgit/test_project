from selenium.webdriver.common.by import By


class LoginLocators:

    input_number_field_id = (By.ID, "login")
    next_button_css = (By.CSS_SELECTOR, "button[type]")
    compare_text_xpath = (By.XPATH, "/html/body/app-root/auth-page/div[2]/bpm-auth-qr/form/div[1]")