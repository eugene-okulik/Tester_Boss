from playwright.sync_api import Page, expect, Route
import json
import re


def test_iphone_popup_title(page: Page):
    new_name = "яблокофон 17 про"

    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = new_name
        body = json.dumps(body)
        route.fulfill(response=response, body=body)

    page.route(re.compile("/shop/api/digital-mat"), handle_route)
    page.goto("https://www.apple.com/shop/buy-iphone")
    page.get_by_role("heading", name="iPhone 17 Pro & iPhone 17 Pro Max").click()

    header = page.locator(".rf-digitalmat-overlay-header").first
    expect(header).to_have_text(new_name)
