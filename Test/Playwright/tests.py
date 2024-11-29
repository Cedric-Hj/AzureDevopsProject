import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        # Use WebKit or Firefox, which might be more lightweight than Chromium
        browser = p.webkit.launch(headless=True)  # Replace with 'firefox' for Firefox
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def browser_context(browser):
    context = browser.new_context()
    yield context
    context.close()

def test_page_title(browser_context):
    with browser_context.new_page() as page:
        page.goto('http://192.168.0.101:31806/', timeout=5000)
        title = page.title()
        assert title == "Ced's Webpage"  # Verify the title matches the one in the HTML

def test_dev_environment_text(browser_context):
    with browser_context.new_page() as page:
        page.goto('http://192.168.0.101:31806/', timeout=5000)
        dev_text_visible = page.locator("text=Hello").is_visible(timeout=5000)
        assert dev_text_visible is True  # Ensure the "dev environment" text is visible

def test_version_text(browser_context):
    with browser_context.new_page() as page:
        page.goto('http://192.168.0.101:31806/', timeout=5000)
        version_text = page.locator("#version").text_content(timeout=5000)
        assert version_text == 'v2.0.1'  # Ensure the version is displayed correctly
