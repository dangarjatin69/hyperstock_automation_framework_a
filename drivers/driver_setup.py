from appium import webdriver
from appium.options.common import AppiumOptions

class DriverSetup:
    @staticmethod
    def get_driver():
        caps = {
            "platformName": "Android",
            "deviceName": "R5CT91K1G6L",  # Your device ID or emulator name
            "automationName": "UiAutomator2",  # Driver for Android
            "appPackage": "com.hyperstock",  # Your app's package name
            "appActivity": "com.hyperstock.main.entry_module.view.act.SplashAct",  # Your app's activity
            "appWaitActivity": "com.hyperstock.*",  # Wait for the main activity
            "appWaitDuration": 60000,  # Duration (milliseconds) to wait for app to start
            "noReset": True,  # Don't reset app state between sessions
            "fullContextList": True,  # Enable hybrid app support (for webview/native interaction)
            "newCommandTimeout": 300,  # Timeout for new commands before session is terminated
            "autoGrantPermissions": True,  # Automatically grant permissions
            "skipDeviceInitialization": True,  # Skip initialization for faster tests
            "clearSystemFiles": True,  # Clear app data before session
            "disableWindowAnimation": True,  # Disable animations for faster tests
            "udid": "R5CT91K1G6L",  # Device UDID if using a real device
            "uiautomator2ServerInstallTimeout": 60000  # Increase timeout for server installation
        }


        options = AppiumOptions()
        options.load_capabilities(caps)
        return webdriver.Remote("http://localhost:4723", options=options)
