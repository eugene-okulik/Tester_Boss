from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_choose_language():
    driver = webdriver.Chrome()
    driver.get("https://www.qa-practice.com/elements/select/single_select")

    select_language = driver.find_element(By.ID, "id_choose_language")
    Select(select_language).select_by_visible_text("Python")

    submit = driver.find_element(By.ID, "submit-id-submit")
    driver.execute_script("arguments[0].click();", submit)

    result_element = driver.find_element(By.ID, "result-text")
    assert result_element.text == "Python"

    driver.quit()


def test_hello_world():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    wait = WebDriverWait(driver, 10)
    finish_element = wait.until(EC.visibility_of_element_located((By.ID, "finish")))

    assert "Hello World!" in finish_element.text

    driver.quit()
