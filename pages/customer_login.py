from playwright.sync_api import expect
import allure
from pages.base_page import BasePage
from pages.locators import login_locators as loc


class CustomerLogin(BasePage):
    page_url = "/web/login"

    @allure.step("Enter email")
    def enter_email(self, email):
        self.find(loc.email_field_loc).fill(email)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.find(loc.password_field_loc).fill(password)

    @allure.step("Click the button")
    def click_submit_button(self):
        self.find("//button[text()='Log in']").click()

    @allure.step("Check error message")
    def check_error_alert(self, text):
        error_alert = self.page.locator(".alert-danger")
        expect(error_alert).to_be_visible(timeout=10000)
        expect(error_alert).to_have_text(text)
