import pytest
from pages.login_page import LoginPage

from playwright.sync_api import Page, expect


# Tests for successful login of a standard user
def test_standard_user_can_log_in(page: Page):
    # Create the login page object for this test's browser page
    login_page = LoginPage(page)

    # Navigate to the test page
    login_page.load()

    # Log in using standard user's credentials
    login_page.login("standard_user", "secret_sauce")

    # Ensure we have navigated to the inventory page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(login_page.title).to_have_text("Products")


@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        (
            "locked_out_user",
            "secret_sauce",
            "Epic sadface: Sorry, this user has been locked out.",
        ),
        (
            "standard_user",
            "incorrect_password",
            "Epic sadface: Username and password do not match any user in this service",
        ),
        (
            "no_user",
            "secret_sauce",
            "Epic sadface: Username and password do not match any user in this service",
        ),
        ("", "secret_sauce", "Epic sadface: Username is required"),
        ("username", "", "Epic sadface: Password is required"),
    ],
    ids=[
        "locked-out-user",
        "incorrect-password",
        "unknown-user",
        "empty-username",
        "empty-password",
    ],
)

# Tests for expected login failure states
def test_login_failures(page: Page, username, password, expected_error):
    # Create the login page object for this test's browser page
    login_page = LoginPage(page)

    # Navigate to the test page
    login_page.load()

    # Log in using error state user credentials
    login_page.login(username, password)

    # Ensure the error element is visible, and contains expected text
    expect(login_page.error).to_be_visible()
    expect(login_page.error).to_have_text(expected_error)
