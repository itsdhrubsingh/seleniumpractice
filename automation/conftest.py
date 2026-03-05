import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from configs.config import Config

def pytest_addoption(parser):
    """Add command line options to pytest."""
    parser.addoption(
        "--env", action="store", default="prod", help="Environment to run tests against: dev, qa, prod"
    )

def pytest_configure(config):
    """Configure pytest based on command line options."""
    env_name = config.getoption("--env").lower()
    # Reload config with the specified environment
    Config.load(env_name)

@pytest.fixture(scope="function")
def driver():
    # Setup - Initializing Driver using Config class
    browser = Config.BROWSER
    headless = Config.HEADLESS
    implicit_wait = Config.IMPLICIT_WAIT
    
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif browser == "firefox":
        # Add support for other browsers if needed
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Browser {browser} is not supported")

    driver.implicitly_wait(implicit_wait)
    driver.maximize_window()
    
    yield driver
    
    # Teardown - Quitting Browser
    driver.quit()
