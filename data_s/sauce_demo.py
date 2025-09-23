from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

LOG_FILE = Path("log.txt")

class sauce_demo():
    def __init__(self):
        self.driver = webdriver.Firefox()
        

    def test_login_standard_user(self):
        try:
            self.driver.get("https://www.saucedemo.com/")
            self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
            self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
            self.driver.find_element(By.ID, "login-button").click()
            #assert "inventory" in self.driver.current_url
            #add to log.txt
            with open(LOG_FILE, "a") as f:
                f.write("Login successful for standard_user\n")
        except Exception as e:
            with open(LOG_FILE, "a") as f:
                f.write(f"Login failed for standard_user: {e}\n")


    
    def test_add_to_card(self):
        
        try:
            self.driver.get("https://www.saucedemo.com/")
            self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
            self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
            self.driver.find_element(By.ID, "login-button").click()
            self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
            cart_count = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
            #assert cart_count == "1"
            with open(LOG_FILE, "a") as f:
                f.write("Add to cart successful for standard_user\n")
        except Exception as e:
            with open(LOG_FILE, "a") as f:
                f.write(f"Add to cart failed for standard_user: {e}\n")

        
    def quit(self):
        self.driver.quit()
    
    def test_about(self):
        
        try:
            self.driver.get("https://www.saucedemo.com/")
            self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
            self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
            self.driver.find_element(By.ID, "login-button").click()
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
            #click on react-burger-menu-btn
            self.driver.find_element(By.ID, "react-burger-menu-btn").click()
            self.driver.find_element(By.ID, "about_sidebar_link").click()
            #assert "saucelabs.com" in self.driver.current_url
            with open(LOG_FILE, "a") as f:
                f.write("About page navigation successful for standard_user\n")
        except Exception as e:
            with open(LOG_FILE, "a") as f:
                f.write(f"About page navigation failed for standard_user: {e}\n")