from playwright.sync_api import Page


def test_confirm_alert_ok(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm")

    page.on("dialog", lambda dialog: dialog.accept())

    page.locator(".a-button").click()

    result_text = page.text_content("#result-text")
    assert result_text == "Ok"


def test_new_tab_button(page: Page):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")

    with page.expect_popup() as popup_info:
        page.locator(".a-button").click()

    new_page = popup_info.value

    result_text = new_page.text_content("#result-text")
    assert result_text == "I am a new page in a new tab"

    assert page.locator(".a-button").is_enabled()


def test_color_change_button(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")

    page.wait_for_selector("#colorChange.text-danger")

    page.locator("#colorChange").click()
