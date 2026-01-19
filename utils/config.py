import os

ENV = os.getenv("ENV", "prod")

BASE_URLS = {
    "prod": "https://www.jalasoft.com",
}

BASE_URL = BASE_URLS[ENV]
CONTACT_URL = f"{BASE_URL}/contact"

BROWSER = os.getenv("BROWSER", "chromium")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
SLOW_MO = int(os.getenv("SLOW_MO", "0"))

DEFAULT_TIMEOUT = 10_000
NAVIGATION_TIMEOUT = 20_000
