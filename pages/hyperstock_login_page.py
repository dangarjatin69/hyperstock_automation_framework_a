from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SnapchatLoginPage(BasePage):
    LOGIN_BUTTON = (By.XPATH, '//android.widget.TextView[@resource-id="com.snapchat.android:id/login_text"]')
    PASSWORD_FIELD = (By.XPATH, '//android.widget.EditText[@resource-id="com.snapchat.android:id/password_field"]')
    LOGIN_CONFIRM_BUTTON = (By.XPATH, '//android.widget.FrameLayout[@resource-id="com.snapchat.android:id/nav_button"]/android.widget.LinearLayout')
    ALLOW_BUTTON = (By.XPATH, '//*[@text="Allow"]')

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def grant_permissions(self):
        try:
            allow_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.ALLOW_BUTTON)
            )
            allow_button.click()
        except NoSuchElementException:
            pass

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.click(self.LOGIN_CONFIRM_BUTTON)

    def is_logged_in(self):
        return True  # Replace with actual check
