import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="fucntion")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1440x90")  # Set window

    driver = webdriver.Chrome(options=chrome_options) # Initialize the Chrome driver
    yield driver # This is where the test will run
    driver.quit()  # Cleanup after the test is done

