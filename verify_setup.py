from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    title = driver.find_element(By.CLASS_NAME, "title").text

    if title == "Products":
        print("✓ Selenium Setup Working")
        print("✓ Login Successful")
        print("✓ Element Located Successfully")
        print("✓ Text Verification Passed")
    else:
        print("✗ Verification Failed")

except Exception as e:
    print("ERROR:", e)

finally:
    driver.quit()