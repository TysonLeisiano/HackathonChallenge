from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_user_profile_update():
    # Desired capabilities for the Appium session
    desired_caps = {
        "platformName": "Android",
        "deviceName": "Android Emulator",  # Or the name of your real device
        "appPackage": "com.example.yourapp",  # Replace with your app's package
        "appActivity": "com.example.yourapp.MainActivity",  # Replace with your app's main activity
        "automationName": "UiAutomator2"
    }

    # Initialize the Appium driver
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    wait = WebDriverWait(driver, 10)

    try:
        # Log in to the application
        username_field = wait.until(EC.presence_of_element_located((By.ID, "com.example.yourapp:id/username")))
        username_field.send_keys("testuser")

        password_field = driver.find_element(By.ID, "com.example.yourapp:id/password")
        password_field.send_keys("password123")

        login_button = driver.find_element(By.ID, "com.example.yourapp:id/login")
        login_button.click()

        # Navigate to the settings page
        settings_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@content-desc='Settings']")))
        settings_button.click()

        # Update user profile (e.g., change the username)
        profile_field = wait.until(EC.presence_of_element_located((By.ID, "com.example.yourapp:id/profile_name")))
        profile_field.clear()
        profile_field.send_keys("new_testuser")

        save_button = driver.find_element(By.ID, "com.example.yourapp:id/save_profile")
        save_button.click()

        # Confirm the profile update was successful
        updated_profile_name = wait.until(
            EC.presence_of_element_located((By.ID, "com.example.yourapp:id/profile_name_display")))
        assert updated_profile_name.text == "new_testuser", "Profile update failed!"

        print("Profile updated successfully!")

    finally:
        # Quit the driver to close the session
        driver.quit()


# To run the test, simply call the function
if __name__ == "__main__":
    test_user_profile_update()
