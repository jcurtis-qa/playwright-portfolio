import pytest
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

@pytest.mark.parametrize(
        "username,password,expected_error",
        [
            ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
            ("standard_user", "incorrect_password", "Epic sadface: Username and password do not match any user in this service"),
            ("no_user", "secret_sauce", "Epic sadface: Username and password do not match any user in this service"),
            ("","secret_sauce", "Epic sadface: Username is required"),
            ("username","","Epic sadface: Password is required")
        ],
        ids=["locked-out-user", "incorrect-password", "unknown-user", "empty-username", "empty-password"]
)

# Tests for preventing login of a locked out user
def test_login_failures(page: Page, username, password, expected_error):
    # Navigate to the test page
    page.goto("https://www.saucedemo.com")

    # Log in using error state user credentials
    page.locator('[data-test="username"]').fill(username)
    page.locator('[data-test="password"]').fill(password)
    page.locator('[data-test="login-button"]').click()
    
    # Ensure the error element is visible, and contains expected text
    error = page.locator('[data-test="error"]')
    expect(error).to_be_visible()
    expect(error).to_have_text(expected_error)