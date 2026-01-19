from faker import Faker

fake = Faker()

def generate_contact_form_data() -> dict:
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.msisdn(),
        "company_url": f"https://{fake.domain_name()}",
        "interest": "Jalasoft Services",
        "message": "This is an automated UI test. The form is not submitted."
    }
