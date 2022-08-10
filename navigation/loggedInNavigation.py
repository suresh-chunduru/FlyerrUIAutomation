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
        self.myJobsPage_locators = self.pageLocators('MyJobsPage')

    def goToProfilePage(self):
        time.sleep(2)
        self.elementClick(*self.locator(self.loggedInPage_locators, 'btn_hiMenu'))
        time.sleep(2)
        self.elementClick(*self.locator(self.loggedInPage_locators, 'btn_menuProfile'))
        time.sleep(5)
        self.page_has_loaded()

    def goToPostJobRequestPage(self):
        time.sleep(2)
        self.elementClick(*self.locator(self.loggedInPage_locators, 'link_post_a_request'))
        self.page_has_loaded()

    def goToMyJobsPage(self):
        time.sleep(2)
        self.elementClick(*self.locator(self.loggedInPage_locators, 'link_my_jobs'))
        time.sleep(2)
        self.page_has_loaded()

    def goToFindJobsPage(self):
        time.sleep(2)
        self.elementClick(*self.locator(self.loggedInPage_locators, 'link_find_jobs'))
        time.sleep(2)
        self.page_has_loaded()
