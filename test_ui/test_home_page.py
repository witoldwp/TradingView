from playwright.sync_api import Playwright, sync_playwright, expect
from page_object_model.home_page_elements import HomePage


def test_home_page(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.tradingview.com/")

    home_page = HomePage(page)
    expect(home_page.logo).to_be_visible()

