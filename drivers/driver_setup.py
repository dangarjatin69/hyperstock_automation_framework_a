from appium import webdriver
from appium.options.common import AppiumOptions

class DriverSetup:
    @staticmethod
    def get_driver():
        caps = {
            "platformName": "Android",
            "deviceName": "R5CT91K1G6L",
            "automationName": "UiAutomator2",
            "appPackage": "com.hyperstock",
            "appActivity": "com.hyperstock.main.entry_module.view.act.SplashAct",
            "appWaitActivity": "com.hyperstock.*",
            "appWaitDuration": 30000,
            "noReset": True,
            "newCommandTimeout": 300,
        }

        options = AppiumOptions()
        options.load_capabilities(caps)
        return webdriver.Remote("http://localhost:4723", options=options)
