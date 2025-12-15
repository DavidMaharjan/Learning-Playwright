import re
from playwright.sync_api import Page, expect
def test_page_title(page: Page) :
    page.goto("https://uat.cyberensic.ai/sign-in")
    expect(page).to_have_title(re.compile("Cyberensic"))
    page.wait_for_timeout(3000)
    
def test_user_login(page: Page) :
    page.goto("https://uat.cyberensic.ai/sign-in")
    email=page.get_by_role("textbox", name="Enter your email (eg, john@")
    password=page.get_by_role("textbox", name="Enter your password")
    email.fill("")
    password.fill("")
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Password is incorrect. Try again, or use another method.")).to_be_visible()
    
