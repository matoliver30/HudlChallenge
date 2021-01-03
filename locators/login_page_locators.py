from selenium.webdriver.common.by import By


"""A module for login page locators. All login page locators should come here"""
EMAIL_INPUT_ID = (By.ID, "email")
EMAIL_INPUT_CSS = (By.CSS_SELECTOR, "input#email")
PWD_INPUT_ID = (By.ID, "password")
PWD_INPUT_CSS = (By.CSS_SELECTOR, "input#password")
LOGIN_BUTTON_ID = (By.ID, "logIn")
LOGIN_BUTTON_CSS = (By.CSS_SELECTOR, "button#logIn")
ERROR_CONTAINER_TEXT_CSS = (By.CSS_SELECTOR, "div.login-error-container > p")
