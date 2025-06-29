import time
import uuid
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config.selenium_config import driver

BASE_URL = "http://localhost:3000"  

def test_user_workflow(driver):
    driver.get(f"{BASE_URL}/login")

    # Login

driver.find_element(By.Name, "email").send_keys("admin@example.com")
driver.find_element(By.Name, "password").send_keys("adminpassword")
driver.find_element(By.TAG_NAME, "form").submit()
time.sleep(1) # wait for login to be completed

assert "Dashboard" in driver.title

#Navigate to Users page
driver.find_element(By.LINK_TEXT, "users").click()
time.sleep(1) #wait for page to load

#Create a new user
driver.find_element(By.ID, "create_user_button").click()
time.sleep(1) # wait for modal to open

unique_email = f"user_{uuid.uuid4().hex[:6]}@example.com"
driver.find_element(By.Name, "name").send_keys("Test User")
driver.find_element(By.Name, "email").send_keys(unique_email)
driver.find_element(By.Name, "role").send_keys("user")
driver.find_element(By.CSS_SELECTOR, "form").submit()
time.sleep(1)

assert unique_email in driver.page_source 

# Edit the user
driver.find_element(By.XPATH, f"//tr[td[text()='{unique_email}']]//button[text()='Edit']").click()
time.sleep(1)
driver.find_element(By.name,"name").clear()
driver.find_element(By.name, "name").send_keys("Updated User")
driver.find_element(By.CSS_SELECTOR, "form").submit()
time.sleep(1)

assert "Updated User" in driver.page_source

# Delete user
driver.find_element(By.XPATH, f"//tr[td[text()='{unique_email}']]//button[text()='Delete']").click()
time.sleep(1)
driver.find_element(By.ID, "confirm-delete").click()
time.sleep(2)

assert unique_email not in driver.page_source

#Log out
driver.find_element(By.ID, "logout").click()
time.sleep(1)
assert "Login" in driver.page_source

