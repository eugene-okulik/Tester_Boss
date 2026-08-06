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


def test__shop_1(driver):
    driver.get("http://testshop.qa-practice.com/")

    link = driver.find_element(By.CLASS_NAME, "oe_product_image_link")

    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(
        Keys.CONTROL
    ).perform()

    driver.switch_to.window(driver.window_handles[1])

    add_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "add_to_cart"))
    )

    driver.execute_script("arguments[0].click();", add_button)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-secondary"))
    ).click()

    driver.close()

    driver.switch_to.window(driver.window_handles[0])

    driver.refresh()

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
