from data import global_data
from page_objects.base_page import BasePage
from locators import main_page_locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions
import time


class MainPage(BasePage):
    MAIN_PAGE_TITLE = "Performance analysis tools for sports teams and athletes at every level."
    # On some browsers on Mac OS the home page was different
    MAIN_PAGE_TITLE_VARIANT = "Hudl: We Help Teams and Athletes Win"

    def is_title_matches(self):
        """Verifies if the title of the main page is the expected"""
        return WebDriverWait(self.driver, global_data.DEFAULT_WAIT_TIMEOUT).until(
            lambda x: (self.MAIN_PAGE_TITLE in self.driver.title) | (self.MAIN_PAGE_TITLE_VARIANT in self.driver.title))

    def click_login_button(self):
        """Triggers the redirection to the login page"""
        element = WebDriverWait(self.driver, global_data.DEFAULT_WAIT_TIMEOUT).until(
            conditions.visibility_of_element_located(main_page_locators.LOGIN_BUTTON_CSS),
            "The element didn't exist after {} seconds.".format(global_data.DEFAULT_WAIT_TIMEOUT))            
        element.click()
