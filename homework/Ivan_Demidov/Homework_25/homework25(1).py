from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver = webdriver.Chrome()
chrome_driver.get("https://www.qa-practice.com/elements/input/simple")

text_input = chrome_driver.find_element(By.ID, "id_text_string")
chrome_driver.execute_script("arguments[0].scrollIntoView(true);", text_input)
text_input.send_keys("hi")
text_input.send_keys(Keys.ENTER)
find_input = chrome_driver.find_element(By.ID, "result-text")
print(find_input.text)
