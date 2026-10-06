from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CheckoutPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ==================================================
    # CHECKOUT INFORMATION LOCATORS
    # ==================================================

    first_name = (
        By.ID,
        "first-name"
    )

    last_name = (
        By.ID,
        "last-name"
    )

    postal_code = (
        By.ID,
        "postal-code"
    )

    continue_button = (
        By.ID,
        "continue"
    )

    # ==================================================
    # OVERVIEW LOCATORS
    # ==================================================

    checkout_items = (
        By.CLASS_NAME,
        "cart_item"
    )

    checkout_item_names = (
        By.CLASS_NAME,
        "inventory_item_name"
    )

    checkout_item_prices = (
        By.CLASS_NAME,
        "inventory_item_price"
    )

    subtotal = (
        By.CLASS_NAME,
        "summary_subtotal_label"
    )

    tax = (
        By.CLASS_NAME,
        "summary_tax_label"
    )

    total = (
        By.CLASS_NAME,
        "summary_total_label"
    )

    finish_button = (
        By.ID,
        "finish"
    )

    # ==================================================
    # ORDER CONFIRMATION
    # ==================================================

    confirmation_message = (
        By.CLASS_NAME,
        "complete-header"
    )

    # ==================================================
    # ENTER FIRST NAME
    # ==================================================

    def enter_first_name(self, name):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.first_name
            )
        )

        field.send_keys(name)

        time.sleep(2)

    # ==================================================
    # ENTER LAST NAME
    # ==================================================

    def enter_last_name(self, name):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.last_name
            )
        )

        field.send_keys(name)

        time.sleep(2)

    # ==================================================
    # ENTER POSTAL CODE
    # ==================================================

    def enter_postal_code(self, code):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.postal_code
            )
        )

        field.send_keys(code)

        time.sleep(2)

    # ==================================================
    # CONTINUE
    # ==================================================

    def click_continue(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.continue_button
            )
        )

        button.click()

        time.sleep(3)

    # ==================================================
    # GET CHECKOUT ITEMS
    # ==================================================

    def get_checkout_items(self):

        items = self.driver.find_elements(
            *self.checkout_items
        )

        time.sleep(2)

        return items

    # ==================================================
    # GET CHECKOUT ITEM NAMES
    # ==================================================

    def get_checkout_item_names(self):

        names = self.driver.find_elements(
            *self.checkout_item_names
        )

        time.sleep(2)

        return names

    # ==================================================
    # GET CHECKOUT ITEM PRICES
    # ==================================================

    def get_checkout_item_prices(self):

        prices = self.driver.find_elements(
            *self.checkout_item_prices
        )

        time.sleep(2)

        return prices

    # ==================================================
    # GET SUBTOTAL
    # ==================================================

    def get_subtotal(self):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.subtotal
            )
        )

        return element.text

    # ==================================================
    # GET TAX
    # ==================================================

    def get_tax(self):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.tax
            )
        )

        return element.text

    # ==================================================
    # GET TOTAL
    # ==================================================

    def get_total(self):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.total
            )
        )

        return element.text

    # ==================================================
    # FINISH ORDER
    # ==================================================

    def click_finish(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.finish_button
            )
        )

        button.click()

        time.sleep(4)

    # ==================================================
    # GET CONFIRMATION MESSAGE
    # ==================================================

    def get_confirmation_message(self):

        message = self.wait.until(
            EC.visibility_of_element_located(
                self.confirmation_message
            )
        )

        return message.text