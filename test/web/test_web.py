from test.conftest import *
from model.pages.bmw_pages import MainPage


@pytest.mark.web
@allure.description('Click link')
def test_bmw_link(setup_browser):
    browser = setup_browser
    browser.open('ru/all-models')
    with allure.step('Просмотр всех вкладок'):
        MainPage().click_link()


@pytest.mark.web
@allure.description('Use search')
def test_bmw_search(setup_browser):
    browser = setup_browser
    browser.open('ru/all-models')
    with allure.step('Поиск вакансии'):
        MainPage().bmw_search()


@pytest.mark.web
@allure.description('Check models')
def test_bmw_models(setup_browser):
    browser = setup_browser
    browser.open('ru/index.html')
    with allure.step('Поиск модели BMW M3'):
        MainPage().bmw_models()


@pytest.mark.web
@allure.description('Serch Kodix')
def test_bmw_kodix(setup_browser):
    browser = setup_browser
    browser.open('ru/all-models')
    with allure.step('Поиск компании Кодикс'):
        MainPage().bmw_kodix()


@pytest.mark.web
@allure.description('Check location')
def test_bmw_check_all_models(setup_browser):
    browser = setup_browser
    browser.open('ru/index.html')
    with allure.step('Просмотр всех моделй'):
        MainPage().bmw_check_all_models()
