import pytest
import allure
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from utilities.logger import Logger
from utilities.screenshot import capture_screenshot
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

    with allure.step("Clicking startup login button"):
        try:
            # Wait and click startup login button
            login_page.click_startup_login_button()

        except Exception as e:
            logger.error(f"Failed to click startup login button: {e}")
            screenshot_path = capture_screenshot(driver, "startup_login_button_failure")
            allure.attach.file(screenshot_path, name="Startup Login Button Failure", attachment_type=allure.attachment_type.PNG)
            pytest.fail(f"Failed to click startup login button: {e}")

    with allure.step("Entering email and clicking login"):
        try:
            # Enter email and click login
            login_page.enter_email(email)
            login_page.click_login_button()

        except Exception as e:
            logger.error(f"Failed to enter email or click login: {e}")
            screenshot_path = capture_screenshot(driver, "email_login_failure")
            allure.attach.file(screenshot_path, name="Email Login Failure", attachment_type=allure.attachment_type.PNG)
            pytest.fail(f"Failed to enter email or click login: {e}")

    with allure.step("Entering password and clicking login again"):
        try:
            # Enter password and click login again
            login_page.enter_password(password)
            login_page.click_login_button()

        except Exception as e:
            logger.error(f"Failed to enter password or click login: {e}")
            screenshot_path = capture_screenshot(driver, "password_login_failure")
            allure.attach.file(screenshot_path, name="Password Login Failure", attachment_type=allure.attachment_type.PNG)
            pytest.fail(f"Failed to enter password or click login: {e}")

    with allure.step("Granting permissions"):
        try:
            # Handle permission prompt if it appears
            login_page.grant_permissions()

        except Exception as e:
            logger.warning(f"Failed to grant permissions: {e}")
            screenshot_path = capture_screenshot(driver, "permission_grant_warning")
            allure.attach.file(screenshot_path, name="Permission Grant Warning", attachment_type=allure.attachment_type.PNG)

    with allure.step("Waiting for post-login screen"):
        try:
            # Wait for app to transition to post-login screen
            time.sleep(5)

        except Exception as e:
            logger.error(f"Failed to wait for post-login screen: {e}")
            screenshot_path = capture_screenshot(driver, "post_login_wait_failure")
            allure.attach.file(screenshot_path, name="Post Login Wait Failure", attachment_type=allure.attachment_type.PNG)
            pytest.fail(f"Failed to wait for post-login screen: {e}")

    with allure.step("Verifying login success"):
        try:
            if login_page.is_logged_in():
                screenshot_path = capture_screenshot(driver, "hyperstock_login_success")
                allure.attach.file(screenshot_path, name="Login Success", attachment_type=allure.attachment_type.PNG)
                logger.info("Login successful")
            else:
                raise AssertionError("Login completed steps, but is_logged_in returned False")
                
        except AssertionError as e:
            logger.error(f"Login failed: {e}")
            screenshot_path = capture_screenshot(driver, "hyperstock_login_failure")
            allure.attach.file(screenshot_path, name="Login Failure", attachment_type=allure.attachment_type.PNG)
            pytest.fail(f"Test failed due to: {e}")
        except Exception as e:
            logger.warning(f"Non-critical issue occurred: {e}")
            screenshot_path = capture_screenshot(driver, "hyperstock_login_warning")
            allure.attach.file(screenshot_path, name="Login Warning", attachment_type=allure.attachment_type.PNG)
