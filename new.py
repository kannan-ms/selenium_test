from selenium import webdriver
from selenium.webdriver.common.by import By 
browser = webdriver.Chrome()
browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
print("open browser")
title = browser.title
print("title: " + title)
