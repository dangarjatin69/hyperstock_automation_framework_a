import pytest
import allure
import time
from selenium.common.exceptions import NoSuchElementException
from utilities.logger import Logger
from utilities.screenshot import Screenshot
from pages.snapchat_login_page import SnapchatLoginPage
from drivers.driver_setup import DriverSetup

logger = Logger.get_logger()

def setup_module(module):
    global driver
    driver = DriverSetup.get_driver()

def teardown_module(module):
    driver.quit()

@pytest.mark.parametrize("password", [("Jd@sanp01")])
@allure.feature("Snapchat Login Feature")
@allure.story("Valid Login Test")
def test_snapchat_login(password):
    logger.info("Starting Snapchat login test")
    snapchat_login_page = SnapchatLoginPage(driver)
    
    try:
        snapchat_login_page.click_login()
        snapchat_login_page.grant_permissions()
        snapchat_login_page.enter_password(password)
        snapchat_login_page.click_login_button()
        
        time.sleep(5)  # Wait for login process
        assert snapchat_login_page.is_logged_in(), "Login failed!"
        logger.info("Snapchat login test passed")
        
        # Take screenshot after successful login
        screenshot_path = Screenshot.capture(driver, "snapchat_login_success")
        allure.attach.file(screenshot_path, name="Snapchat Login Screenshot", attachment_type=allure.attachment_type.PNG)
        logger.info("Screenshot captured and attached to Allure report")
    
    except NoSuchElementException as e:
        logger.error(f"Test failed due to missing element: {e}")
        screenshot_path = Screenshot.capture(driver, "snapchat_login_failure")
        allure.attach.file(screenshot_path, name="Snapchat Login Failure Screenshot", attachment_type=allure.attachment_type.PNG)
        pytest.fail(f"Test failed due to missing element: {e}")
