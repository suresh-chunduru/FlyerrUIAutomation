import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class HomeNavigation(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.homePage_locators = self.pageLocators('HomePage')

    def goToLoginPage(self):
        time.sleep(2)
        self.elementClick(*self.locator(self.homePage_locators, 'link_login'))
        self.page_has_loaded()
