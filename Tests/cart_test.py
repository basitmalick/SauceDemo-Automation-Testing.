from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

import time


class TestSauceDemo:

    def test_complete_sauce_demo(self, driver):

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
        # 2. PRODUCT LIST
        # ==================================================

        print("\n========== PRODUCT LIST ==========")

        product = ProductPage(driver)

        products = product.get_product_list()

        assert len(products) == 6

        print(
            "Products found:",
            len(products)
        )

        time.sleep(3)

        # ==================================================
        # 3. PRODUCT NAMES
        # ==================================================

        print("\n========== PRODUCT NAMES ==========")

        names = product.get_product_names()

        assert len(names) == 6

        for name in names:

            print(
                "Product:",
                name.text
            )

            assert name.text != ""

        time.sleep(3)

        # ==================================================
        # 4. PRODUCT DESCRIPTIONS
        # ==================================================

        print(
            "\n========== PRODUCT DESCRIPTIONS =========="
        )

        descriptions = (
            product.get_product_descriptions()
        )

        assert len(descriptions) == 6

        for description in descriptions:

            print(
                "Description:",
                description.text
            )

            assert description.text != ""

        time.sleep(3)

        # ==================================================
        # 5. PRODUCT PRICES
        # ==================================================

        print(
            "\n========== PRODUCT PRICES =========="
        )

        prices = product.get_product_prices()

        assert len(prices) == 6

        for price in prices:

            print(
                "Price:",
                price.text
            )

            assert price.text.startswith("$")

        time.sleep(3)

        # ==================================================
        # 6. PRODUCT IMAGES
        # ==================================================

        print(
            "\n========== PRODUCT IMAGES =========="
        )

        images = product.get_product_images()

        assert len(images) == 6

        for image in images:

            assert image.is_displayed()

        print(
            "All product images are displayed!"
        )

        time.sleep(3)

        # ==================================================
        # 7. SORT A TO Z
        # ==================================================

        print(
            "\n========== SORT A TO Z =========="
        )

        product.sort_products("az")

        names = product.get_product_names()

        name_list = []

        for name in names:

            name_list.append(
                name.text
            )

        assert name_list == sorted(
            name_list
        )

        print(
            "A to Z sorting successful!"
        )

        time.sleep(3)

        # ==================================================
        # 8. SORT Z TO A
        # ==================================================

        print(
            "\n========== SORT Z TO A =========="
        )

        product.sort_products("za")

        names = product.get_product_names()

        name_list = []

        for name in names:

            name_list.append(
                name.text
            )

        assert name_list == sorted(
            name_list,
            reverse=True
        )

        print(
            "Z to A sorting successful!"
        )

        time.sleep(3)

        # ==================================================
        # 9. PRICE LOW TO HIGH
        # ==================================================

        print(
            "\n========== PRICE LOW TO HIGH =========="
        )

        product.sort_products("lohi")

        prices = product.get_product_prices()

        price_list = []

        for price in prices:

            value = float(
                price.text.replace(
                    "$",
                    ""
                )
            )

            price_list.append(value)

        assert price_list == sorted(
            price_list
        )

        print(
            "Low to High sorting successful!"
        )

        time.sleep(3)

        # ==================================================
        # 10. PRICE HIGH TO LOW
        # ==================================================

        print(
            "\n========== PRICE HIGH TO LOW =========="
        )

        product.sort_products("hilo")

        prices = product.get_product_prices()

        price_list = []

        for price in prices:

            value = float(
                price.text.replace(
                    "$",
                    ""
                )
            )

            price_list.append(value)

        assert price_list == sorted(
            price_list,
            reverse=True
        )

        print(
            "High to Low sorting successful!"
        )

        time.sleep(3)

        # ==================================================
        # 11. ADD BACKPACK
        # ==================================================

        print(
            "\n========== ADD BACKPACK =========="
        )

        product.add_backpack()

        print(
            "Backpack added!"
        )

        time.sleep(2)

        # ==================================================
        # 12. ADD BIKE LIGHT
        # ==================================================

        print(
            "\n========== ADD BIKE LIGHT =========="
        )

        product.add_bike_light()

        print(
            "Bike Light added!"
        )

        time.sleep(2)

        # ==================================================
        # 13. CART COUNT
        # ==================================================

        print(
            "\n========== CART COUNT =========="
        )

        cart_count = product.get_cart_count()

        print(
            "Cart count:",
            cart_count
        )

        assert cart_count == "2"

        print(
            "Cart count is correct!"
        )

        time.sleep(3)

        # ==================================================
        # 14. OPEN CART
        # ==================================================

        print(
            "\n========== OPEN CART =========="
        )

        product.open_cart()

        assert "cart" in driver.current_url

        print(
            "Cart opened successfully!"
        )

        time.sleep(3)

        # ==================================================
        # 15. VERIFY CART ITEMS
        # ==================================================

        print(
            "\n========== VERIFY CART ITEMS =========="
        )

        cart = CartPage(driver)

        items = cart.get_cart_items()

        assert len(items) == 2

        print(
            "Cart items:",
            len(items)
        )

        names = cart.get_cart_item_names()

        cart_names = []

        for name in names:

            cart_names.append(
                name.text
            )

            print(
                "Cart product:",
                name.text
            )

        assert (
            "Sauce Labs Backpack"
            in cart_names
        )

        assert (
            "Sauce Labs Bike Light"
            in cart_names
        )

        print(
            "Both products verified!"
        )

        time.sleep(3)

        # ==================================================
        # 16. REMOVE BACKPACK
        # ==================================================

        print(
            "\n========== REMOVE BACKPACK =========="
        )

        cart.remove_backpack()

        items = cart.get_cart_items()

        assert len(items) == 1

        names = cart.get_cart_item_names()

        assert (
            names[0].text
            == "Sauce Labs Bike Light"
        )

        print(
            "Backpack removed successfully!"
        )

        time.sleep(3)

        # ==================================================
        # 17. CONTINUE SHOPPING
        # ==================================================

        print(
            "\n========== CONTINUE SHOPPING =========="
        )

        cart.continue_shopping()

        assert (
            "inventory"
            in driver.current_url
        )

        print(
            "Returned to Products page!"
        )

        time.sleep(3)

        # ==================================================
        # 18. ADD BACKPACK AGAIN
        # ==================================================

        print(
            "\n========== ADD BACKPACK AGAIN =========="
        )

        product = ProductPage(driver)

        product.add_backpack()

        print(
            "Backpack added again!"
        )

        time.sleep(3)

        # ==================================================
        # 19. OPEN CART AGAIN
        # ==================================================

        print(
            "\n========== OPEN CART AGAIN =========="
        )

        product.open_cart()

        assert (
            "cart"
            in driver.current_url
        )

        print(
            "Cart opened again!"
        )

        time.sleep(3)

        # ==================================================
        # 20. FINAL VERIFICATION
        # ==================================================

        print(
            "\n========== FINAL CART =========="
        )

        cart = CartPage(driver)

        items = cart.get_cart_items()

        assert len(items) == 2

        names = cart.get_cart_item_names()

        final_names = []

        for name in names:

            final_names.append(
                name.text
            )

            print(
                "Final product:",
                name.text
            )

        assert (
            "Sauce Labs Backpack"
            in final_names
        )

        assert (
            "Sauce Labs Bike Light"
            in final_names
        )

        print(
            "\n======================================"
        )

        print(
            "ALL SAUCEDEMO TESTING PASSED!"
        )

        print(
            "======================================"
        )

        time.sleep(5)