from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Chrome options for Linux
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Start browser
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Open Google
driver.get("https://www.google.com")
print("✅ Browser opened successfully!")

# Find search box and type
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python Tutorial")
print("✅ Typed in search box!")

# Press ENTER instead of clicking button (more reliable!)
search_box.send_keys(Keys.RETURN)
print("✅ Search submitted!")

time.sleep(3)

# Count all links on results page
all_links = driver.find_elements(By.TAG_NAME, "a")
print(f"✅ Total links found on page: {len(all_links)}")

driver.quit()
print("✅ Browser closed successfully!")