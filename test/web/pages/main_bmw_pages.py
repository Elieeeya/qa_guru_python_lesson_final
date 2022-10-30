import time

from selene import have
from selene.support.shared import browser


class MainPage:

    def click_link(self):
        browser.element('[title="Автомобили"]').click()
        time.sleep(1)
        browser.element('[title="Покупка"]').click()
        time.sleep(1)
        browser.element('[title="Владельцам"]').click()
        time.sleep(1)
        browser.element('[title="BMW Россия"]').click()
        time.sleep(1)

    def bmw_search(self):
        browser.element('[id="id-search_desktop"]').click()
        browser.element('[name="search"]').send_keys('вакансия').press_enter()
        browser.element('[class="aems-sr-results"]').should(
            have.text('Вакансии - Карьера в компании BMW Group Россия | BMW'))
        browser.element('//a[text()=" - Карьера в компании BMW Group Россия | BMW"]').click()
        browser.element('[class="main "]').should(
            have.text('BMW Group Russia'))

    def bmw_models(self):
        browser.element('[title="configurator"]').click()
        browser.element('[title="BMW M3 Competition"]').click()

    def bmw_kodix(self):
        browser.element('[title="BMW с пробегом"]').click()
        browser.element('[class="main-footer"]').should(
            have.text('Kodix Automotive'))


    def bmw_check_all_models(self):
        browser.element('[title="Автомобили"]').click()
        browser.element('[data-series="X"]').click()
        time.sleep(1)
        browser.element('[data-series="M"]').click()
        time.sleep(1)
        browser.element('[data-series="8"]').click()
        time.sleep(1)
        browser.element('[data-series="7"]').click()
        time.sleep(1)
        browser.element('[data-series="6"]').click()
        time.sleep(1)
        browser.element('[data-series="5"]').click()
        time.sleep(1)
        browser.element('[data-series="4"]').click()
        time.sleep(1)
        browser.element('[data-series="3"]').click()
        time.sleep(1)
        browser.element('[data-series="2"]').click()
        time.sleep(1)
        browser.element('[data-series="Z"]').click()
        time.sleep(1)
        browser.element('[data-series="BMW Концепты"]').click()



