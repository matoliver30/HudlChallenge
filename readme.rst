##########################
Hudl Challenge
##########################

The ``HudlChallenge`` project is intended to be a code challenge given by Hudl to tests their website
(https://www.hudl.com) login functionality.

==========================
Structure of the project
==========================

--------------------------
data
--------------------------

In this folder, you'll find all the constants that can be reused on different parts of the project.

--------------------------
drivers
--------------------------

This folder is where the browser's drivers should be located.

* The **win** folder is where the Windows drivers are located.
* The **mac** folder is where the MacOS drivers are located.
* The **unix** folder is where the Unix drivers are located.

The version of the drivers used in this project are:

* For Chrome, chromedriver version **87.0.4280.88**
* For Firefox, geckodriver version **0.28.0**
* For Safari, safaridriver version **13.1.3**

*If your browser version is not compatible with those drive versions please download the suitable driver on*
https://selenium-python.readthedocs.io/installation.html#drivers *and replace the executable on the respective folder.*

To change in which browser the tests will run you can change the constant **BROWSER** on **data/global_data.py**::

    # Those are the available options

    BROWSER = "CHROME"
    BROWSER = "FIREFOX"
    BROWSER = "SAFARI"

--------------------------
locators
--------------------------

Each file on this folder holds all the necessary locators of a specific page.

--------------------------
page_elements
--------------------------

In this folder, you'll find classes of elements with custom actions.

The *GenericTextElement* class for example creates a getter and setter for text elements, just so the code looks cleaner
and more understandable.

--------------------------
page_objects
--------------------------

Each file on this folder holds all the specific methods, hardcoded texts, etc that you might need for each page.

--------------------------
test_cases
--------------------------

In this folder you'll find all the test cases that are part of this test suite, each test case can contain multiple steps.

Test case(s) overview:

* test_hudl_login.py
    1. test_successful_login_clicking_button
        Tests if the login functionality succeeds as expected when the user performs the action by clicking on the **Login**
        button.
    2. test_successful_login_pressing_enter
        Tests if the login functionality succeeds as expected when the user performs the action by pressing the **Enter** key.
    3. test_unsuccessful_login_empty_fields
        Tests if the login functionality fails as expected when the user leaves both fields empty and performs the action.
    4. test_unsuccessful_login_invalid_email
        Tests if the login functionality fails as expected when the user performs the action using an invalid email.
    5. test_unsuccessful_login_invalid_password
        Tests if the login functionality fails as expected when the user performs the action using an invalid password for
        the correct email address.

==========================
Running the project
==========================

--------------------------
Preparation
--------------------------

As mentioned above if your browser version is not compatible with the driver version supplied, please download the
correct version for your browser and replace it in the respective folder.

If you're using a virtual environment you need to first activate it by running::

    # If you're on Windows
    ./your_venv_name/Scripts/activate

    # If you're on Mac or Unix
    source venv/bin/activate

Where **your_venv_name** is the name you gave to your virtual environment.

You can read more about how to create and use virtual environments at https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment

All the dependencies can be installed by running::

    pip install -r requirements.txt

    # OR

    pip3 install -r requirements.txt

If you're planning to run the test on Safari make sure you have enabled support for developers on your Safari browser. You can check how to do that at https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari

--------------------------
Running the test suite
--------------------------

Then you can run all the tests available by running one of the commands below on the root folder of the project::

    python -m unittest discover -v

    # OR

    python3 -m unittest discover -v

Or if you prefer to run a specific test case you can run::

    python -m unittest test_cases.test_hudl_login -v

    # OR

    python3 -m unittest test_cases.test_hudl_login -v


By default, the tests will run on **headless** mode on **Chrome** and **Firefox** as Safari doesn't support his feature.

If you want to run the tests on non-headless mode you can change the constant **HEADLESS** inside **data/global_data.py**::

    # Inside global_data.py
    HEADLESS = False

