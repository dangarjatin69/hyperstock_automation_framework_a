from appium import webdriver
from appium.options.common import AppiumOptions

class DriverSetup:
    @staticmethod
    def get_driver():
        caps = {
            "platformName": "Android",
            "deviceName": "R5CT91K1G6L",  # Replace with your actual device ID
            "appPackage": "com.snapchat.android",
            "appActivity": "com.snapchat.android.VampireFangsAlias",
            "automationName": "UiAutomator2",
        }

        options = AppiumOptions()
        options.load_capabilities(caps)
        url = 'http://localhost:4723'
        return webdriver.Remote(command_executor=url, options=options)
