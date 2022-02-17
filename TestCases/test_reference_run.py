from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test_NopCommerece:

    def test_verify_nopcommerece(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)

        driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2FAdmin")
        driver.maximize_window()

        username = driver.find_element(By.ID, "Email")
        username.clear()
        username.send_keys("admin@yourstore.com")

        password = driver.find_element(By.ID, "Password")
        password.clear()
        password.send_keys("admin")

        loginButton = driver.find_element(By.XPATH, "//button[@type='submit']")
        loginButton.click()

        # logoutButton = driver.find_element(By.LINK_TEXT, "Logout")
        # logoutButton.click()

        TITLE_TEXT_XPATH = driver.find_element(By.XPATH, "//h1[normalize-space()='Dashboard']").text
        if TITLE_TEXT_XPATH == "Dashboard":
            print("Valid title")
        else:
            print("Title is not matching")

        driver.close()
