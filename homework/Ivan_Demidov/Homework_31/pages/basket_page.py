from pages.base_page import BasePage
from pages.locators import basket_locators as loc


class BasketPage(BasePage):
    page_url = "/shop/cart"

    def check_text(self, expected_text: str):
        self.assert_text_equal(loc.header_text_loc, expected_text)

    def check_cart_message(self, expected_message: str):
        self.assert_text_equal(loc.empty_cart_text, expected_message)

    def check_about_us_text(self, expected_text: str):
        self.assert_text_equal(loc.about_us_text, expected_text)
