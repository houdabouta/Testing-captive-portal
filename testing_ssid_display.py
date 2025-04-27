from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# List of SSIDs you want to test
ssids = ["EDU_CAMPUS", "EDU_ADMIN", "EDU_INVITE"]

# Base URL (without SSID part)
base_url = "https://VOTRE_SPLASH_PAGE_URI_ICI"

# Chrome options
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")  # Uncomment if needed

# Create driver
driver = webdriver.Chrome(options=chrome_options)

try:
    for ssid in ssids:
        # Build the complete URL by injecting SSID
        url = f"{base_url}?ssid={ssid}"
        print(f"\nTesting SSID: {ssid} -> {url}")
        driver.get(url)

        try:
            # Try to wait for 'CONNEXION WI-FI' to appear
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'CONNEXION WI-FI')]"))
            )
            print(f"'CONNEXION WI-FI' found for {ssid}")
        except TimeoutException:
            print(f"⚠️ Timeout waiting for 'CONNEXION WI-FI' on {ssid} - taking screenshot anyway.")

        # Always take a screenshot
        time.sleep(2)
        screenshot_filename = f"{ssid}_screenshot.png"
        driver.save_screenshot(screenshot_filename)
        print(f"Screenshot saved: {screenshot_filename}")

        time.sleep(1)

finally:
    time.sleep(3)
    driver.quit()