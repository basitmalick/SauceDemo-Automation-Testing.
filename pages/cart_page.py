 from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ==================================================
    # LOCATORS
    # ==================================================

    cart_items = (
        By.CLASS_NAME,
        "cart_item"
    )

    cart_item_names = (
        By.CLASS_NAME,
        "inventory_item_name"
    )

    cart_item_prices = (
        By.CLASS_NAME,
        "inventory_item_price"
    )

    remove_backpack_button = (
        By.ID,
        "remove-sauce-labs-backpack"
    )

    remove_bike_light_button = (
        By.ID,
        "remove-sauce-labs-bike-light"
    )

    continue_shopping_button = (
        By.ID,
        "continue-shopping"
    )

    # NEW
    checkout_button = (
        By.ID,
        "checkout"
    )

    # ==================================================
    # CART ITEMS
    # ==================================================

    def get_cart_items(self):

        items = self.driver.find_elements(
            *self.cart_items
        )

        time.sleep(2)

        return items

    # ==================================================
    # CART ITEM NAMES
    # ==================================================

    def get_cart_item_names(self):

        names = self.driver.find_elements(
            *self.cart_item_names
        )

        time.sleep(2)

        return names

    # ==================================================
    # CART ITEM PRICES
    # ==================================================

    def get_cart_item_prices(self):

        prices = self.driver.find_elements(
            *self.cart_item_prices
        )

        time.sleep(2)

        return prices

    # ==================================================
    # REMOVE BACKPACK
    # ==================================================

    def remove_backpack(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.remove_backpack_button
            )
        )

        button.click()

        time.sleep(3)

    # ==================================================
    # REMOVE BIKE LIGHT
    # ==================================================

    def remove_bike_light(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.remove_bike_light_button
            )
        )

        button.click()

        time.sleep(3)

    # ==================================================
    # CONTINUE SHOPPING
    # ==================================================

    def continue_shopping(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.continue_shopping_button
            )
        )

        button.click()

        time.sleep(3)

    # ==================================================
    # CHECKOUT
    # ==================================================

    def click_checkout(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.checkout_button
            )
        )

        button.click()

        time.sleep(3)