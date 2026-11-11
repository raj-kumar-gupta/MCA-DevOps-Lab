
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

try:
    file_path = Path(__file__).resolve().parent / "login.html"
    driver.get(file_path.as_uri())

    wait = WebDriverWait(driver, 10)

    def test_login(username, password, expected):
        username_field = driver.find_element(By.ID, "username")
        username_field.clear()
        username_field.send_keys(username)

        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(password)

        driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        ).click()

        wait.until(
            lambda d: d.find_element(
                By.ID, "message"
            ).text == expected
        )

        message = driver.find_element(By.ID, "message").text

        if message == expected:
            print(f"PASS: {expected}")
        else:
            print(f"FAIL: Expected {expected}, Got {message}")

    test_login("admin", "12345", "Login Successful")
    test_login("admin", "wrong123", "Invalid Credentials")

finally:
    driver.quit()
