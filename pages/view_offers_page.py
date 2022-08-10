import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class ViewOffersPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.loggedInPage_locators = self.pageLocators('LoggedInPage')
        self.myJobsPage_locators = self.pageLocators('MyJobsPage')
        self.requestorMyJobsPage_locators = self.pageLocators('RequestorMyJobsPage')
        self.viewOffersPage_locators = self.pageLocators('ViewOffersPage')

    def isAt(self):
        header_my_jobs = self.getElementList(*self.locator(self.loggedInPage_locators, 'link_my_jobs'))
        if len(header_my_jobs) > 0:
            return True
        return False

    def viewOffersAndSelectFirstJob(self):
        time.sleep(5)
        self.elementClick(*self.locator(self.myJobsPage_locators, 'click_requestor_toggle'))
        time.sleep(2)
        self.elementClick(*self.locator(self.requestorMyJobsPage_locators, 'click_on_first_job'))
        time.sleep(2)

    def viewOffersAndSelectFirstOffer(self):
        self.elementClick(*self.locator(self.viewOffersPage_locators, 'click_on_view_offers_button'))
        time.sleep(2)

    def viewOffersAndAcceptTheOffer(self):
        self.elementClick(*self.locator(self.viewOffersPage_locators, 'click_on_accept_offer_button'))
        time.sleep(2)

    def viewOffersAndConfirmAcceptTheOffer(self):
        self.elementClick(*self.locator(self.viewOffersPage_locators, 'click_on_confirm_offer_accept_button'))
        time.sleep(2)

    def viewOffersAndConfirmAcceptTheOfferContinue(self):
        self.elementClick(*self.locator(self.viewOffersPage_locators, 'click_on_ok_button'))
        time.sleep(2)
