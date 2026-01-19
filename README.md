# Jalasoft Playwright SDET Automation Framework

## Project Overview

This project is a **UI automation framework built with Playwright and Python**, following **Object-Oriented Programming (OOP)**, **SOLID principles**, and the **Page Object Model (POM)** pattern.

The application under test is the public website:

https://www.jalasoft.com

This repository was created as a **portfolio-grade SDET project**, designed to demonstrate real-world automation practices, including CI pipelines, dynamic DOM handling, and safe execution against production environments.

---

## Project Goals

- Demonstrate professional-level UI test automation
- Apply clean architecture and scalable design patterns
- Automate dynamic, third-party forms (HubSpot)
- Ensure safe, non-invasive execution in PROD
- Provide a CI-ready framework suitable for interviews

---

## Architecture & Design Principles

### Design Patterns & Principles
- Page Object Model (POM)
- SOLID principles
- Separation of concerns
- Reusable and maintainable components
- Defensive automation strategies

### Key Characteristics
- No hardcoded URLs inside tests
- Centralized configuration management
- Environment-driven execution
- Human-like scrolling and interactions
- Resilient selectors for dynamic DOM elements

---

## Project Structure

```markdown
JalaSoft_Playwright_SDET/
│
├── pages/
│ ├── base_page.py # Shared browser actions and helpers
│ ├── home_page.py # Home page object
│ ├── header_component.py # Header navigation component
│ └── contact_page.py # Contact / Schedule a Call page
│
├── tests/
│ ├── test_header_navigation.py
│ └── test_schedule_call_form.py
│
├── utils/
│ ├── config.py # Environment, URLs and browser config
│ ├── test_data.py # Static test data
│ └── data_factory.py # Dynamic test data (Faker)
│
├── .github/
│ └── workflows/
│ └── playwright.yml # GitHub Actions CI pipeline
│
├── Makefile # Standardized project commands
├── conftest.py # Pytest + Playwright fixtures
├── requirements.txt
└── README.md
```

---

## Configuration Management

All environment and browser configuration is centralized in:

utils/config.py

Examples:

```python
BASE_URL = "https://www.jalasoft.com"
CONTACT_URL = f"{BASE_URL}/contact"

BROWSER = "chromium"
HEADLESS = false
```

NOTE: Configuration is fully compatible with both local execution and CI pipelines.

---

## Standardized Commands (Makefile)

This project uses a Makefile to standardize all commands, similar to npm scripts.

### Available commands:
make install   # Create virtual environment and install dependencies
make test      # Run tests locally (headed browser)
make test-ci   # Run tests in CI mode (headless)
make clean     # Remove venv and cache files

This enrures:
* Same commands locally and in CI
* No duplicated setup logic
* Easy onboarding for new contributors

---

## Running the Project Locally

1. Prerequisites

* Python 3.12+
* Git
* Make (Git Bash or WSL on Windows)

---
2. Setup environment
```bash
make install
```
This will:
* Create a virtual environment
* Install Python dependencies
* Install Playwright browsers and system dependencies

---
3. Run tests locally
```bash
make test
```
* Browser opens (headed mode)
* Smooth scrolling
* Visual form filling

---
4. Deactivate virtual environment (optional)
```bash
deactivate
```

---

## Continuous Integration (GitHub Actions)
This project includes a **GitHub Actions CI pipeline** that runs automatically on:

* Push to main / master
* Pull requests

CI Highlights:
* Ubuntu runner 
* Python 3.12
* Playwright installed with system dependencies
* Headless execution
* Uses the same Makefile commands as local execution

### Pipeline file:

```bash
.github/workflows/playwright.yml
```

---

## Test Coverage

### Header Navigation Tests

**File:** `test_header_navigation.py`

Validates navigation through the website header:

- Services  
- Clients  
- About Us  
- Careers  
- Blog  

Ensures correct navigation and URL validation.

---

### Schedule a Call / Contact Form Tests

**File:** `test_schedule_call_form.py`

This test demonstrates advanced automation techniques:

- Navigates safely to `/contact`
- Waits for dynamic HubSpot form loading
- Validates dropdown options
- Smooth scrolling while filling fields
- Handles optional fields defensively
- **Does NOT submit the form (safe for PROD)**

---

## Handling Dynamic Third-Party Forms (HubSpot)

The Jalasoft contact form is powered by **HubSpot**, which introduces:

- Dynamic DOM updates  
- Optional and unstable fields  
- A/B testing variations  

This framework addresses these challenges by:

- Using resilient, non-brittle selectors  
- Treating optional fields as best-effort  
- Avoiding hard iframe dependencies  
- Preventing false-negative test failures  

---

## Why the Form Is Not Submitted

Form submission is intentionally skipped to:

- Avoid sending data to a real production system  
- Prevent side effects in PROD  
- Keep tests idempotent and repeatable  
- Follow ethical automation practices  

---

## Technology Stack

- Python 3.12+
- Playwright (Python)
- Pytest
- Faker
- Git
- GitHub Actions
- Make

---

## Author

Automation framework developed as an **SDET portfolio and interview-ready project**, focusing on clean architecture, real-world constraints, and production-aware automation practices.

---

## License

This project is intended for educational and demonstration purposes only.


