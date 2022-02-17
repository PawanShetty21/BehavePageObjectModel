
import time

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from Utilities.Logger_utils import Logger


class DashboardPage(BasePage):
    log = Logger.custom_logger()

    def __init__(self, driver):
        self.driver = driver

    # Locators
    DASHBOARD_TITLE_XPATH = "//h1[normalize-space()='Dashboard']"
    LOGOUT_BUTTON_XPATH = "//a[text()='Logout']"

    # Locator return functions
    def get_dashboard_title(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DASHBOARD_TITLE_XPATH)

    def get_logout_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.LOGOUT_BUTTON_XPATH)

    # Operating functions
    def validate_dashboard_title(self, title):
        print("Text is new: ", self.get_dashboard_title().text)

        try:
            assert title == self.get_dashboard_title().text, "Title not matching"
        except:
            # self.driver.execute_script("arguments[0].style.border='3px solid red'", self.get_dashboard_title())
            self.highlighter(self.get_dashboard_title())
            assert False,"Failing the test as Title not matching"
        self.remove_highlight(self.get_dashboard_title())
        time.sleep(5)



    def click_logout_button(self):
        self.get_logout_button().click()
        self.log.info("Clicked on logout button")


    # Main functions
