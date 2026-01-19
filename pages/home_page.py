from pages.base_page import BasePage
from pages.header_component import HeaderComponent
from utils.config import BASE_URL  

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.header = HeaderComponent(page)

    def open(self):
        self.navigate(BASE_URL)
