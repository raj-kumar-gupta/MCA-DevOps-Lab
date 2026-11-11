
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open Chrome browser
driver = webdriver.Chrome()

try:
    # Open local login page
    file_path = Path(__file__).resolve().parent / "Login.html"
    driver.get(file_path.as_uri())

    wait = WebDriverWait(driver, 10)

    def test_login(username, password, expected):
        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "username").send_keys(username)

        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys(password)

        driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        ).click()

        message = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "message")
            )
        ).text

        if message == expected:
            print(f"PASS: {expected}")
        else:
            print(f"FAIL: Expected {expected}, Got {message}")

    # Test Case 1: Valid Login
    test_login("admin", "12345", "Login Successful")

    # Test Case 2: Invalid Login
    test_login("admin", "wrong123", "Invalid Credentials")

finally:
    driver.quit()
