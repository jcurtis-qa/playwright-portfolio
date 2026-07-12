from pages.checkout_one_page import CheckoutOne
from pages.checkout_two_page import CheckoutTwo
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from playwright.sync_api import Page, expect


def test_checkout(logged_in_page: Page):
    # Create new inventory page from a logged in page
    inventory_page = InventoryPage(logged_in_page)

    # Ensure we have landed on the inventory page with no items in cart
    expect(inventory_page.shopping_cart).to_be_visible()

    # Add the first item to the cart
    inventory_page.add_to_cart("sauce-labs-onesie")

    # Ensure the shopping cart badge exists now, and has the correct count
    shopping_cart_badge = logged_in_page.locator('[data-test="shopping-cart-badge"]')
    expect(shopping_cart_badge).to_be_visible()
    expect(shopping_cart_badge).to_have_text("1")

    # Add the second item to the cart
    inventory_page.add_to_cart("sauce-labs-backpack")

    # Ensure the shopping cart badge exists now, and has the correct count
    shopping_cart_badge = logged_in_page.locator('[data-test="shopping-cart-badge"]')
    expect(shopping_cart_badge).to_be_visible()
    expect(shopping_cart_badge).to_have_text("2")

    # Navigate to the shopping cart page
    inventory_page.shopping_cart.click()

    # Verify that we have reached the shopping cart page
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/cart.html")

    # Reframe context as cart page
    cart_page = CartPage(logged_in_page)

    # Verify that cart integrity has been maintained
    shopping_cart_badge = logged_in_page.locator('[data-test="shopping-cart-badge"]')
    expect(shopping_cart_badge).to_be_visible()
    expect(shopping_cart_badge).to_have_text("2")

    expect(cart_page.inventory_items).to_have_count(2)
    expect(
        cart_page.inventory_items.filter(has_text="Sauce Labs Onesie")
    ).to_have_count(1)
    expect(
        cart_page.inventory_items.filter(has_text="Sauce Labs Backpack")
    ).to_have_count(1)

    # Proceed to checkout
    cart_page.checkout_button.click()

    # Ensure we have reached step one of checkout
    expect(logged_in_page).to_have_url(
        "https://www.saucedemo.com/checkout-step-one.html"
    )
    checkout_one_page = CheckoutOne(logged_in_page)

    # Enter preselected information in the form
    checkout_one_page.first_name.fill("Standard")
    checkout_one_page.last_name.fill("User")
    checkout_one_page.postal_code.fill("54321")
    checkout_one_page.continue_button.click()

    # Ensure we have reached step two of checkout
    expect(logged_in_page).to_have_url(
        "https://www.saucedemo.com/checkout-step-two.html"
    )
    checkout_two_page = CheckoutTwo(logged_in_page)

    # Ensure that we have the correct number of items in the cart
    expect(checkout_two_page.inventory_items).to_have_count(2)

    # Ensure that our prices match the total expectations
    assert (
        checkout_two_page.item_total_value() == checkout_two_page.summed_item_value()
    ), "Sum of item prices does not equal subtotal presented during checkout."
    assert (
        checkout_two_page.item_total_value() + checkout_two_page.tax_value()
    ) == checkout_two_page.total_value(), (
        "Sum of subtotal and tax is not equal to total price during checkout."
    )

    # Complete the checkout process
    checkout_two_page.finish_button.click()

    # Assert that we have reached the checkout complete page
    expect(logged_in_page).to_have_url(
        "https://www.saucedemo.com/checkout-complete.html"
    )
    expect(logged_in_page.locator('[data-test="complete-header"]')).to_have_text(
        "Thank you for your order!"
    )
    expect(logged_in_page.locator('[data-test="complete-text"]')).to_have_text(
        "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
    )
