import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        yield context
        browser.close()

def test_page_title(browser_context):
    with browser_context.new_page() as page:
        print("Navigating to the page...")
        page.goto('http://192.168.0.101:31804/', timeout=10000)  # 30-second timeout
        print("Page loaded, checking title...")
        title = page.title()
        assert title == "Ced's Webpage"  # Verify the title matches the one in the HTML

def test_dev_environment_text(browser_context):
    with browser_context.new_page() as page:
        print("Navigating to the page...")
        page.goto('http://192.168.0.101:31804/', timeout=10000)
        print("Page loaded, checking for 'dev environment' text...")
        dev_text_visible = page.locator("text=dev environment").is_visible(timeout=10000)
        assert dev_text_visible is True  # Ensure the "dev environment" text is visible

def test_version_text(browser_context):
    with browser_context.new_page() as page:
        print("Navigating to the page...")
        page.goto('http://192.168.0.101:31804/', timeout=10000)
        print("Page loaded, checking version text...")
        version_text = page.locator("#version").text_content(timeout=10000)
        assert version_text == 'v2.0.3'  # Ensure the version is displayed correctly
