# utilities/screenshot.py

import os
from datetime import datetime
import allure

def capture_screenshot(driver, name_prefix="screenshot"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name_prefix}_{timestamp}.png"
    screenshots_dir = "reports/screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)
    filepath = os.path.join(screenshots_dir, filename)
    
    driver.save_screenshot(filepath)

    # Attach to Allure report
    with open(filepath, "rb") as image_file:
        allure.attach(image_file.read(), name=filename, attachment_type=allure.attachment_type.PNG)

    return filepath
