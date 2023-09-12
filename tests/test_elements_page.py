import allure
import pytest
from ui_pages.elements_page import ElementsPage, TextBoxPage, CheckBoxPage, RadioButtonPage


@allure.suite('Elements page')
@pytest.mark.lesson_19
class TestElementsPage:

    def test_elements_page(self, browser):
        page = ElementsPage(browser)
        page.open_elements_page()
        page.check_elements_page_is_open()

    def test_text_box_page(self, browser):
        page = TextBoxPage(browser)
        page.open_text_box_page()
        page.enter_full_name()
        page.enter_email()
        page.enter_current_address()
        page.enter_permanent_address()
        page.press_submit_button()
        page.check_full_name()
        page.check_email()
        page.check_current_address()
        page.check_permanent_address()

    def test_check_box_page(self, browser):
        page = CheckBoxPage(browser)
        page.open_check_box_page()
        page.select_desktop_checkbox()
        page.select_downloads_checkbox()
        page.check_desktop_checkbox_selected()
        page.check_downloads_checkbox_selected()

    def test_radio_button_page(self, browser):
        page = RadioButtonPage(browser)
        page.open_radio_button_page()
        page.select_yes_radio_button()
        page.check_yes_button_selected()
        page.select_impressive_radio_button()
        page.check_impressive_button_selected()
        page.check_no_button_disable()
        page.back_to_home_page()
