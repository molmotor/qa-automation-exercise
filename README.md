# QA Automation: automationexercise.com

![Tests](https://github.com/molmotor/qa-automation-exercise/actions/workflows/tests.yml/badge.svg)

UI and API test automation for [automationexercise.com](https://www.automationexercise.com), a practice e-commerce site. Built with Python, pytest, Playwright and requests, and run on every push with GitHub Actions.

## What's covered

**UI tests** (Playwright, `ui_tests/`)
- Home page loads
- Sign up: form visible, advances to account information
- Register a user, verify "Logged in as", delete the account
- Login with valid and invalid credentials
- Search for a product

**API tests** (requests, `api_tests/`)
- GET all products
- POST to products list (unsupported method)
- Search product, with and without the required parameter
- Verify login with valid credentials (user created and deleted by a fixture)
- Verify login with invalid credentials

The UI test cases follow the site's own [test case list](https://www.automationexercise.com/test_cases). Progress is tracked in `test_plan.md`.

## Project structure

```
qa-automation-exercise/
├── .github/workflows/tests.yml   # CI: runs both suites on every push
├── README.md
├── test_plan.md
├── requirements.txt
├── ui_tests/
│   ├── config.py                 # BASE_URL, AUTH_URL
│   ├── conftest.py               # shared fixtures (registered_user)
│   ├── pages/                    # page objects: locators and actions
│   ├── utils/                    # test data generation (Faker)
│   └── tests/                    # one file per feature area
└── api_tests/
    ├── config.py
    ├── conftest.py               # api_user fixture (create and delete via API)
    └── tests/
```

## Setup

Requires Python 3.10+.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```

On Linux or WSL, Chromium may need system libraries:

```bash
playwright install-deps
```

## Running the tests

Run each suite from inside its own folder, with the venv active.

```bash
cd ui_tests
pytest                          # headless
pytest --headed --slowmo 500    # watch the browser
pytest -k test_search_product   # a single test
```

```bash
cd api_tests
pytest
```

## Continuous integration

A GitHub Actions workflow (`.github/workflows/tests.yml`) runs on every push to `main` and on pull requests. It has two parallel jobs, one for the API suite and one for the UI suite, so a failure shows which layer broke. Each job starts on a clean Linux machine, installs `requirements.txt`, and runs `pytest` the same way as locally. The UI job installs Chromium with its system dependencies and uploads Playwright's output if a test fails.

## Design decisions

- **Page objects return values, tests assert.** Page methods find elements and perform actions. They never assert, so the same method can be reused for positive and negative checks. All expectations live in the tests.
- **Dependencies point one way:** tests, then pages, then config.
- **`expect()` instead of `is_visible()` after navigation.** `is_visible()` answers instantly and doesn't wait, which caused false failures right after page loads. Page methods that feed `expect()` return a locator, so Playwright can retry until the element appears.
- **Locators chosen by what the page exposes.** "Logged in as" is plain text, not a link, so a role-based locator could never match it. Reading Playwright's aria snapshot in the failure output showed this.
- **Generated test data.** Faker creates names and addresses, and a UUID makes every signup email unique, so tests never collide with existing accounts. Dropdown values (date of birth, country) are fixed, because random values can fail for reasons unrelated to the test.
- **API error cases assert on the `responseCode` in the response body.** The site often returns HTTP 200 even for errors, so checking only the HTTP status would pass when the API actually rejected the request.
- **Fixtures create and clean up their own data.** The `api_user` fixture creates an account through the API and deletes it after the test, even if the test fails.

## Known issues

- **Retries:** UI tests rerun up to 2 times (`pytest-rerunfailures`) because the public site sometimes returns a "heavy load (queue full)" page. Retries handle external instability, not flaky tests of my own. If a test fails on all 3 attempts, it is a real failure.

- Ad overlays (`#google_vignette`) on the site can occasionally block clicks and cause flaky failures.
- The site is public and shared, so CI can fail when it is slow or down, and tests may leave data behind if they fail before cleanup.

## Next steps

- More UI cases: logout, register with existing email, cart, contact form