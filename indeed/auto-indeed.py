from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Function to check if logged in
def is_logged_in(driver):
    try:
        # Check if there's an element unique to the logged-in state
        driver.find_element(By.XPATH,"//a[@class='gnav-LoggedOutAccountLink-text']")
        return False
    except:
        return True

# Function to login
def login(driver, username, password):
    # Navigate to the login page
    driver.get("https://secure.indeed.com/account/login?hl=en_AU&co=AU&continue=https%3A%2F%2Fau.indeed.com%2F")
    time.sleep(2)  # Wait for the page to load

    # Find the username and password fields and input the credentials
    username_field = driver.find_element(By.ID,"signin_email")
    username_field.send_keys(username)

    password_field = driver.find_element(By.ID,"signin_password")
    password_field.send_keys(password)

    # Submit the form
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for the login process to complete

# Main function
def main():
    # Initialize the WebDriver (make sure you have the appropriate driver for your browser installed)
    driver = webdriver.Chrome()  # Change to appropriate driver if using a different browser

    # Enter your Indeed credentials
    username = "achaulagain123@gmail.com"
    password = "Amit@rew3"

    # Check if already logged in
    if not is_logged_in(driver):
        login(driver, username, password)

    # Now you can proceed with whatever you want to do on Indeed after logging in

    # Remember to close the WebDriver when done
    driver.quit()

if __name__ == "__main__":
    main()
