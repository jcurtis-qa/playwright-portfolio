from decimal import Decimal

from playwright.sync_api import Page


class CheckoutTwo:
    URL = "https://www.saucedemo.com/checkout-step-two.html"

    def __init__(self, page: Page):
        # Define references to commonly used locators
        self.page = page

        self.title = page.locator('[data-test="title"]')

        self.shopping_cart = page.locator('[data-test="shopping-cart-link"]')
        self.cart_list = page.locator('[data-test="cart-list"]')
        self.inventory_items = page.locator('[data-test="inventory-item"]')
        self.item_prices = page.locator('[data-test="inventory-item-price"]')

        self.item_total = page.locator('[data-test="subtotal-label"]')
        self.tax = page.locator('[data-test="tax-label"]')
        self.total = page.locator('[data-test="total-label"]')

        self.finish_button = page.locator('[data-test="finish"]')

    def load(self):
        self.page.goto(self.URL)

    def item_total_value(self) -> Decimal:
        return Decimal(self.item_total.inner_text().split("$")[-1])

    def tax_value(self) -> Decimal:
        return Decimal(self.tax.inner_text().split("$")[-1])

    def total_value(self) -> Decimal:
        return Decimal(self.total.inner_text().split("$")[-1])

    def summed_item_value(self) -> Decimal:
        return sum(
            Decimal(num.split("$")[-1]) for num in self.item_prices.all_inner_texts()
        )
