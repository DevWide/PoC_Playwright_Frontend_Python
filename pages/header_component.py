import re
from playwright.sync_api import expect


class HeaderComponent:
    def __init__(self, page):
        self.page = page

    def _nav(self):
        return self.page.get_by_role("navigation")

    def _link(self, name: str):
        return self._nav().get_by_role("link", name=name)

    def go_to_services(self):
        self._link("Services").hover()
        self._link("Services").click()
        expect(self.page).to_have_url(re.compile(".*/services.*"))

    def go_to_clients(self):
        # Ensure menu is visible again
        self._link("Services").hover()
        self._link("Clients").click(force=True)
        expect(self.page).to_have_url(re.compile(".*/clients.*"))

    def go_to_about_us(self):
        self._link("About Us").click(force=True)
        expect(self.page).to_have_url(re.compile(".*/about.*"))

    def go_to_careers(self):
        self._link("Careers").click(force=True)
        expect(self.page).to_have_url(re.compile(".*/careers.*"))

    def go_to_blog(self):
        self._link("Blog").click(force=True)
        expect(self.page).to_have_url(re.compile(".*/blog.*"))

    def click_schedule_call(self):
        self._link("Schedule a call").click(force=True)
        expect(self.page).to_have_url("https://www.jalasoft.com/contact")





