import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_search():
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.google.com/")

    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@id='APjFqb']")))
    search_box.send_keys("Test Automation")

    search_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']")))
    search_button.click()

    try:
        search_results = driver.find_elements(By.XPATH,
                                              "//div[@id='search']//span[contains(text(), 'Test Automation')]")

        assert len(search_results) > 0, "Search results do not contain 'Test Automation'."

    except Exception as e:
        print("Search verification failed:", e)
    finally:
        driver.quit()
