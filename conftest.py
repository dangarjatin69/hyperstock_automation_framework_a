import pytest
import allure
from drivers.driver_setup import DriverSetup
import os
import json
import getpass
import socket

# Fixture for setting up the WebDriver for Appium-based Android tests
@pytest.fixture(scope="session")
def driver():
    # Setup: Initialize driver once per session
    drv = DriverSetup.get_driver()
    yield drv
    # Teardown: Quit driver after session ends
    drv.quit()

# pytest configuration hook to add custom metadata for Allure reports
def pytest_configure(config):
    # Optional: Add custom metadata to Allure report
    config._metadata['Project Name'] = 'HyperStock Automation'
    config._metadata['Environment'] = 'QA'
    config._metadata['Tester'] = 'JD'

    # Optional: Add custom metadata to environment
    allure.environment(
        **{
            'Project Name': 'HyperStock Automation',
            'Environment': 'QA',
            'Tester': 'JD',
            'Platform': 'Android',  # Platform specific to your app
            'Automation Tool': 'Appium',  # Automation tool used
        }
    )

# Hook to write custom data into Allure environment.properties and executor.json before the session starts
def pytest_sessionstart(session):
    """Write Allure environment.properties and executor.json"""
    platform = 'Android'  # Set the platform as Android for app testing
    results_dir = os.path.join("reports", "allure-results")
    os.makedirs(results_dir, exist_ok=True)

    # Allure environment.properties (stores environment-related data like platform, automation tool)
    env_path = os.path.join(results_dir, "environment.properties")
    with open(env_path, "w") as f:
        f.write(f"Platform={platform}\n")  # Platform for your app (Android)
        f.write("OS=macOS\n")  # OS Type
        f.write("Environment=Staging\n")  # Set the environment (e.g., QA, Staging)

    # Allure executor.json (stores executor-related info like executor name, build name, etc.)
    executor_path = os.path.join(results_dir, "executor.json")
    executor_info = {
        "name": "Local Run",
        "type": "manual",  # Can change to automated if applicable
        "buildName": f"Local Build - {socket.gethostname()}",  # Hostname of the machine
        "executor": getpass.getuser()  # Executor (the user running the tests)
    }
    with open(executor_path, "w") as f:
        json.dump(executor_info, f, indent=4)  # Write executor info in json format
