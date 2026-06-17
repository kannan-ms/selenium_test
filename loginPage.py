from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ─────────────────────────────────────────
# SETUP
# ─────────────────────────────────────────
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# ─────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────

def open_login_page():
    driver.get("https://the-internet.herokuapp.com/login")
    print("\n🌐 Opened login page")

def do_login(username, password):
    username_box = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    username_box.clear()
    username_box.send_keys(username)

    password_box = driver.find_element(By.ID, "password")
    password_box.clear()
    password_box.send_keys(password)

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

def get_message():
    try:
        # Try ID first
        flash = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        return flash.text
    except:
        pass

    try:
        # Try class name
        flash = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(@class,'flash')]")))
        return flash.text
    except:
        pass

    try:
        # Try getting current URL — if login passed, URL changes
        current_url = driver.current_url
        if "secure" in current_url:
            return "You logged into a secure area"
        else:
            return "Login failed — stayed on login page"
    except:
        return "Could not get message"

# ─────────────────────────────────────────
# TEST CASE 1 — CORRECT LOGIN
# ─────────────────────────────────────────
print("\n" + "="*50)
print("TEST CASE 1: Login with correct credentials")
print("="*50)

open_login_page()
do_login("tomsmith", "SuperSecretPassword!")
time.sleep(2)

message = get_message()

if "You logged into a secure area" in message:
    print(" TEST PASSED — Login successful!")
    print(f"   Message: {message.strip()}")
else:
    print(" TEST FAILED!")
    print(f"   Message: {message.strip()}")

time.sleep(2)

# ─────────────────────────────────────────
# TEST CASE 2 — WRONG PASSWORD
# ─────────────────────────────────────────
print("\n" + "="*50)
print("TEST CASE 2: Login with wrong password")
print("="*50)

open_login_page()
do_login("tomsmith", "wrongpassword123")
time.sleep(2)

message = get_message()

# Check URL stayed on login page
current_url = driver.current_url
if "login" in current_url:
    print("✅ TEST PASSED — Wrong password rejected correctly!")
    print(f"   Still on login page: {current_url}")
    print(f"   Message: {message.strip()}")
else:
    print("❌ TEST FAILED — Wrong password was accepted!")

time.sleep(2)

# ─────────────────────────────────────────
# TEST CASE 3 — EMPTY FIELDS
# ─────────────────────────────────────────
print("\n" + "="*50)
print("TEST CASE 3: Login with empty fields")
print("="*50)

open_login_page()
do_login("", "")
time.sleep(2)

message = get_message()

current_url = driver.current_url
if "login" in current_url:
    print("✅ TEST PASSED — Empty fields rejected correctly!")
    print(f"   Still on login page: {current_url}")
    print(f"   Message: {message.strip()}")
else:
    print("❌ TEST FAILED — Empty fields were accepted!")

time.sleep(2)

# ─────────────────────────────────────────
# SUMMARY
# ─────────────────────────────────────────
print("\n" + "="*50)
print("ALL TEST CASES COMPLETED!")
print("="*50)

driver.quit()
print("✅ Browser closed!")