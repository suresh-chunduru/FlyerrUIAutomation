import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class SubmitOfferPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.submitOfferPage_locators = self.pageLocators('SubmitOfferPage')
        self.findJobsPage_locators = self.pageLocators('FindJobsPage')
        self.loggedInPage_locators = self.pageLocators('LoggedInPage')

    def isAt(self):
        header_find_jobs = self.getElementList(*self.locator(self.loggedInPage_locators, 'link_find_jobs'))
        if len(header_find_jobs) > 0:
            return True
        return False

    def submitOfferWithMilestones_FillDetails(self, offerBudget, firstMilestoneTitle, firstMilestoneBudget, firstMilestoneDesc, offerDesc):
        self.elementClick(*self.locator(self.findJobsPage_locators, 'click_on_first_job'))
        time.sleep(2)
        self.elementClick(*self.locator(self.submitOfferPage_locators, 'click_on_submit_offer_button'))
        time.sleep(2)
        self.sendKeys(offerBudget, *self.locator(self.submitOfferPage_locators, 'input_offer_budget'))
        time.sleep(2)
        self.elementClick(*self.locator(self.submitOfferPage_locators, 'date_calender_icon'))
        time.sleep(2)
        self.elementClick(*self.locator(self.submitOfferPage_locators, 'date_select_next_month'))
        time.sleep(2)
        self.elementClick(*self.locator(self.submitOfferPage_locators, 'date_select_day'))
        time.sleep(2)
        self.elementClick(*self.locator(self.submitOfferPage_locators, 'select_mile_stone_checkbox'))
        time.sleep(2)
        self.elementClick(*self.locator(self.submitOfferPage_locators, 'click_add_milestone_button'))
        time.sleep(2)
        self.sendKeys(firstMilestoneTitle, *self.locator(self.submitOfferPage_locators, 'input_first_milestone'))
        time.sleep(2)
        self.sendKeys(firstMilestoneBudget, *self.locator(self.submitOfferPage_locators, 'input_first_milestone_budget'))
        time.sleep(2)
        self.sendKeys(firstMilestoneDesc, *self.locator(self.submitOfferPage_locators, 'input_first_milestone_desc'))
        time.sleep(2)
        self.sendKeys(offerDesc, *self.locator(self.submitOfferPage_locators, 'input_offer_desc'))
        time.sleep(2)

    def submitOfferWithMilestones_clickContinue(self):
        self.elementClick(*self.locator(self.submitOfferPage_locators, 'click_on_submit_offer_button_in_form'))
        time.sleep(2)

    def submitOfferWithMilestones_clickFindmorejobs(self):
        self.elementClick(*self.locator(self.submitOfferPage_locators, 'click_find_more_jobs'))
        time.sleep(2)