import unittest
from sys import platform
from data import login_data
from data import global_data
# from page_objects import Pages
from page_objects.main_page import MainPage
from page_objects.login_page import LoginPage
from page_objects.logged_in_page import LoggedInPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def get_correct_driver_for_os():
    if global_data.BROWSER == "CHROME":
        opts = ChromeOptions()
        if global_data.HEADLESS:
            opts.add_argument("--headless")
            opts.add_argument("--window-size=1920,1080")
        opts.add_argument("--start-maximized")
        if platform == "win32":
            return webdriver.Chrome(global_data.WIN_CHROMEDRIVER_PATH, options=opts)
        elif platform == "linux":
            return webdriver.Chrome(global_data.UNIX_CHROMEDRIVER_PATH, options=opts)
        elif platform == "darwin":
            return webdriver.Chrome(global_data.MAC_CHROMEDRIVER_PATH, options=opts)
    elif global_data.BROWSER == "FIREFOX":
        opts = FirefoxOptions()
        if global_data.HEADLESS:
            opts.add_argument("-headless")
        if platform == "win32":
            driver = webdriver.Firefox(executable_path=global_data.WIN_GECKODRIVER_PATH, options=opts)
            driver.maximize_window()
            return driver
        elif platform == "linux":
            driver = webdriver.Firefox(executable_path=global_data.UNIX_GECKODRIVER_PATH, options=opts)
            driver.maximize_window()
            return driver
        elif platform == "darwin":
            driver = webdriver.Firefox(executable_path=global_data.MAC_GECKODRIVER_PATH, options=opts)
            driver.maximize_window()
            return driver
    elif global_data.BROWSER == "SAFARI":
        if (platform == "win32") | (platform == "linux"):
            return None
        elif platform == "darwin":
            driver = webdriver.Safari(executable_path=global_data.MAC_SAFARIDRIVER_PATH)
            driver.maximize_window()
            return driver
    else:
        return None


class TestHudlLogin(unittest.TestCase):

    def setUp(self):
        self.driver = get_correct_driver_for_os()

        # Check if the method above managed to setup a driver for the desired browser + os combination
        self.assertTrue(self.driver is not None, "The test didn't manage to setup the driver, please check if "
                                                 "your driver choice is supported on this OS.")
        self.driver.set_script_timeout(10)
        self.driver.get(global_data.BASE_URL)

    def tearDown(self):
        self.driver.close()

    def test_successful_login_clicking_button(self):
        """
        Tests the login functionality of www.hudl.com considering the user clicked on the Login button
        to perform the action.
        """

        main_page = MainPage(self.driver)
        self.assertTrue(
            main_page.is_title_matches(),
            "The title of the Hudl main page was different from the expected. Found: {}, Expected: {}"
            .format(self.driver.title, main_page.MAIN_PAGE_TITLE)
        )

        # Clicks on the Login button to be redirected to the login page
        main_page.click_login_button()

        login_page = LoginPage(self.driver)

        self.assertTrue(
            login_page.is_title_matches(),
            "The title of the Hudl login page was different from the expected. Found: {}, Expected: {}"
            .format(self.driver.title, login_page.LOGIN_PAGE_TITLE)
        )

        # Sets the text of the email input to the user's email
        login_page.email_text_element = login_data.VALID_EMAIL

        # Sets the text of the password input to the user's password
        login_page.pwd_text_element = login_data.VALID_PASSWORD

        login_page.click_login_button()

        logged_in_page = LoggedInPage(self.driver)

        # Verifies if the user menu is visible
        self.assertTrue(logged_in_page.is_logged_in(), "The user wasn't logged in after clicking the Login button.")

        # Verifies if the display name present on the user menu matches the expected
        self.assertTrue(
            logged_in_page.is_display_name_matches(),
            "The display name don't match the expected. Found: {}, Expected: {}"
            .format(logged_in_page.display_name_text_element, login_data.DISPLAY_NAME)
        )

        print("\nSuccessfully logged in as {}!".format(logged_in_page.display_name_text_element))

    def test_successful_login_pressing_enter(self):
        """
        Tests the login functionality of www.hudl.com considering the user pressed the enter key to perform the action.
        """

        main_page = MainPage(self.driver)
        self.assertTrue(
            main_page.is_title_matches(),
            "The title of the Hudl main page was different from the expected. Found: {}, Expected: {}"
            .format(self.driver.title, main_page.MAIN_PAGE_TITLE)
        )

        # Clicks on the Login button to be redirected to the login page
        main_page.click_login_button()

        login_page = LoginPage(self.driver)

        self.assertTrue(
            login_page.is_title_matches(),
            "The title of the Hudl login page was different from the expected. Found: {}, Expected: {}"
            .format(self.driver.title, login_page.LOGIN_PAGE_TITLE)
        )

        # Sets the text of the email input to the user's email
        login_page.email_text_element = login_data.VALID_EMAIL

        # Sets the text of the password input to the user's password
        login_page.pwd_text_element = login_data.VALID_PASSWORD

        login_page.press_enter()

        logged_in_page = LoggedInPage(self.driver)

        # Verifies if the user is logged in
        self.assertTrue(logged_in_page.is_logged_in(), "The user wasn't logged in after clicking the Login button.")

        # Verifies if the display name present on the user menu matches the expected
        self.assertTrue(
            logged_in_page.is_display_name_matches(),
            "The display name don't match the expected. Found: {}, Expected: {}"
            .format(logged_in_page.display_name_text_element, login_data.DISPLAY_NAME)
        )

        print("\nSuccessfully logged in as {}!".format(logged_in_page.display_name_text_element))

    def test_unsuccessful_login_empty_fields(self):
        """
        Tests the login functionality of www.hudl.com considering the user try to login with empty fields.
        """

        main_page = MainPage(self.driver)
        self.assertTrue(
            main_page.is_title_matches(),
            "The title of the Hudl main page was different from the expected. Found: {}, Expected: {}"
            .format(self.driver.title, main_page.MAIN_PAGE_TITLE)
        )

        # Clicks on the Login button to be redirected to the login page
        main_page.click_login_button()

        login_page = LoginPage(self.driver)

        self.assertTrue(login_page.is_title_matches(),
                        "The title of the Hudl login page was different from the expected. "
                        "Found: {}, Expected: {}"
                        .format(self.driver.title, login_page.LOGIN_PAGE_TITLE))

        login_page.clear_credential_fields()

        login_page.click_login_button()

        # Verifies if the error container is visible
        self.assertTrue(login_page.is_error_container_visible(), "No error message was shown when trying to login with "
                                                                 "empty credential fields.")
        # Verify if the visible error message matches the expected
        self.assertTrue(login_page.is_error_message_matches(), "The error message displayed to the user was different "
                                                               "from the expected.")

    def test_unsuccessful_login_invalid_email(self):
        """
        Tests the login functionality of www.hudl.com considering the user entered a invalid email address.
        """

        main_page = MainPage(self.driver)
        self.assertTrue(
            main_page.is_title_matches(),
            "The title of the Hudl main page was different from the expected. Found: {}, Expected: {}"
            .format(self.driver.title, main_page.MAIN_PAGE_TITLE)
        )

        # Clicks on the Login button to be redirected to the login page
        main_page.click_login_button()

        login_page = LoginPage(self.driver)

        self.assertTrue(
            login_page.is_title_matches(),
            "The title of the Hudl login page was different from the expected. Found: {}, Expected: {}"
            .format(self.driver.title, login_page.LOGIN_PAGE_TITLE)
        )

        # Sets the text of the email input to the user's email
        login_page.email_text_element = login_data.INVALID_EMAIL

        # Sets the text of the password input to the user's password
        login_page.pwd_text_element = login_data.VALID_PASSWORD

        login_page.click_login_button()

        # Verifies if the error container is visible
        self.assertTrue(login_page.is_error_container_visible(), "No error message was shown when trying to login with "
                                                                 "empty credential fields.")
        # Verify if the visible error message matches the expected
        self.assertTrue(login_page.is_error_message_matches(), "The error message displayed to the user was different "
                                                               "from the expected.")

    def test_unsuccessful_login_invalid_password(self):
        """
        Tests the login functionality of www.hudl.com considering the user pressed the enter key to perform the action.
        """

        main_page = MainPage(self.driver)
        self.assertTrue(
            main_page.is_title_matches(),
            "The title of the Hudl main page was different from the expected. Found: {}, Expected: {}"
            .format(self.driver.title, main_page.MAIN_PAGE_TITLE)
        )

        # Clicks on the Login button to be redirected to the login page
        main_page.click_login_button()

        login_page = LoginPage(self.driver)

        self.assertTrue(
            login_page.is_title_matches(),
            "The title of the Hudl login page was different from the expected. Found: {}, Expected: {}"
            .format(self.driver.title, login_page.LOGIN_PAGE_TITLE)
        )

        # Sets the text of the email input to the user's email
        login_page.email_text_element = login_data.VALID_EMAIL

        # Sets the text of the password input to the user's password
        login_page.pwd_text_element = login_data.INVALID_PASSWORD

        login_page.click_login_button()

        # Verifies if the error container is visible
        self.assertTrue(login_page.is_error_container_visible(), "No error message was shown when trying to login with "
                                                                 "empty credential fields.")
        # Verify if the visible error message matches the expected
        self.assertTrue(login_page.is_error_message_matches(), "The error message displayed to the user was different "
                                                               "from the expected.")


if __name__ == '__main__':
    unittest.main()
