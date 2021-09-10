# Simple assignment
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Initialize the driver and selenium wait instances
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)


def user_login(username, password):
    """
    This functions takes username and password as an argument and,
    will log in using these credentias in your instagram account and,
    then saves the screenshot of your home feed in your current directory.
    """

    # Makea get request to instagram home page
    driver.get("http://www.instagram.com")

    # Wait for the login form to load completely
    wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "KPnG0")
        )
    )

    # Select username input element in form
    user_element = driver.find_element_by_xpath("//input[@name='username']")
    # Input the username into form field
    user_element.send_keys(username)

    # Select password input element in form
    password_element = driver.find_element_by_xpath(
        "//input[@name='password']")
    # Input the password into form field
    password_element.send_keys(password)

    # Select Log In submit button element
    login_button = driver.find_element_by_xpath("//button[@type='submit']")
    # Click on the button
    login_button.click()

    # Wait for next page to load until it is asking you to save info
    wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "ABCxa")
        )
    )

    # Once the save info page opens up, simply redirect to instagram home feed page
    driver.get("http://www.instagram.com")

    # Wait for Notification window prompt from instagram
    wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "HoLwm")
        )
    )

    # Once the Notification prompt is open, just close it by clicking on Not Now button
    not_now_button = driver.find_element_by_class_name(name="HoLwm")
    # Click on now now button
    not_now_button.click()

    # Now home feed is ready, take the screenshot and save it in current directory
    driver.save_screenshot(
        filename="screenshot.png")

    # driver.close()


username = input("Input username: ")
password = input("Input password: ")

user_login(username, password)
