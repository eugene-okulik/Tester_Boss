from pages.base_page import BasePage
from pages.locators import desks_locators as loc
from playwright.sync_api import expect


class DesksPage(BasePage):
    page_url = "/shop/category/desks-1"

    def click_first_product(self):
        self.page.locator(loc.first_product_link).first.click()

    def add_to_cart(self):
        self.page.locator(loc.add_to_cart_btn).click()
        self.page.locator(loc.continue_shopping_btn).wait_for(
            state="visible", timeout=15000
        )

    def check_continue_shopping_visible(self):
        self.is_element_visible(loc.continue_shopping_btn)

    def click_continue_shopping(self):
        self.page.locator(loc.continue_shopping_btn).click()

    def check_cart_quantity(self, expected_qty: str):
        cart = self.page.locator(loc.cart_quantity).first
        expect(cart).to_have_text(expected_qty)

    def check_add_to_cart_visible(self):
        self.is_element_visible(loc.add_to_cart_btn)

    def check_product_title(self, expected_title: str):
        self.assert_text_equal(loc.product_title, expected_title)

    def click_logo(self):
        self.page.locator(loc.logo_link).first.click()

    def check_categories_title(self, expected_title: str):
        self.assert_text_equal(loc.categories_text, expected_title)
