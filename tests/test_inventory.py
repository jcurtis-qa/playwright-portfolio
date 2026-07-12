from pages.inventory_page import InventoryPage

from playwright.sync_api import Page, expect

def test_product_count(logged_in_page: Page):
    # Create new inventory page from a logged in page
    inventory_page = InventoryPage(logged_in_page)
    
    # Expect product count to match inventory list
    expect(inventory_page.inventory_items).to_have_count(6)


def test_sort_ascending(logged_in_page: Page):
    # Create new inventory page from a logged in page
    inventory_page = InventoryPage(logged_in_page)

    # Sort items by ascending price
    inventory_page.select_sort("Price (low to high)")

    # Use expect to await confirmation of sort
    expect(inventory_page.sort_dropdown).to_have_value("lohi")

    # Get the list of all inventory prices
    prices = [float(t.removeprefix("$")) for t in inventory_page.item_prices.all_text_contents()]
    
    # Ensure prices are sorted ascending as expected
    assert prices == sorted(prices)