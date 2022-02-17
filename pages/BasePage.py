import time

from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities import ConfigReader


class BasePage:
    def __init__(self,driver):
        self.driver = driver


    def click(self, locator_type, locator):
        self.driver.find_element(locator_type, locator).click()

# For Typing
    def type(self, locator_type, locator, value):
        self.driver.find_element(locator_type, locator).send_keys(value)

# For Keyboard Enter
    def keyboardEnter(self, locator_type, locator):
        self.driver.find_element(locator_type, locator).send_keys(Keys.ENTER)

# For wait condition
    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, ConfigReader.readConfig("basic info", "explicit.wait"))
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_until_element_is_visible(self, locator_type, locator):
        wait = WebDriverWait(self.driver, ConfigReader.readConfig("basic info", "explicit.wait"))
        element = wait.until(EC.visibility_of_element_located((locator_type, locator)))
        return element

# To highlight elements while validating
    def highlighter(self, element):
        self.driver.execute_script("arguments[0].style.border='3px solid red'", element)

# To remove highlights after validating
    def remove_highlight(self, element):
        self.driver.execute_script("arguments[0].style.border='0px solid red'", element)

