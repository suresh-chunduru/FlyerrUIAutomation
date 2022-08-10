import utilities.custom_logger as cl
import logging

import utilities.util
from base.basepage import BasePage


class AdminConfigurationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.adminPage_locators = self.pageLocators('AdminPage')
        self.countrySettings_locators = self.pageLocators('CountrySettings')

    @property
    def isAt(self):
        header_adminRole = self.getElementList(*self.locator(self.adminPage_locators, 'header_adminRole'))
        if len(header_adminRole) > 0:
            return True
        return False

    def verifyAdminPageTitle(self, expectedTitle):
        return self.verifyPageTitle(expectedTitle)

    def verifyElementDisplayed(self, element):
        return self.isElementDisplayed(*self.locator(self.adminPage_locators, element))
