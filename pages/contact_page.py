from pages.base_page import BasePage
from playwright.sync_api import expect
import time


class ContactPage(BasePage):
    FIRST_NAME = "input[name='firstname']"
    LAST_NAME = "input[name='lastname']"
    EMAIL = "input[name='email']"
    PHONE = "input[name='phone']"

    COMPANY_WEBSITE = (
        "input[name='website'], "
        "input[name='companywebsite'], "
        "input[type='url']"
    )

    INTEREST_DROPDOWN = "select"
    MESSAGE = "textarea"
    SUBMIT_BUTTON = "input[type='submit'], button[type='submit']"

    def wait_for_form(self):
        expect(self.page.locator(self.FIRST_NAME)).to_be_visible(timeout=30_000)

    def fill_form(self, data: dict):
        self._fill_with_scroll(self.FIRST_NAME, data["first_name"])
        self._fill_with_scroll(self.LAST_NAME, data["last_name"])
        self._fill_with_scroll(self.EMAIL, data["email"])
        self._fill_with_scroll(self.PHONE, data["phone"])

        self._fill_optional(self.COMPANY_WEBSITE, data.get("company_url"))

        dropdown = self.page.locator(self.INTEREST_DROPDOWN)
        self._scroll_center(dropdown)
        dropdown.select_option(label=data["interest"])

        self._fill_with_scroll(self.MESSAGE, data["message"])

    def validate_dropdown_options(self, expected_options: list[str]):
        dropdown = self.page.locator(self.INTEREST_DROPDOWN)
        expect(dropdown).to_be_visible(timeout=30_000)

        actual = [
            opt.text_content().strip()
            for opt in dropdown.locator("option").all()
        ]

        assert actual == expected_options

    def _fill_with_scroll(self, selector: str, value: str):
        locator = self.page.locator(selector).first
        self._scroll_center(locator)
        locator.fill(value)

    def _fill_optional(self, selector: str, value: str | None):
        if not value:
            return

        locator = self.page.locator(selector)
        if locator.count() == 0:
            print("ℹ️ Company Website field not present — skipping")
            return

        self._scroll_center(locator.first)
        locator.first.fill(value)

    def _scroll_center(self, locator):
        """
        Real human-like scroll (slow + visible)
        """
        self.page.evaluate(
            """el => el.scrollIntoView({behavior: 'smooth', block: 'center'})""",
            locator.element_handle(),
        )
        time.sleep(0.8)



