import re 
import uuid
import random
from playwright.sync_api import Page, expect

def test_page_title(page:Page):
    page.goto("https://dashboard.dev01.cyberensic.ai/sign-up")
    expect(page.locator("//h1[text()='Create your account']")).to_be_visible()

#simulates the signup process : positive test scenario
def test_signup(page:Page):
    page.goto("https://dashboard.dev01.cyberensic.ai/sign-up")
    first_name=page.locator("#firstName")
    last_name=page.locator("#lastName")
    email=page.locator("#email")
    phone=page.locator("#phone")
    company=page.locator("#companyName")
    first_name.fill("John")
    last_name.fill("Cena")
    email.fill(uuid.uuid4().hex[:10]+"@gmail.com")
    phone.fill(str(random.randint(1000000000,9999999999)))
    company.fill("Cyberensic")
    page.get_by_role("button", name="Sign Up").click()
    page.wait_for_load_state("networkidle")
    expect(page.get_by_text("Signup request sent successfully")).to_be_visible()
    