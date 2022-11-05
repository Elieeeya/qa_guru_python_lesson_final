import requests
import allure
import logging
import curlify
import os
import allure_commons
import pytest

import time
from selene.support.shared import browser
from selene import support
from appium import webdriver
from util.sessions import api
from selene.support.shared import browser
from dotenv import load_dotenv
from util import attach
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from resources.schemas.model_scheme import *


@pytest.fixture(scope='session', autouse=True)
def env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = os.getenv('selene.base_url', 'https://www.bmw.ru/')
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.hold_browser_open = (
            os.getenv('selene.hold_browser_open', 'false').lower() == 'true'
    )
    browser.config.timeout = float(os.getenv('selene.timeout', '3'))
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture(scope='function')
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN_WEB')
    password = os.getenv('PASSWORD_WEB')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver
    yield browser
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)


@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.config.base_url = 'https://www.bmw.ru/'
    browser.config.window_width = 1920
    browser.config.window_height = 1080


