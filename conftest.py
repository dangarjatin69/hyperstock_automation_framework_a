import pytest
import allure
from drivers.driver_setup import DriverSetup

@pytest.fixture(scope="session")
def driver():
    # Setup: Initialize driver once per session
    drv = DriverSetup.get_driver()
    yield drv
    # Teardown: Quit driver after session ends
    drv.quit()

def pytest_configure(config):
    # Optional: Add custom metadata to Allure report
    config._metadata['Project Name'] = 'HyperStock Automation'
    config._metadata['Environment'] = 'QA'
    config._metadata['Tester'] = 'JD'
