from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, browser=WebDriver):
        self.browser = browser
