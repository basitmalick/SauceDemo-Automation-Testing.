import pytest
from selenium import webdriver
import time


@pytest.fixture
def driver():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://www.saucedemo.com/")

    time.sleep(2)

    yield driver

    time.sleep(3)

    driver.quit()