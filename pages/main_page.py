from playwright.sync_api import expect
import allure
from pages.base_page import BasePage


class MainPage(BasePage):
    page_url = "/"

    @allure.step("Check logo text")
    def check_logo_is(self, text):
        logo_title = self.page.locator("#top_menu .dropdown-toggle span")
        expect(logo_title).to_be_visible(timeout=10000)
        expect(logo_title).to_have_text(text)
