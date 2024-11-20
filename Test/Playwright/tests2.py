import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=True)  # Replace with 'firefox' for Firefox
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def browser_context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # We only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if hasattr(rep, "wasxfail") else "w"
        with open("failures", mode) as f:
            if "browser_context" in item.fixturenames:
                context = item.funcargs["browser_context"]
                page = context.new_page()
                screenshot_path = f"playwright-report/{item.name}.png"
                page.screenshot(path=screenshot_path)
                if hasattr(item, "add_report_section"):
                    item.add_report_section("call", "screenshot", screenshot_path)
                else:
                    pytest_html = item.config.pluginmanager.getplugin("html")
                    extra = getattr(rep, "extra", [])
                    extra.append(pytest_html.extras.image(screenshot_path))
                    rep.extra = extra

def test_page_title(browser_context):
    with browser_context.new_page() as page:
        page.goto('http://192.168.0.101:31806/', timeout=5000)
        title = page.title()
        assert title == "Ced's Webpage"  # Verify the title matches the one in the HTML

def test_dev_environment_text(browser_context):
    with browser_context.new_page() as page:
        page.goto('http://192.168.0.101:31806/', timeout=5000)
        dev_text_visible = page.locator("text=dev environment").is_visible(timeout=5000)
        assert dev_text_visible is True  # Ensure the "dev environment" text is visible

def test_version_text(browser_context):
    with browser_context.new_page() as page:
        page.goto('http://192.168.0.101:31806/', timeout=5000)
        version_text = page.locator("#version").text_content(timeout=5000)
        assert version_text == 'v2.0.3'  # Ensure the version is displayed correctly
