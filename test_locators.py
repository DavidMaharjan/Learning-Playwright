import re
from playwright.sync_api import Page, expect
def test_role_locator(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page.get_by_role("heading",name="Login")).to_be_visible()
    Username=page.get_by_role("textbox", name="Username")
    Password=page.get_by_role("textbox", name="Password")
    Username.fill("Admin")
    Password.fill("admin123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading",name="Dashboard")).to_be_visible()
    
def test_label_placeholder(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_title(re.compile("OrangeHRM"))
    expect(page.get_by_placeholder("Username")).to_be_visible()
    expect(page.get_by_placeholder("Password")).to_be_visible()
    username=page.get_by_placeholder("Username")
    password=page.get_by_placeholder("Password")
    username.fill("Admin")
    password.fill("admin123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_alt_text("client brand banner")).to_be_visible()


def test_xpath(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page.get_by_alt_text("company-branding")).to_be_visible
    username=page.locator("//input[@name='username']")
    password=page.locator("//input[@name='password']")
    username.fill("Admin")
    password.fill("admin123")
    page.locator("//button[@type='submit']").click()
    expect(page.locator("//h6[text()='Dashboard']")).to_be_visible()
    