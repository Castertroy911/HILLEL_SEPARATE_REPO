import allure
import pytest
from ui_pages.alerts_page import BrowserWindowsPage


@allure.suite('Alerts page')
@pytest.mark.lesson_19
class TestAlertsPage:

    def test_browser_windows_page(self, browser):
        page = BrowserWindowsPage(browser)
        page.open_alerts_and_windows_page()
        page.check_alerts_and_windows_page_open()
        page.open_browser_windows_page()
        page.open_new_tab()
        page.check_text_in_new_tab()
        page.open_new_window()
        page.check_text_in_new_window()
        page.back_to_home_page()
