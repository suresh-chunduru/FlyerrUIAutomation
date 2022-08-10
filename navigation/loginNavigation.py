import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class LoginNavigation(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.loginPage_locators = self.pageLocators('LoginPage')

    def goToSignUpPage(self):
        time.sleep(2)
        self.elementClick(*self.locator(self.loginPage_locators, 'link_signUp'))
        self.page_has_loaded()
