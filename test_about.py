from selenium import webdriver
from selenium.webdriver.common.by import By

def test_about():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    #click on react-burger-menu-btn
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    driver.find_element(By.ID, "about_sidebar_link").click()
    assert "saucelabs.com" in driver.current_url
    driver.quit()

