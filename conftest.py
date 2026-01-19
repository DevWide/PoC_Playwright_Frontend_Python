import pytest
from playwright.sync_api import sync_playwright
from utils.config import (
    BROWSER,
    HEADLESS,
    SLOW_MO,
    DEFAULT_TIMEOUT,
    NAVIGATION_TIMEOUT,
)


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = getattr(playwright_instance, BROWSER).launch(
        headless=HEADLESS,
        slow_mo=SLOW_MO
    )
    yield browser
    browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    context.set_default_timeout(DEFAULT_TIMEOUT)
    context.set_default_navigation_timeout(NAVIGATION_TIMEOUT)

    page = context.new_page()
    yield page

    context.close()
