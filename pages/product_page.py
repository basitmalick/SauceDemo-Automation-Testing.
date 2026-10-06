from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ==================================================
    # LOCATORS
    # ==================================================

    product_list = (By.CLASS_NAME, "inventory_item")

    product_names = (
        By.CLASS_NAME,
        "inventory_item_name"
    )

    product_descriptions = (
        By.CLASS_NAME,
        "inventory_item_desc"
    )

    product_prices = (
        By.CLASS_NAME,
        "inventory_item_price"
    )

    # FIXED PRODUCT IMAGE LOCATOR
    product_images = (
        By.CSS_SELECTOR,
        ".inventory_item_img img"
    )

    sorting_dropdown = (
        By.CLASS_NAME,
        "product_sort_container"
    )

    backpack_button = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    bike_light_button = (
        By.ID,
        "add-to-cart-sauce-labs-bike-light"
    )

    cart_button = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    cart_badge = (
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    # ==================================================
    # PRODUCT LIST
    # ==================================================

    def get_product_list(self):

        products = self.driver.find_elements(
            *self.product_list
        )

        time.sleep(2)

        return products

    # ==================================================
    # PRODUCT NAMES
    # ==================================================

    def get_product_names(self):

        names = self.driver.find_elements(
            *self.product_names
        )

        time.sleep(2)

        return names

    # ==================================================
    # PRODUCT DESCRIPTIONS
    # ==================================================

    def get_product_descriptions(self):

        descriptions = self.driver.find_elements(
            *self.product_descriptions
        )

        time.sleep(2)

        return descriptions

    # ==================================================
    # PRODUCT PRICES
    # ==================================================

    def get_product_prices(self):

        prices = self.driver.find_elements(
            *self.product_prices
        )

        time.sleep(2)

        return prices

    # ==================================================
    # PRODUCT IMAGES
    # ==================================================

    def get_product_images(self):

        images = self.driver.find_elements(
            *self.product_images
        )

        time.sleep(2)

        return images

    # ==================================================
    # SORT PRODUCTS
    # ==================================================

    def sort_products(self, option):

        dropdown = self.wait.until(
            EC.element_to_be_clickable(
                self.sorting_dropdown
            )
        )

        Select(dropdown).select_by_value(option)

        time.sleep(3)

    # ==================================================
    # ADD BACKPACK
    # ==================================================

    def add_backpack(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.backpack_button
            )
        )

        button.click()

        time.sleep(3)

    # ==================================================
    # ADD BIKE LIGHT
    # ==================================================

    def add_bike_light(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.bike_light_button
            )
        )

        button.click()

        time.sleep(3)

    # ==================================================
    # GET CART COUNT
    # ==================================================

    def get_cart_count(self):

        badge = self.wait.until(
            EC.visibility_of_element_located(
                self.cart_badge
            )
        )

        time.sleep(2)

        return badge.text

    # ==================================================
    # OPEN CART
    # ==================================================

    def open_cart(self):

        cart = self.wait.until(
            EC.element_to_be_clickable(
                self.cart_button
            )
        )

        cart.click()

        time.sleep(3)