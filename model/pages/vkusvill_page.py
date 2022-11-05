import time

from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait

from util.attach import add_mob_video
from test.conftest import *


class MainPageVkusvill:

    def swipe_menu(self):
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/btn_enter')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/bottom_item_profile')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/bottom_item_catalog')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/bottom_item_history')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/bottom_item_support')).click()
        add_mob_video(browser)
        browser.quit()


    def loacation(self):
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/btn_enter')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/bottom_item_catalog')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/button_service_not')).click()
        browser.element(
            (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/tv_address')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/search')).send_keys('Moscow, Prospekt Mira, 95с1')
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/rl_root')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/btn_select')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/button_rules_ok')).click()
        add_mob_video(browser)
        browser.quit()



    def delete(self):
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/btn_enter')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/bottom_item_profile')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/btn')).click()
        browser.element(
            (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')).click()
        time.sleep(2)
        add_mob_video(browser)
        browser.quit()



    def contacts(self):
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/btn_enter')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/bottom_item_support')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/tv_contact_call')).click()
        add_mob_video(browser)
        browser.quit()

    def loyalty_program(self):
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/btn_enter')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/bottom_item_support')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/sl')).click()
        time.sleep(2)
        add_mob_video(browser)
        browser.quit()




