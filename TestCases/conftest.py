import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Utilities import ConfigReader


# To check for failures in the tests
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


# To take screenshot of failed test cases
@pytest.fixture()
def log_on_failure(request, setup):
    yield
    item = request.node
    driver = setup
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@pytest.fixture(scope="class", autouse=True)
def setup(request):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get(ConfigReader.readConfig("basic info", "testURL"))  # To pass url from Config using ConfigReader
    driver.maximize_window()

    # request.cls.driver = driver  - This says driver reference is available at the class level of the requesting class
    # here calling class is TestNopCommerce()
    request.cls.driver = driver
    yield driver
    driver.close()
