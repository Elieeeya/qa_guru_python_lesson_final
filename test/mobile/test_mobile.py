import allure
import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser
from model.pages.vkusvill_page import MainPageVkusvill
import allure_commons
import time
from selene.support.shared import browser
from selene import support
from appium import webdriver
import config



@pytest.fixture(scope='function', autouse=True)
def create_driver():
    browser.config.timeout = config.settings.timeout
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    browser.config.driver = webdriver.Remote(
        config.settings.remote_url, options=config.settings.driver_options
    )

    return browser


@pytest.mark.mobile
@allure.description('Swipe list')
def test_swipe_menu():
    with allure.step('Свайп разделов'):
        MainPageVkusvill().swipe_menu()



@pytest.mark.mobile
@allure.description('loacation')
def test_loacation():
    with allure.step('Определение локации'):
        MainPageVkusvill().loacation()


@pytest.mark.mobile
@allure.description('Delete catalog')
def test_delete():
    with allure.step('Меню удаления'):
        MainPageVkusvill().delete()


@pytest.mark.mobile
@allure.description('Check contacts')
def test_contacts():
    with allure.step('Просмотр контактов'):
        MainPageVkusvill().contacts()


@pytest.mark.mobile
@allure.description('Loyalty program')
def test_loyalty_program():
    with allure.step('Путешествие по карте лояльности'):
        MainPageVkusvill().loyalty_program()