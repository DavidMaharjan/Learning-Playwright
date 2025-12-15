from playwright.sync_api import sync_playwright
with sync_playwright() as p:
        # Launch the browser (set headless=False to see it)
        browser = p.chromium.launch(headless=False)
        
        # Create a new browser page
        page = browser.new_page()
        
        # Navigate to Google
        page.goto("https://www.google.com")
        
        # Wait a bit so you can see the page
        page.wait_for_timeout(3000)
        
        # Close the browser
        browser.close()
        
        