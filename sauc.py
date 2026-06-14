from selenium import webdriver
from selenium.webdriver.common.by import By
import time

test_data = [
    ("standard_user", "secret_sauce"),
    ("standard_user", "wrong_password"),
    ("wrong_user", "secret_sauce"),
    ("", "secret_sauce"),
    ("standard_user", "")
]

driver = webdriver.Chrome()

for username, password in test_data:

    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "password").clear()

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)

    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

if "inventory" in driver.current_url:
    print(f"PASS -> {username} / {password}")

    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    driver.find_element(By.ID, "logout_sidebar_link").click()

else:
    try:
        error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        print(f"FAIL -> {username} / {password}")
        print("Error:", error.text)
    except:
        print(f"FAIL -> {username} / {password}")
        print("Error message not found")

driver.quit()