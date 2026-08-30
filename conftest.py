import pytest
from playwright.sync_api import BrowserContext

from pages.main_page import MainPage
from pages.customer_login import CustomerLogin


@pytest.fixture()
def main_page(page):
    return MainPage(page)


@pytest.fixture()
def customer_login(page):
    return CustomerLogin(page)


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    return page
