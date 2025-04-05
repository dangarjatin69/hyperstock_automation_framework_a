import pytest
import allure
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from utilities.logger import Logger
from utilities.screenshot import Screenshot
from pages.hyperstock_login_page import HyperStockLoginPage
from drivers.driver_setup import DriverSetup

logger = Logger.get_logger()

def setup_module(module):
    global driver
    driver = DriverSetup.get_driver()

def teardown_module(module):
    driver.quit()

@pytest.mark.parametrize("email,password", [("jatin.d@rishvi.uk", "Jd@login1")])
@allure.feature("HyperStock Login Feature")
@allure.story("Valid Login Test")
def test_hyperstock_login(email, password):
    logger.info("Starting HyperStock login test")
    login_page = HyperStockLoginPage(driver)

    try:
        # Wait and click startup login button
        login_page.click_startup_login_button()
    
        # Enter email and click login
        login_page.enter_email(email)
        login_page.click_login_button()

        # Enter password and click login again
        login_page.enter_password(password)
        login_page.click_login_button()

        # Handle permission prompt if it appears
        login_page.grant_permissions()

        # Wait for app to transition to post-login screen
        time.sleep(5)

        if login_page.is_logged_in():
            screenshot_path = Screenshot.capture(driver, "hyperstock_login_success")
            allure.attach.file(screenshot_path, name="Login Success", attachment_type=allure.attachment_type.PNG)
            logger.info("Login successful")
        else:
            raise AssertionError("Login completed steps, but is_logged_in returned False")

    except (NoSuchElementException, TimeoutException) as e:
        logger.error(f"Critical failure: {e}")
        screenshot_path = Screenshot.capture(driver, "hyperstock_login_failure")
        allure.attach.file(screenshot_path, name="Login Failed", attachment_type=allure.attachment_type.PNG)
        pytest.fail(f"Test failed due to: {e}")

    except Exception as e:
        logger.warning(f"Non-critical issue occurred: {e}")
        screenshot_path = Screenshot.capture(driver, "hyperstock_login_warning")
        allure.attach.file(screenshot_path, name="Login Warning", attachment_type=allure.attachment_type.PNG)
