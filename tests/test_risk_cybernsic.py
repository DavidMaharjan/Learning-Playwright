import uuid, re 
from playwright.sync_api import Page, expect

def fillform1(page):
    page.get_by_role("textbox",name="Enter Name (e.g. Data Breach Risk)").fill(str(uuid.uuid4().hex[:12]))
    page.locator("button").filter(has_text="Select Category").click()
    page.get_by_role("option").nth(1).click()
    page.get_by_text("Select Threat").click()
    page.get_by_role("option").nth(1).click()

def test_add_risk (page : Page) :
    page.goto("https://dashboard.dev01.cyberensic.ai/sign-in")
    email=page.get_by_role("textbox", name="Enter your email (eg, john@")
    password=page.get_by_role("textbox", name="Enter your password")
    email.fill("maharjandavid4@gmail.com")
    password.fill("Cyberensic@512")
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(5000)
    page.pause()
    page.get_by_role("button",name="Risk").first.click()
    page.get_by_role("button", name="Risk").nth(1).click()
    page.locator("//span[text()='Risk Register']").click()
    expect(page.get_by_role("heading", name="Manage Organisation Risk")).to_be_visible()
    page.get_by_role("button", name="Add Risk").click()
    expect(page.get_by_role("heading",name="Register New Risk")).to_be_visible()
    fillform1(page)
    
    
    
    

    
    
