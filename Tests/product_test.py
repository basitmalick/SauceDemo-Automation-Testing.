from pages.login_page import LoginPage
from pages.product_page import ProductPage
import time


class TestProduct:

    def test_complete_product_flow(self, driver):

        # =========================
        # LOGIN
        # =========================

        login = LoginPage(driver)

        login.enter_username("standard_user")
        time.sleep(2)

        login.enter_password("secret_sauce")
        time.sleep(2)

        login.click_login()
        time.sleep(3)

        # =========================
        # PRODUCT PAGE
        # =========================

        product = ProductPage(driver)

        # Show product list
        products = product.get_product_list()

        print("Number of products:", len(products))

        time.sleep(3)

        # =========================
        # PRODUCT NAMES
        # =========================

        names = product.get_product_names()

        for name in names:
            print("Product:", name.text)

        time.sleep(3)

        # =========================
        # PRODUCT DESCRIPTIONS
        # =========================

        descriptions = product.get_product_descriptions()

        for description in descriptions:
            print("Description:", description.text)

        time.sleep(3)

        # =========================
        # PRODUCT PRICES
        # =========================

        prices = product.get_product_prices()

        for price in prices:
            print("Price:", price.text)

        time.sleep(3)

        # =========================
        # SORT A TO Z
        # =========================

        print("Sorting A to Z...")

        product.sort_products("az")

        time.sleep(3)

        # =========================
        # SORT Z TO A
        # =========================

        print("Sorting Z to A...")

        product.sort_products("za")

        time.sleep(3)

        # =========================
        # PRICE LOW TO HIGH
        # =========================

        print("Sorting price Low to High...")

        product.sort_products("lohi")

        time.sleep(3)

        # =========================
        # PRICE HIGH TO LOW
        # =========================

        print("Sorting price High to Low...")

        product.sort_products("hilo")

        time.sleep(3)

        # =========================
        # ADD BACKPACK
        # =========================

        print("Adding Backpack...")

        product.add_backpack()

        time.sleep(3)

        # =========================
        # ADD BIKE LIGHT
        # =========================

        print("Adding Bike Light...")

        product.add_bike_light()

        time.sleep(3)

        # =========================
        # OPEN CART
        # =========================

        print("Opening Cart...")

        product.open_cart()

        time.sleep(5)

        # =========================
        # VERIFY CART
        # =========================

        assert "cart" in driver.current_url

        print("Cart opened successfully!")

        time.sleep(3)