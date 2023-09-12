import allure
import pytest

from ui_pages.forms_page import FormsPage


@allure.suite('Forms page')
@pytest.mark.lesson_19
class TestFormsPage:

    def test_forms_page(self, browser):
        page = FormsPage(browser)
        page.open_forms_page()
        page.check_forms_page_is_opened()
        page.open_practice_form_page()
        page.fill_in_student_registration_form()

    @pytest.mark.xfail
    def test_select_state_and_city(self, browser):
        page = FormsPage(browser)
        page.select_state_and_city()

    def test_check_form(self, browser):
        page = FormsPage(browser)
        page.click_submit_button()
        page.check_filled_form()
        page.back_to_home_page()
