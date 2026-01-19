from pages.contact_page import ContactPage
from utils.data_factory import generate_contact_form_data
from utils.config import CONTACT_URL

EXPECTED_DROPDOWN_OPTIONS = [
    "Please Select",
    "Jalasoft Services",
    "Join Our Team",
    "Get Training",
    "Others",
]


def test_schedule_call_form_fields(page):
    page.goto(CONTACT_URL)

    contact = ContactPage(page)
    contact.wait_for_form()

    contact.validate_dropdown_options(EXPECTED_DROPDOWN_OPTIONS)

    data = generate_contact_form_data()
    contact.fill_form(data)

    assert contact.is_visible(contact.SUBMIT_BUTTON)
    assert contact.is_enabled(contact.SUBMIT_BUTTON)





