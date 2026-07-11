import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

from playwright.sync_api import Page, expect

def test_product_count(page: Page):
    # For demonstration purposes, login using the LoginPage class
    login_page = LoginPage(page)
    login_page.load()
    login_page.login('standard_user','secret_sauce')

    # Reframe context as an InventoryPage, now logged in
    inventory_page = InventoryPage(page)
    
    # Expect product count to match inventory list
    expect(inventory_page.inventory_items).to_have_count(6)


def test_sort_ascending(page: Page):
    # For demonstration purposes, login using the LoginPage class
    login_page = LoginPage(page)
    login_page.load()
    login_page.login('standard_user','secret_sauce')

    # Reframe context as an InventoryPage, now logged in
    inventory_page = InventoryPage(page)

    # Sort items by ascending price
    inventory_page.select_sort('Price (low to high)')

    # Use expect to await confirmation of sort
    expect(inventory_page.sort_dropdown).to_have_value('lohi')

    # Get the list of all inventory prices
    prices = [float(t.removeprefix("$")) for t in inventory_page.item_prices.all_text_contents()]
    
    # Ensure prices are sorted ascending as expected
    assert prices == sorted(prices)