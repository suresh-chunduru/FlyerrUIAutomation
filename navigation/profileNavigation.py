import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class ProfileNavigation(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.profilePage_locators = self.pageLocators('ProfilePage')

    def goToOverviewPage(self):
        time.sleep(2)
        self.elementClick(*self.locator(self.profilePage_locators, 'tab_overview'))
        time.sleep(2)

    def goToProfilePage(self):
        time.sleep(2)
        self.elementClick(*self.locator(self.profilePage_locators, 'tab_profile'))
        time.sleep(2)

    def goToInboxPage(self):
        time.sleep(2)
        self.elementClick(*self.locator(self.profilePage_locators, 'tab_inbox'))
        time.sleep(2)

    def goToPaymentPage(self):
        time.sleep(2)
        self.elementClick(*self.locator(self.profilePage_locators, 'tab_payment'))
        time.sleep(2)

    def goToAccountPage(self):
        time.sleep(2)
        self.elementClick(*self.locator(self.profilePage_locators, 'tab_account'))
        time.sleep(2)

    def goToEditProfile(self):
        time.sleep(2)
        self.elementClick(*self.locator(self.profilePage_locators, 'btn_addOrEditProfile'))
        time.sleep(2)

    def goToEditServiceLocation(self):
        time.sleep(2)
        self.elementClick(*self.locator(self.profilePage_locators, 'btn_addOrEditServiceLocation'))

    def goToEditSkills(self):
        time.sleep(2)
        self.elementClick(*self.locator(self.profilePage_locators, 'btn_addOrEditSkills'))
        time.sleep(2)

    def goToEditServices(self):
        time.sleep(2)
        self.elementClick(*self.locator(self.profilePage_locators, 'btn_addOrEditServices'))
        time.sleep(2)

    def goToEditListingsAndPackages(self):
        time.sleep(2)
        self.elementClick(*self.locator(self.profilePage_locators, 'btn_addOrEditListingsAndPackages'))
        time.sleep(2)