from playwright.sync_api import Page, expect


class BasePage:
    page_url = ""
    base_url = "http://testshop.qa-practice.com"

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto(f"{self.base_url}{self.page_url}")

    def assert_text_equal(self, locator: str, expected_text: str):
        expect(self.page.locator(locator)).to_have_text(expected_text, timeout=15000)

    def is_element_visible(self, locator: str):
        expect(self.page.locator(locator)).to_be_visible(timeout=15000)
