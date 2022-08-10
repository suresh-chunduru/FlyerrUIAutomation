import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class AdminNavigation(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.adminPage_locators = self.pageLocators('AdminPage')
        self.countrySettings_locators = self.pageLocators('CountrySettings')

    def goToCountrySettings(self):
        self.elementClick(*self.locator(self.adminPage_locators, 'link_countrySettings'))

    def goToAccount(self):
        self.elementClick(*self.locator(self.adminPage_locators, 'link_account'))

    def goToProfile(self):
        self.elementClick(*self.locator(self.adminPage_locators, 'link_profile'))