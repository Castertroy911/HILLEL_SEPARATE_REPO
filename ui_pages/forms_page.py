import os.path
import allure
from selenium.webdriver.common.by import By
from . home_page import HomePage
from Data.pages_locators_data import FormsPageLocators as FP
from Data.pages_data import FormsPageData as FPD
from Data.pages_locators_data import PracticeFormPageLocators as PF
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormsPage(HomePage):

    @allure.step('Open practice form page')
    def open_practice_form_page(self):
        element = self.find_element_by_xpath(FP.PRACTICE_FORM_PAGE)
        self.scroll_and_click(element)
        self.find_element_by_xpath(FP.WIDGETS_PAGE_LOCATOR).click()

    @allure.step('Fill in students registration form')
    def fill_in_student_registration_form(self):
        self.find_element_by_xpath(PF.FIRST_NAME).send_keys(FPD.FIRST_NAME)
        self.find_element_by_xpath(PF.LAST_NAME).send_keys(FPD.LAST_NAME)
        self.find_element_by_xpath(PF.EMAIL).send_keys(FPD.EMAIL)
        self.find_element_by_xpath(PF.GENDER).click()
        self.find_element_by_xpath(PF.MOBILE).send_keys(FPD.MOBILE)
        self.find_element_by_xpath(PF.DATE_OF_BIRTH_FIELD).click()
        self.find_element_by_xpath(PF.DATE_OF_BIRTH_DAY).click()

        self.find_element_by_xpath(PF.HOBBIES_SPORT).click()
        self.find_element_by_xpath(PF.HOBBIES_MUSIC).click()

        path = os.path.abspath('../Test_artifacts/space.jpg')
        self.find_element_by_xpath(PF.PICTURE).send_keys(path)
        self.find_element_by_xpath(PF.CURRENT_ADDRESS).send_keys(FPD.CURRENT_ADDRESS)

    @allure.step('Select state and city')
    def select_state_and_city(self):
        state = self.find_element_by_xpath(PF.STATE)
        self.scroll_and_click(state)
        state.send_keys(Keys.ENTER)

        city = self.find_element_by_xpath(PF.CITY)
        self.scroll_and_click(city)
        city.send_keys(Keys.ENTER)

    @allure.step('Click submit button')
    def click_submit_button(self):
        self.find_element_by_xpath(PF.SUBMIT_BUTTON).click()

    @allure.step('Check filed form')
    def check_filled_form(self):
        form = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, PF.CONFIRM_MODAL_FORM)))
        assert form, 'Confirmation modal form is not showed'
        self.find_element_by_xpath(PF.CLOSE_MODAL_BUTTON).click()
