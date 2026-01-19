import time
from utils.config import DEFAULT_TIMEOUT, NAVIGATION_TIMEOUT


class BasePage:
    def __init__(self, page):
        self.page = page
        self.page.set_default_timeout(DEFAULT_TIMEOUT)
        self.page.set_default_navigation_timeout(NAVIGATION_TIMEOUT)

    # ---------- Navigation ----------
    def navigate(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")

    # ---------- Common helpers ----------
    def slow_scroll_to(self, locator, delay: float = 0.5):
        """
        Scroll to element smoothly and wait briefly so user can see it.
        """
        locator.first.scroll_into_view_if_needed()
        time.sleep(delay)

    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()

    def is_enabled(self, selector: str) -> bool:
        return self.page.locator(selector).is_enabled()


