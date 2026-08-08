import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_shop_1(driver):
    driver.get("http://testshop.qa-practice.com/")

    link = driver.find_element(By.CLASS_NAME, "oe_product_image_link")

    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(
        Keys.CONTROL
    ).perform()

    driver.switch_to.window(driver.window_handles[1])

    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add_to_cart"))
    )

    add_button.click()

    continue_shopping = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "btn-secondary"))
    )

    assert "Customizable Desk" in driver.page_source

    continue_shopping.click()

    driver.close()

    driver.switch_to.window(driver.window_handles[0])

    driver.refresh()

    WebDriverWait(driver, 10).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )

    cart = WebDriverWait(driver, 10).until(
        lambda driver: next(
            (
                element
                for element in driver.find_elements(By.XPATH, '//a[@href="/shop/cart"]')
                if element.is_displayed() and element.is_enabled()
            ),
            False,
        )
    )

    cart.click()

    WebDriverWait(driver, 10).until(EC.url_contains("/shop/cart"))

    assert "Customizable Desk" in driver.page_source


def test_shop_2(driver):
    driver.get("http://testshop.qa-practice.com/")

    link = driver.find_element(By.CLASS_NAME, "oe_product_image_link")

    ActionChains(driver).move_to_element(link).perform()

    cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "a-submit"))
    )

    cart_button.click()

    product_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "modal-body"))
    )

    assert "Customizable Desk" in product_name.text
