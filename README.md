# Playwright Test Automation Portfolio

This repository demonstrates a step-by-step creation of a Playwright Test Suite from scratch to fully functional end-to-end UI tests utilizing Python + Playwright.

The tests run against [SauceDemo](https://www.saucedemo.com), SauceLabs' open demo site for automation practice.

Each capability was developed, refined, and committed one step at a time. Full commit history and messages are available.

## Highlight: full checkout E2E

[`tests/test_checkout.py`](tests/test_checkout.py) walks the entire purchase journey: login (via fixture) -> add two products -> cart verification -> checkout form -> **order math validation** -> order confirmation.

Details worth noticing:
- Every page transition is anchored with a URL assertion before proceeding.
- Cart contents are verified order-independently with locator filters.
- The summary screen's math is checked two ways: line items vs. subtotal, and subtotal + tax vs. total, using `Decimal` for exact currency arithmetic.
- No sleeps, no manual waits anywhere — Playwright auto-waiting plus
  retrying `expect` assertions.

## Structure

- `pages/` — page object model: one class per page, locators + actions only, no assertions
- `tests/` — pytest suites: login (parametrized failure cases), inventory (sorting, product counts), checkout E2E
- `conftest.py` — shared fixtures, including `logged_in_page`

## Run it yourself
```bash
    # Clone the repository
    git clone https://github.com/jcurtis-qa/playwright-portfolio.git
    # Change directories to the cloned repo
    cd playwright-portfolio
    # Instantiate the python virtual environment
    python -m venv .venv
    
    # Start the virtual environment
    # - Windows
    .venv\Scripts\activate          
    # - macOS/Linux: 
    source .venv/bin/activate

    # Install the requirements
    pip install -r requirements.txt
    playwright install chromium

    # Run the tests!
    pytest                          # run everything (headless)
    pytest --headed --slowmo 500    # watch it work
    pytest tests/test_checkout.py   # just the E2E
```

## Tooling

- **pytest** with parametrization and custom fixtures
- **Ruff** for formatting and linting (`ruff format`, `ruff check`)
- Locator strategy: `data-test` attributes throughout

## Roadmap

- Session-scoped authentication via `storage_state`
- GitHub Actions CI running the suite on every push
- Cross-browser runs (Firefox/WebKit)