import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def automate_message():
    # Setup the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Open the website
    driver.get("https://www.instagram.com")

    try:
        # Explicitly wait for the username field and enter the username
        username_input = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "username")))
        username_input.send_keys("ogjahishes")

        # Explicitly wait for the password field and enter the password
        password_input = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "password")))
        password_input.send_keys("moralesballs")
        
        # Optional: Add a strategic wait here to ensure all fields are ready
        time.sleep(2)  # Wait for 2 seconds before clicking the login button

        # Check if the login button is enabled and clickable, then click it
        login_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']:not([disabled])")))
        login_button.click()

        # Ensure the page has loaded and you are logged in
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search']")))

        try:
            # Handle the "Not Now" button if it appears
            not_now_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']")))
            not_now_button.click()
        except Exception as e:
            print("Notification prompt did not appear or could not be closed:", e)

        # Navigate to the specific direct message page
        driver.get("https://www.instagram.com/direct/t/108557950540780/")
        
        # Wait for the message input box to be clickable and send a message
        spam = 0
        while True:
            message_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p")))
            if spam % 2 == 0:
                message_input.send_keys("https://www.instagram.com/p/C5aaN8tA-Vy/")
            else:
                message_input.send_keys("https://www.instagram.com/p/CoExxEWuXDM/")
            
            # Wait for the send button and click it
            send_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]")))
            send_button.click()

            spam = spam + 1
            time.sleep(.5)

    finally:
        # Wait for a while before closing so you can see what happened
        input("Press Enter to close the browser...")
        driver.quit()

automate_message()
