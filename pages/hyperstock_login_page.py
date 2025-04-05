import subprocess
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class HyperStockLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.STARTUP_LOGIN_BUTTON = (By.ID, "com.hyperstock:id/btn_login")
        self.EMAIL_FIELD = (By.XPATH, '//android.widget.EditText[@resource-id="com.hyperstock:id/et_input_box"]')
        self.PASSWORD_FIELD = (By.XPATH, '//android.widget.EditText[@resource-id="com.hyperstock:id/et_input_box" and @text="Enter Password"]')
        self.LOGIN_BUTTON = (By.XPATH, '//android.widget.Button[@resource-id="com.hyperstock:id/btn_login"]')
        self.ALLOW_BUTTON = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")
        self.DASHBOARD_TEXT = (By.XPATH, '//*[@text="Dashboard"]')

    def launch_app(self):
        print("[ADB] Launching HyperStock app on user 0...")
        subprocess.run([
            "adb", "shell", "am", "start", "--user", "0",
            "-n", "com.hyperstock/com.hyperstock.main.entry_module.view.act.SplashAct"
        ])
    
    def click_startup_login_button(self):
        self.launch_app()
        print("Waiting for startup login button...")
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.STARTUP_LOGIN_BUTTON)
        ).click()
        print("Startup login button clicked.")

        # 🚨 NEW: Wait for email field to be visible after navigation
        print("Waiting for email field to appear...")
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.EMAIL_FIELD)
        )


    def enter_email(self, email):
        print("Entering email...")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.EMAIL_FIELD)
        ).send_keys(email)

    def enter_password(self, password):
        print("Entering password...")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PASSWORD_FIELD)
        ).send_keys(password)

    def click_login_button(self):
        print("Clicking login button...")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.LOGIN_BUTTON)
        ).click()

    def grant_permissions(self):
        print("Granting permissions if prompted...")
        try:
            allow_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.ALLOW_BUTTON)
            )
            allow_button.click()
            print("Permission granted.")
        except (TimeoutException, NoSuchElementException):
            print("No permission prompt found.")

    def is_logged_in(self):
        print("Checking if Dashboard is visible...")
        try:
            dashboard_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.DASHBOARD_TEXT)
            )
            print("Login successful.")
            return dashboard_text is not None
        except TimeoutException:
            print("Dashboard not found. Login failed.")
            return False
