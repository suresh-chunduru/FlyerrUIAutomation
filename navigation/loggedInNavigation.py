import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class LoggedInNavigation(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.loggedInPage_locators = self.pageLocators('LoggedInPage')

    def goToProfilePage(self):
        time.sleep(2)
        self.elementClick(*self.locator(self.loggedInPage_locators, 'btn_hiMenu'))
        time.sleep(2)
        self.elementClick(*self.locator(self.loggedInPage_locators, 'btn_menuProfile'))
        time.sleep(5)
        self.page_has_loaded()
