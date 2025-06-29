# ui_tests/test_responsive_design.py

import pytest
from selenium.webdriver.common.by import By
from config.selenium_config import driver

BASE_URL = "http://localhost:3000"  # Adjust based on app

# Define viewports
VIEWPORTS = [
    {"device": "Mobile", "width": 375, "height": 667},
    {"device": "Tablet", "width": 768, "height": 1024},
    {"device": "Desktop", "width": 1440, "height": 900}
]

@pytest.mark.parametrize("viewport", VIEWPORTS)
def test_responsive_user_page(driver, viewport):
    width = viewport["width"]
    height = viewport["height"]
    device = viewport["device"]

    driver.set_window_size(width, height)
    driver.get(f"{BASE_URL}/login")

    # Login
    driver.find_element(By.NAME, "email").send_keys("admin@example.com")
    driver.find_element(By.NAME, "password").send_keys("adminpassword")
    driver.find_element(By.TAG_NAME, "form").submit()

    # Open users page
    driver.find_element(By.LINK_TEXT, "Users").click()

    # Check essential elements visibility
    create_btn = driver.find_element(By.ID, "create-user-btn")
    assert create_btn.is_displayed(), f"[{device}] Create User button not visible"

    table = driver.find_element(By.TAG_NAME, "table")
    assert table.is_displayed(), f"[{device}] User table not visible"

    # Optional: Navbar behavior on mobile
    if device == "Mobile":
        burger_icon = driver.find_element(By.ID, "navbar-toggle")
        assert burger_icon.is_displayed(), "Navbar toggle not visible on mobile"
