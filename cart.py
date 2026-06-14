from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://www.saucedemo.com")

# Login
wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Add to cart
wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()

# Go to cart
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

# Checkout (IMPORTANT FIX)
checkout_btn = wait.until(
    EC.element_to_be_clickable((By.ID, "checkout"))
)
checkout_btn.click()

# Verify
if "checkout-step-one" in driver.current_url:
    print("PASS - Checkout reached")
else:
    print("FAIL")

driver.quit()