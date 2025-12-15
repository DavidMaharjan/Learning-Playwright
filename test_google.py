import re
from playwright.sync_api import Page, expect

def test_google_search(page: Page):
    page.goto("https://playwright.dev/python/docs/intro")
    page.wait_for_timeout(2000)  # Wait for page to fully load
    
    # Try to close cookie banner
    try:
        page.get_by_role("button", name="Accept all").click()
        page.wait_for_timeout(1000)
    except Exception as e:
        print(f"No cookie banner found: {e}")
    expect(page).to_have_title(re.compile("Installation | Playwright Python"))
    page.close()