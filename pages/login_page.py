from playwright.sync_api import Page


class LoginPage:
    URL = "https://www.saucedemo.com"

    def __init__(self, page: Page):
        # Define references to commonly used locators
        self.page = page
        self.username = page.locator('[data-test="username"]')
        self.password = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')

        self.title = page.locator('[data-test="title"]')

        self.error = page.locator('[data-test="error"]')

    def load(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
