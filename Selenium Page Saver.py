from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the webdriver
driver = webdriver.Chrome()

# Open the website
driver.get("http://www.saucedemo.com/")

# Login with credentials
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
login_button.click()


time.sleep(5)

# Extract the webpage and save it
with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(driver.page_source)

# Close the webdriver
driver.quit()
