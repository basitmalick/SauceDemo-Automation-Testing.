from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

import time


class TestCheckout:

    def test_complete_checkout(self, driver):

        # ==================================================
        # 1. LOGIN
        # ==================================================

        print("\n========== LOGIN ==========")

        login = LoginPage(driver)

        login.enter_username(
            "standard_user"
        )

        login.enter_password(
            "secret_sauce"
        )

        login.click_login()

        assert "inventory" in driver.current_url

        print("Login successful!")

        time.sleep(3)

        # ==================================================
        # 2. ADD PRODUCTS
        # ==================================================

        print("\n========== ADD PRODUCTS ==========")

        product = ProductPage(driver)

        product.add_backpack()

        print("Backpack added!")

        time.sleep(2)

        product.add_bike_light()

        print("Bike Light added!")

        time.sleep(3)

        # ==================================================
        # 3. VERIFY CART COUNT
        # ==================================================

        print("\n========== CART COUNT ==========")

        cart_count = product.get_cart_count()

        print("Cart count:", cart_count)

        assert cart_count == "2"

        print("Cart count is correct!")

        time.sleep(3)

        # ==================================================
        # 4. OPEN CART
        # ==================================================

        print("\n========== OPEN CART ==========")

        product.open_cart()

        assert "cart" in driver.current_url

        print("Cart opened successfully!")

        time.sleep(3)

        # ==================================================
        # 5. VERIFY CART
        # ==================================================

        print("\n========== VERIFY CART ==========")

        cart = CartPage(driver)

        items = cart.get_cart_items()

        assert len(items) == 2

        print("Cart items:", len(items))

        names = cart.get_cart_item_names()

        cart_names = []

        for name in names:

            cart_names.append(name.text)

            print(
                "Cart product:",
                name.text
            )

        assert "Sauce Labs Backpack" in cart_names

        assert "Sauce Labs Bike Light" in cart_names

        print("Both products verified!")

        time.sleep(3)

        # ==================================================
        # 6. CLICK CHECKOUT
        # ==================================================

        print("\n========== CHECKOUT ==========")

        cart.click_checkout()

        assert "checkout-step-one" in driver.current_url

        print("Checkout page opened successfully!")

        time.sleep(3)

        # ==================================================
        # 7. ENTER CUSTOMER INFORMATION
        # ==================================================

        print("\n========== CUSTOMER INFORMATION ==========")

        checkout = CheckoutPage(driver)

        checkout.enter_first_name(
            "Abdul"
        )

        checkout.enter_last_name(
            "Basit"
        )

        checkout.enter_postal_code(
            "44000"
        )

        print("Customer information entered!")

        time.sleep(3)

        # ==================================================
        # 8. CONTINUE TO OVERVIEW
        # ==================================================

        print("\n========== CHECKOUT OVERVIEW ==========")

        checkout.click_continue()

        assert "checkout-step-two" in driver.current_url

        print("Checkout overview opened!")

        time.sleep(3)

        # ==================================================
        # 9. VERIFY CHECKOUT ITEMS
        # ==================================================

        print("\n========== VERIFY CHECKOUT ITEMS ==========")

        checkout_items = checkout.get_checkout_items()

        assert len(checkout_items) == 2

        print(
            "Checkout items:",
            len(checkout_items)
        )

        names = checkout.get_checkout_item_names()

        checkout_names = []

        for name in names:

            checkout_names.append(
                name.text
            )

            print(
                "Checkout product:",
                name.text
            )

        assert "Sauce Labs Backpack" in checkout_names

        assert "Sauce Labs Bike Light" in checkout_names

        print("Checkout products verified!")

        time.sleep(3)

        # ==================================================
        # 10. VERIFY PRICES
        # ==================================================

        print("\n========== VERIFY PRICES ==========")

        prices = checkout.get_checkout_item_prices()

        assert len(prices) == 2

        for price in prices:

            print(
                "Product price:",
                price.text
            )

            assert price.text.startswith("$")

        print("Product prices verified!")

        time.sleep(3)

        # ==================================================
        # 11. VERIFY SUBTOTAL
        # ==================================================

        print("\n========== VERIFY SUBTOTAL ==========")

        subtotal = checkout.get_subtotal()

        print(
            "Subtotal:",
            subtotal
        )

        assert "Item total:" in subtotal

        print("Subtotal displayed correctly!")

        time.sleep(3)

        # ==================================================
        # 12. VERIFY TAX
        # ==================================================

        print("\n========== VERIFY TAX ==========")

        tax = checkout.get_tax()

        print(
            "Tax:",
            tax
        )

        assert "Tax:" in tax

        print("Tax displayed correctly!")

        time.sleep(3)

        # ==================================================
        # 13. VERIFY TOTAL
        # ==================================================

        print("\n========== VERIFY TOTAL ==========")

        total = checkout.get_total()

        print(
            "Total:",
            total
        )

        assert "Total:" in total

        print("Total displayed correctly!")

        time.sleep(3)

        # ==================================================
        # 14. FINISH ORDER
        # ==================================================

        print("\n========== FINISH ORDER ==========")

        checkout.click_finish()

        print("Finish button clicked!")

        time.sleep(4)

        # ==================================================
        # 15. VERIFY ORDER CONFIRMATION
        # ==================================================

        print("\n========== ORDER CONFIRMATION ==========")

        confirmation = checkout.get_confirmation_message()

        print(
            "Confirmation:",
            confirmation
        )

        assert confirmation == "Thank you for your order!"

        print("Order completed successfully!")

        print("\n======================================")

        print(
            "ALL CHECKOUT TESTING PASSED!"
        )

        print("======================================")

        time.sleep(5)