from playwright.sync_api import Page, expect

# Tests for successful login of a standard user
def test_standard_user_can_log_in(page: Page):
    # Navigate to the test page
    page.goto("https://www.saucedemo.com")

    # Log in using standard user's credentials
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    # Ensure we have navigated to the inventory page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Products")

# Tests for preventing login of a locked out user
def test_locked_out_user_login(page: Page):
    # Navigate to the test page
    page.goto("https://www.saucedemo.com")

    # Log in using locked user credentials
    page.locator('[data-test="username"]').fill("locked_out_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    
    # Ensure the error element is visible, and contains expected text
    error = page.locator('[data-test="error"]')
    expect(error).to_be_visible()
    expect(error).to_have_text("Epic sadface: Sorry, this user has been locked out.")