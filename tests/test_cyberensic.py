import re
from playwright.sync_api import Page, expect
def test_page_title(page: Page) :
    page.goto("https://dashboard.dev01.cyberensic.ai/sign-in")
    expect(page).to_have_title(re.compile("Cyberensic"))
    page.wait_for_timeout(3000)

#simulates user login : positive test scenario
def test_user_login(page: Page) :
    page.goto("https://dashboard.dev01.cyberensic.ai/sign-in")
    email=page.get_by_role("textbox", name="Enter your email (eg, john@")
    password=page.get_by_role("textbox", name="Enter your password")
    email.fill("maharjandavid4@gmail.com")
    password.fill("Cyberensic@512")
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_role("heading", name="GRC Operations Centre")).to_be_visible()
    page.wait_for_timeout(5000)
    

    
