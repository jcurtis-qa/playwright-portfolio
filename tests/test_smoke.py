from playwright.sync_api import Page, expect


def test_login_page_loads(page: Page):
    # Navigate to our page
    page.goto("https://www.saucedemo.com")

    # Expect a specific page title
    expect(page).to_have_title("Swag Labs")

    # Expect features of the login container to be present for future testing
    expect(page.locator('[data-test="username"]')).to_be_visible()
    expect(page.locator('[data-test="password"]')).to_be_visible()
    expect(page.locator('[data-test="login-button"]')).to_be_visible()

    # Expect features of the login credentials container to be present
    expect(page.locator('[data-test="login-credentials"]')).to_be_visible()
    expect(page.locator('[data-test="login-password"]')).to_be_visible()
