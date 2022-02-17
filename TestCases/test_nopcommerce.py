import time

import allure
import pytest
from allure_commons.types import AttachmentType

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from Utilities import DataProvider
from Utilities.Logger_utils import Logger


class TestNopCommerce: # Class name should start or end with Test

# Use this function to keep all object creation in common place
    @pytest.fixture(autouse=True) # To use it in all test functions
    def objects_function(self):
        self.log = Logger.custom_logger() # Object for logger
        self.lp = LoginPage(self.driver)

# Call this @pytest.mark.usefixtures("log_on_failure") to add screenshot to allure reports when there is a failure
    @pytest.mark.usefixtures("log_on_failure")
# Call this fixture for data driver testing @pytest.mark.parametrize, here it assigns values to variables from excel
    @pytest.mark.parametrize("username, password", DataProvider.get_data("../TestData/nop_testdata.xlsx","Sheet1"))
    def test_login(self, username, password):
        self.log.info("Inside Test")
        dashboard_reference = self.lp.do_login(username, password)  # Creating object for chaining function
        # allure.attach(self.driver.get_screenshot_as_png(),name="Login", attachment_type=AttachmentType.PNG)
        self.log.info("Completed successfully")
        dashboard_reference.validate_dashboard_title("New")  # Calling dashboard_page function validate_dashboard_title()
        dashboard_reference.click_logout_button()  # Calling dashboard_page function click_logout_button()
