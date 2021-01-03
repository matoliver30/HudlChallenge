from data import global_data
from page_objects.base_page import BasePage
from page_elements.generic_text_element import GenericTextElement
from locators import login_page_locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions


class EmailTextElement(GenericTextElement):
    # The locator for input box where the user's email string is entered
    locator = login_page_locators.EMAIL_INPUT_CSS


class PwdTextElement(GenericTextElement):
    # The locator for input box where the user's password string is entered
    locator = login_page_locators.PWD_INPUT_CSS


class ErrorMessageTextElement(GenericTextElement):
    # The locator for input box where the user's password string is entered
    locator = login_page_locators.ERROR_CONTAINER_TEXT_CSS


class LoginPage(BasePage):
    LOGIN_PAGE_TITLE = "Log In - Hudl"
    LOGIN_PAGE_INVALID_CREDENTIALS_ERROR = "We didn\'t recognize that email and/or password. Need help?"

    # Declares a variable that will contain the user's email
    email_text_element = EmailTextElement()

    # Declares a variable that will contain the user's password
    pwd_text_element = PwdTextElement()

    # Declares a variable that will contain the error message if any is present
    error_message_text_element = ErrorMessageTextElement()

    def is_title_matches(self):
        """Verifies if the title of the login page is the expected"""
        return WebDriverWait(self.driver, global_data.DEFAULT_WAIT_TIMEOUT).until(
            lambda x: self.LOGIN_PAGE_TITLE in self.driver.title)

    def click_login_button(self):
        """Triggers the login action"""
        element = WebDriverWait(self.driver, global_data.DEFAULT_WAIT_TIMEOUT).until(
            conditions.visibility_of_element_located(login_page_locators.LOGIN_BUTTON_CSS),
            "The element didn't exist after {} seconds.".format(global_data.DEFAULT_WAIT_TIMEOUT))
        if global_data.BROWSER == "SAFARI": 
            # Workaround due to an issue with Safari driver
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    def press_enter(self):
        """Press enter to trigger the login action"""
        element = WebDriverWait(self.driver, global_data.DEFAULT_WAIT_TIMEOUT).until(
            conditions.visibility_of_element_located(login_page_locators.PWD_INPUT_CSS),
            "The element didn't exist after {} seconds.".format(global_data.DEFAULT_WAIT_TIMEOUT))
        element.send_keys(Keys.ENTER)

    def is_error_container_visible(self):
        """Verifies if the error container is visible"""
        element = WebDriverWait(self.driver, global_data.DEFAULT_WAIT_TIMEOUT).until(
            conditions.visibility_of_element_located(login_page_locators.ERROR_CONTAINER_TEXT_CSS),
            "The element didn't exist after {} seconds.".format(global_data.DEFAULT_WAIT_TIMEOUT))
        return element.is_displayed()

    def is_error_message_matches(self):
        """Verifies if the error message is the expected"""
        return self.error_message_text_element == self.LOGIN_PAGE_INVALID_CREDENTIALS_ERROR

    def clear_credential_fields(self):
        """Clear the email and password fields"""
        self.email_text_element = ""
        self.pwd_text_element = ""
