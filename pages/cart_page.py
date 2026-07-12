from playwright.sync_api import Page


class CartPage:
    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page: Page):
        # Define references to commonly used locators
        self.page = page
        self.shopping_cart = page.locator('[data-test="shopping-cart-link"]')

        self.cart_list = page.locator('[data-test="cart-list"]')
        self.inventory_items = page.locator('[data-test="inventory-item"]')

        self.checkout_button = page.locator('[data-test="checkout"]')

    def load(self):
        self.page.goto(self.URL)
