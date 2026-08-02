from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def main():
    with webdriver.Chrome() as driver:
        driver.implicitly_wait(5)
        driver.get("https://demoqa.com/automation-practice-form")

        driver.find_element(By.ID, "firstName").send_keys("Tester")
        driver.find_element(By.ID, "lastName").send_keys("Boss")
        driver.find_element(By.ID, "userEmail").send_keys("example@mail.com")
        driver.find_element(By.ID, "userNumber").send_keys("1234243242")

        gender_radio = driver.find_element(By.ID, "gender-radio-1")
        driver.execute_script("arguments[0].click();", gender_radio)

        date_input = driver.find_element(By.ID, "dateOfBirthInput")
        driver.execute_script("arguments[0].click();", date_input)

        year_select = driver.find_element(
            By.CSS_SELECTOR, "select.react-datepicker__year-select"
        )
        Select(year_select).select_by_visible_text("2005")

        month_select = driver.find_element(
            By.CSS_SELECTOR, "select.react-datepicker__month-select"
        )
        Select(month_select).select_by_visible_text("June")

        subjects_input = driver.find_element(By.ID, "subjectsInput")
        subjects_input.send_keys("English")
        subjects_input.send_keys(Keys.ENTER)
        subjects_input.send_keys("Maths")
        subjects_input.send_keys(Keys.ENTER)

        hobby = driver.find_element(By.ID, "hobbies-checkbox-1")
        driver.execute_script("arguments[0].click();", hobby)

        state_input = driver.find_element(By.ID, "react-select-3-input")
        state_input.send_keys("NCR")
        state_input.send_keys(Keys.ENTER)

        city_input = driver.find_element(By.ID, "react-select-4-input")
        city_input.send_keys("Delhi")
        city_input.send_keys(Keys.ENTER)

        submit_btn = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].click();", submit_btn)


if __name__ == "__main__":
    main()
