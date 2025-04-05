import os
from datetime import datetime

class Screenshot:
    @staticmethod
    def capture(driver, name):
        screenshot_dir = "reports/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"{screenshot_dir}/{name}_{timestamp}.png"
        driver.save_screenshot(screenshot_path)
        return screenshot_path
