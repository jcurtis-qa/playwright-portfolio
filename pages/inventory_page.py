from playwright.sync_api import Page

class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        # Define references to commonly used locators
        self.page = page
        self.title = page.locator('[data-test="title"]')

        self.inventory_items = page.locator('[data-test="inventory-item"]')

        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')

        self.item_prices = page.locator('[data-test="inventory-item-price"]')

    def load(self):
        self.page.goto(self.URL)

    def select_sort(self, option: str):
        self.sort_dropdown.select_option(label=option)