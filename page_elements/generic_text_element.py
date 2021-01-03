from data import global_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions


class GenericTextElement(object):
    """Generic page class that is initialized on every Text element on the page"""

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        element = WebDriverWait(driver, global_data.DEFAULT_WAIT_TIMEOUT).until(
            conditions.visibility_of_element_located(self.locator),
            "The element didn't exist after {} seconds.".format(global_data.DEFAULT_WAIT_TIMEOUT))
        element.clear()
        element.send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        element = WebDriverWait(driver, global_data.DEFAULT_WAIT_TIMEOUT).until(
            conditions.presence_of_element_located(self.locator),
            "The element didn't exist after {} seconds.".format(global_data.DEFAULT_WAIT_TIMEOUT))
        return element.text
