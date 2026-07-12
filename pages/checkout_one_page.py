from playwright.sync_api import Page

class CheckoutOne:
    URL = "https://www.saucedemo.com/checkout-step-one.html"

    def __init__(self, page: Page):
        # Define references to commonly used locators
        self.page = page

        self.title = page.locator('[data-test="title"]')

        self.shopping_cart = page.locator('[data-test="shopping-cart-link"]')
   
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.postal_code = page.locator('[data-test="postalCode"]')

        self.continue_button = page.locator('[data-test="continue"]')

    def load(self):
        self.page.goto(self.URL)