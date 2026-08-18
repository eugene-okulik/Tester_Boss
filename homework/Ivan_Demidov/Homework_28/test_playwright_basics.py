from playwright.sync_api import Page


def test_authentication(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Form Authentication").click()
    page.get_by_role("textbox", name="Username").fill("Aboba")
    page.get_by_role("textbox", name="Password").fill("123456789")
    page.get_by_role("button", name="Login").click()


def test_automation_practice_form(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")

    page.locator("#firstName").fill("Tester_Boss")
    page.locator("#lastName").fill("Smith")
    page.locator("#userEmail").fill("vasuapupkin@milo.com")

    page.get_by_label("Other").check()

    page.get_by_placeholder("Mobile Number").fill("+1234567890")

    page.fill("#dateOfBirthInput", "17 Aug 2026")

    page.locator("#subjectsInput").fill("English")
    page.get_by_text("English", exact=True).click()
    page.keyboard.press("Escape")

    page.get_by_label("Reading").check()

    page.locator("#currentAddress").fill("Lenin's street")

    page.locator("#state").click()
    page.get_by_text("NCR").click()

    page.locator("#city").click()
    page.get_by_text("Delhi").click()

    page.get_by_role("button", name="Submit").click()
