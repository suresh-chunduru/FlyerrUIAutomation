import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class CountrySettingsNavigation(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.countrySettings_locators = self.pageLocators('CountrySettings')

    def goToLastPage(self):
        time.sleep(1)
        self.elementClick(*self.locator(self.countrySettings_locators, 'btn_pageRangeActionLastPage'))
        time.sleep(1)

    def goToFirstPage(self):
        time.sleep(1)
        self.elementClick(*self.locator(self.countrySettings_locators, 'btn_pageRangeActionFirstPage'))
        time.sleep(1)

    def goToNextPage(self):
        time.sleep(1)
        self.elementClick(*self.locator(self.countrySettings_locators, 'btn_pageRangeActionNextPage'))
        time.sleep(1)

    def goToPreviousPage(self):
        time.sleep(1)
        self.elementClick(*self.locator(self.countrySettings_locators, 'btn_pageRangeActionPreviousPage'))
        time.sleep(1)