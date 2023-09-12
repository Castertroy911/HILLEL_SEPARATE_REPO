import pytest
from selenium import webdriver


@pytest.fixture(scope='session', autouse=True)
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get('https://demoqa.com/')
    yield driver
    driver.quit()