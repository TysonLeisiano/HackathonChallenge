import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
#@pytest.mark.test

def test_login():
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.facebook.com/")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']"))).send_keys("tysonleisiano@gmail.com")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='pass']"))).send_keys("Leisiano08!")

    login_button_element = driver.find_element(By.NAME, "login")
    login_button_element.click()

    try:
        # Wait for the welcome message or user's profile element to be visible
        welcome_message_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Welcome')]")))
        assert welcome_message_element.is_displayed(), "Welcome message not displayed; login might have failed."

        # Or check for the user's profile name or avatar as an alternative verification
        profile_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Account']")))
        assert profile_element.is_displayed(), "User profile element not displayed; login might have failed."

    except Exception as e:
        print("Login verification failed:", e)
    finally:
        # Close the browser
        driver.quit()

