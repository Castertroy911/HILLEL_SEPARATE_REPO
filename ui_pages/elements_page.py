import allure
from . home_page import HomePage
from Data.pages_locators_data import ElementsPageLocators as EP
from Data.pages_locators_data import TextBoxPageLocators as TBL
from Data.pages_locators_data import CheckBoxPageLocators as CBL
from Data.pages_locators_data import RadioButtonPageLocators as RBL
from Data.pages_data import TextBoxPageData as TBD


class ElementsPage(HomePage):

    @allure.step('Open text box page')
    def open_text_box_page(self):
        element = self.find_element_by_xpath(EP.TEXT_BOX_PAGE_LOCATOR)
        self.scroll_and_click(element)

    @allure.step('Open checkbox page')
    def open_check_box_page(self):
        element = self.find_element_by_xpath(EP.CHECK_BOX_PAGE_LOCATOR)
        self.scroll_and_click(element)

    @allure.step('Open radiobutton page')
    def open_radio_button_page(self):
        element = self.find_element_by_xpath(EP.RADIO_BUTTON_PAGE_LOCATOR)
        self.scroll_and_click(element)


class TextBoxPage(ElementsPage):

    @allure.step('Enter full name')
    def enter_full_name(self):
        element = self.find_element_by_xpath(TBL.ENTER_FULL_NAME_LOCATOR)
        self.scroll_to_element(element)
        element.send_keys(TBD.FULL_NAME)

    @allure.step('Enter email')
    def enter_email(self):
        element = self.find_element_by_xpath(TBL.ENTER_EMAIL_LOCATOR)
        self.scroll_to_element(element)
        element.send_keys(TBD.EMAIL)

    @allure.step('Enter current address')
    def enter_current_address(self):
        element = self.find_element_by_xpath(TBL.ENTER_CURRENT_ADDRESS_LOCATOR)
        self.scroll_to_element(element)
        element.send_keys(TBD.CURRENT_ADDRESS)

    @allure.step('Enter permanent address')
    def enter_permanent_address(self):
        element = self.find_element_by_xpath(TBL.ENTER_PERMANENT_ADDRESS_LOCATOR)
        self.scroll_to_element(element)
        element.send_keys(TBD.PERMANENT_ADDRESS)

    @allure.step('Press submit button')
    def press_submit_button(self):
        element = self.find_element_by_xpath(TBL.SUBMIT_BUTTON_LOCATOR)
        self.scroll_and_click(element)

    @allure.step('Check full name')
    def check_full_name(self):
        name = self.find_element_by_xpath(TBL.CHECK_FULL_NAME_LOCATOR)
        self.scroll_to_element(name)
        name = name.text
        assert TBD.FULL_NAME in name, 'Full name is not saved or saved incorrect'

    @allure.step('Check email')
    def check_email(self):
        email = self.find_element_by_xpath(TBL.CHECK_EMAIL_LOCATOR)
        self.scroll_to_element(email)
        email = email.text
        assert TBD.EMAIL in email, 'Email is not saved or saved incorrect'

    @allure.step('Check current address')
    def check_current_address(self):
        address = self.find_element_by_xpath(TBL.CHECK_CURRENT_ADDRESS_LOCATOR)
        self.scroll_to_element(address)
        address = address.text
        assert TBD.CURRENT_ADDRESS in address, 'Current address is not saved or saved incorrect'

    @allure.step('Check permanent address')
    def check_permanent_address(self):
        address = self.find_element_by_xpath(TBL.CHECK_PERMANENT_ADDRESS_LOCATOR)
        self.scroll_to_element(address)
        address = address.text
        assert TBD.PERMANENT_ADDRESS in address, 'Permanent address is not saved or saved incorrect'


class CheckBoxPage(ElementsPage):

    @allure.step('Select desktop checkbox')
    def select_desktop_checkbox(self):
        self.find_element_by_xpath(CBL.COLLAPSE_LIST).click()
        element = self.find_element_by_xpath(CBL.DESKTOP_CHECKBOX_LOCATOR)
        self.scroll_and_click(element)

    @allure.step('Select downloads checkbox')
    def select_downloads_checkbox(self):
        element = self.find_element_by_xpath(CBL.DESKTOP_CHECKBOX_LOCATOR)
        self.scroll_and_click(element)

    @allure.step('Check that desktop checkbox is selected')
    def check_desktop_checkbox_selected(self):
        class_data = self.find_element_by_xpath(CBL.DESKTOP_CHECKBOX_LOCATOR)
        self.scroll_to_element(class_data)
        class_data = class_data.get_attribute('class')
        assert 'check' in class_data, '"Desktop" checkbox is not selected'

    @allure.step('Check that downloads checkbox is selected')
    def check_downloads_checkbox_selected(self):
        class_data = self.find_element_by_xpath(CBL.DOWNLOADS_CHECKBOX_LOCATOR)
        self.scroll_to_element(class_data)
        class_data = class_data.get_attribute('class')
        assert 'check' in class_data, '"Downloads" checkbox is not selected'


class RadioButtonPage(ElementsPage):

    @allure.step('Select "yes" radiobutton')
    def select_yes_radio_button(self):
        element = self.find_element_by_xpath(RBL.YES_RADIO_BUTTON)
        self.scroll_and_click(element)

    @allure.step('Select "impressive" radiobutton')
    def select_impressive_radio_button(self):
        element = self.find_element_by_xpath(RBL.IMPRESSIVE_RADIO_BUTTON)
        self.scroll_and_click(element)

    @allure.step('Check that yes button is selected')
    def check_yes_button_selected(self):
        text = self.find_element_by_xpath(RBL.SELECTED_BUTTON_LOCATOR)
        self.scroll_to_element(text)
        text = text.text
        assert 'yes' in text.lower(), '"Yes" radio button is not selected'

    @allure.step('Check that impressive button is selected')
    def check_impressive_button_selected(self):
        text = self.find_element_by_xpath(RBL.SELECTED_BUTTON_LOCATOR)
        self.scroll_to_element(text)
        text = text.text
        assert 'impressive' in text.lower(), '"Impressive" radio button is not selected'

    @allure.step('Check that no button is disabled')
    def check_no_button_disable(self):
        class_data = self.find_element_by_xpath(RBL.NO_RADIO_BUTTON)
        self.scroll_to_element(class_data)
        class_data = class_data.get_attribute('class')
        assert 'disabled' in class_data, "'No' radio button is enabled, but it shouldn't"
