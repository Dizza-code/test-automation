# ui_tests/test_real_time_updates.py

import time
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

BASE_URL = "http://localhost:3000"  

def init_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1440,900")
    return webdriver.Chrome(options=options)

def login(driver, email, password):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.TAG_NAME, "form").submit()
    time.sleep(1)

def test_real_time_user_creation():
    # Setup two browser instances
    driver_a = init_driver()  # User A
    driver_b = init_driver()  # User B

    try:
        #Login both users
        login(driver_a, "admin@example.com", "adminpassword")
        login(driver_b, "admin@example.com", "adminpassword")

        # Navigate to users page
        driver_a.find_element(By.LINK_TEXT, "Users").click()
        driver_b.find_element(By.LINK_TEXT, "Users").click()
        time.sleep(1)

        # User A creates a new user 
        driver_a.find_element(By.ID, "create-user-btn").click()
        time.sleep(0.5)

        unique_email = f"realtime_{uuid.uuid4().hex[:6]}@example.com"
        driver_a.find_element(By.NAME, "name").send_keys("Realtime Test")
        driver_a.find_element(By.NAME, "email").send_keys(unique_email)
        driver_a.find_element(By.NAME, "role").send_keys("user")
        driver_a.find_element(By.CSS_SELECTOR, "form").submit()
        time.sleep(2)

        # User B sees the new user without refresh
        retries = 5
        found = False
        for _ in range(retries):
            if unique_email in driver_b.page_source:
                found = True
                break
            time.sleep(1)

        assert found, "New user did not appear on second session in real-time"

    finally:
        driver_a.quit()
        driver_b.quit()
