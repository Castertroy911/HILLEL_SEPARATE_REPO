import allure
from helper import Helper
from Data.pages_locators_data import HomePageLocators as HP


class HomePage(Helper):

    @allure.step('Open elements page')
    def open_elements_page(self):
        element = self.find_element_by_xpath(HP.ELEMENTS_PAGE_LOCATOR)
        self.scroll_and_click(element)

    @allure.step('Check that elements page is open')
    def check_elements_page_is_open(self):
        self.check_page_open('elements')

    @allure.step('Open forms page')
    def open_forms_page(self):
        element = self.find_element_by_xpath(HP.FORMS_PAGE_LOCATOR)
        self.scroll_and_click(element)

    @allure.step('Check that forms page is open')
    def check_forms_page_is_opened(self):
        self.check_page_open('forms')

    @allure.step('Open alerts and windows page')
    def open_alerts_and_windows_page(self):
        element = self.find_element_by_xpath(HP.ALERTS_PAGE_LOCATOR)
        self.scroll_and_click(element)

    @allure.step('Check that alerts and windows page is open')
    def check_alerts_and_windows_page_open(self):
        self.check_page_open('alertsWindows')

    @allure.step('Return user to home page')
    def back_to_home_page(self):
        element = self.find_element_by_xpath(HP.HOME_PAGE_LOCATOR)
        self.scroll_and_click(element)
