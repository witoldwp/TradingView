from playwright.sync_api import Playwright, sync_playwright, expect


def test_log_in(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.tradingview.com/")



    # page.get_by_role("button", name="Open user menu").click()
    # page.get_by_role("menuitem", name="Sign in").click()
    # page.get_by_text("Email").click()
    # page.locator("#email-signin__user-name-input__df553da1-d148-4c28-8858-92e88d056923").click()
    # page.locator("#email-signin__user-name-input__df553da1-d148-4c28-8858-92e88d056923").fill("witold.filarowski@gmail.com")
    # # page.locator("#email-signin__user-name-input__bf6877d3-fcc7-4442-acb4-9732df0b1ae7").press("Tab")
    # # page.locator("#email-signin__password-input__bf6877d3-fcc7-4442-acb4-9732df0b1ae7").fill("witek1993")
    # # page.get_by_role("button", name="Sign in").click()

    # ---------------------
    context.close()
    browser.close()
