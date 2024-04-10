import pytest
import allure
from dotenv import load_dotenv

from utils import attach
from appium import webdriver
from selene import browser
from config import config_app


def pytest_addoption(parser):
    parser.addoption("--context", action="store", default="bstack",
                     help="Context for load options")


@pytest.fixture(scope='function', autouse=True)
def mobile_management(request):
    context = request.config.getoption('--context')
    with allure.step('Set options'):
        options = config_app.to_driver_options(test_context=context)
        browser.config.driver = webdriver.Remote(config_app.REMOTE_URL, options=options)
        browser.config.timeout = config_app.TIMEOUT

    yield

    with allure.step('Add screenshot'):
        attach.add_screenshot(browser)

    if context == 'bstack':
        with allure.step('Add video'):
            attach.add_video(browser)

    with allure.step('Close driver'):
        browser.config.driver.quit()
