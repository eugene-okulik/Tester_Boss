from pages.base_page import BasePage
from pages.locators import product_locators as loc
from playwright.sync_api import expect


class ProductPage(BasePage):
    page_url = "/shop"

    def open_first_product(self):
        self.page.locator(loc.first_product_link).first.click()

    def check_product_title_visible(self):
        self.is_element_visible(loc.product_title)

    def check_not_available_message(self):
        self.is_element_visible(loc.not_available_text)

    def check_contact_us_visible(self):
        self.is_element_visible(loc.contact_us_btn)

    def add_to_cart(self):
        self.page.locator(loc.add_to_cart_btn).click()
        self.page.locator(loc.continue_shopping_btn).wait_for(
            state="visible", timeout=15000
        )

    def check_cart_quantity(self, expected_qty: str):
        continue_btn = self.page.locator(loc.continue_shopping_btn)
        if continue_btn.is_visible():
            continue_btn.click()
            continue_btn.wait_for(state="hidden", timeout=10000)
        cart = self.page.locator(loc.cart_quantity).first
        expect(cart).to_have_text(expected_qty)

    def click_terms_and_conditions(self):
        self.page.locator(loc.terms_link).click()

    def check_terms_title(self, expected_title: str):
        self.assert_text_equal(loc.terms_title, expected_title)
