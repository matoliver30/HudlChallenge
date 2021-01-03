from data import global_data
from data import login_data
from page_objects.base_page import BasePage
from page_elements.generic_text_element import GenericTextElement
from locators import logged_in_page_locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions


class DisplayNameTextElement(GenericTextElement):
    # The locator for input box where the user's email string is entered
    locator = logged_in_page_locators.DISPLAY_NAME_CSS


class LoggedInPage(BasePage):
    # Declares a variable that will contain the user's display name
    display_name_text_element = DisplayNameTextElement()

    def is_logged_in(self):
        """Verifies if the user is logged in by checking the user menu element"""
        element = WebDriverWait(self.driver, global_data.DEFAULT_WAIT_TIMEOUT).until(
            conditions.visibility_of_element_located(logged_in_page_locators.USER_MENU_CSS),
            "The element didn't exist after 30 seconds.")
        return element.is_displayed()

    def is_display_name_matches(self):
        return self.display_name_text_element == login_data.DISPLAY_NAME
