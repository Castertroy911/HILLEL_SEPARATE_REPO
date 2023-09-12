import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session', autouse=True)
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="114.0.5735.90").install()))
    driver.maximize_window()
    driver.get('https://demoqa.com/')
    yield driver
    driver.quit()
