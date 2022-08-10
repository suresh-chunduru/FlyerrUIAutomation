import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class PostJobRequestPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.postJobRequestPage_locators = self.pageLocators('PostJobRequestPage')
        self.loggedInPage_locators = self.pageLocators('LoggedInPage')

    def isAt(self):
        header_post_a_request = self.getElementList(*self.locator(self.loggedInPage_locators, 'link_post_a_request'))
        if len(header_post_a_request) > 0:
            return True
        return False

    def postRemoteJobRequestFlexibleDate_DescribeJobPage(self, serviceCategory, setBudget):
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'input_service_category'))
        time.sleep(2)
        self.sendKeys(serviceCategory, *self.locator(self.postJobRequestPage_locators, 'input_service_category'))
        time.sleep(2)
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'service_category_list'))
        time.sleep(2)
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'location_remote'))
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'date_flexible'))
        self.sendKeys(setBudget, *self.locator(self.postJobRequestPage_locators, 'input_set_budget'))
        time.sleep(2)
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'select_mile_stone_yes'))
        time.sleep(2)
    def postRemoteJobRequestFlexibleDate_GiveDetailsPage(self, setJobTitle, setJobDesc):
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'button_describe_job_continue'))
        self.sendKeys(setJobTitle, *self.locator(self.postJobRequestPage_locators, 'input_job_title'))
        self.sendKeys(setJobDesc, *self.locator(self.postJobRequestPage_locators, 'input_job_description'))
        time.sleep(2)
    def postRemoteJobRequestFlexibleDate_FindFlyersPage(self):
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'button_give_details_continue'))
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'invite_flyers'))
        time.sleep(2)
    def postRemoteJobRequestFlexibleDate_JobCreatedSuccessfully(self):
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'button_find_flyerrs_continue'))
        time.sleep(2)




    def postRemoteJobRequestPreferredDate_DescribeJobPage(self, serviceCategory, setBudget):
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'input_service_category'))
        time.sleep(2)
        self.sendKeys(serviceCategory, *self.locator(self.postJobRequestPage_locators, 'input_service_category'))
        time.sleep(2)
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'service_category_list'))
        time.sleep(2)
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'location_remote'))
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'date_preferred'))
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'date_calender_icon'))
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'date_select_next_month'))
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'date_select_day'))
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'time_select_dropdown'))
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'time_select'))
        self.sendKeys(setBudget, *self.locator(self.postJobRequestPage_locators, 'input_set_budget'))
        time.sleep(2)
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'select_mile_stone_yes'))
        time.sleep(2)
    def postRemoteJobRequestPreferredDate_GiveDetailsPage(self, setJobTitle, setJobDesc):
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'button_describe_job_continue'))
        self.sendKeys(setJobTitle, *self.locator(self.postJobRequestPage_locators, 'input_job_title'))
        self.sendKeys(setJobDesc, *self.locator(self.postJobRequestPage_locators, 'input_job_description'))
        time.sleep(2)
    def postRemoteJobRequestPreferredDate_FindFlyersPage(self):
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'button_give_details_continue'))
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'invite_flyers'))
        time.sleep(2)
    def postRemoteJobRequestPreferredDate_JobCreatedSuccessfully(self):
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'button_find_flyerrs_continue'))
        time.sleep(2)



    def postRemoteJobRequestChooseFlyers_DescribeJobPage(self, serviceCategory, setBudget):
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'input_service_category'))
        time.sleep(2)
        self.sendKeys(serviceCategory, *self.locator(self.postJobRequestPage_locators, 'input_service_category'))
        time.sleep(2)
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'service_category_list'))
        time.sleep(2)
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'location_remote'))
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'date_flexible'))
        self.sendKeys(setBudget, *self.locator(self.postJobRequestPage_locators, 'input_set_budget'))
        time.sleep(2)
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'select_mile_stone_yes'))
        time.sleep(2)
    def postRemoteJobRequestChooseFlyers_GiveDetailsPage(self, setJobTitle, setJobDesc):
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'button_describe_job_continue'))
        self.sendKeys(setJobTitle, *self.locator(self.postJobRequestPage_locators, 'input_job_title'))
        self.sendKeys(setJobDesc, *self.locator(self.postJobRequestPage_locators, 'input_job_description'))
        time.sleep(2)
    def postRemoteJobRequestChooseFlyers_FindFlyersPage(self):
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'button_give_details_continue'))
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'choose_flyers'))
        time.sleep(3)
    def postRemoteJobRequestChooseFlyers_JobCreated(self):
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'button_find_flyerrs_continue'))
        time.sleep(4)
    def postRemoteJobRequestChooseFlyers_SelectFlyers(self):
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'choose_specific_flyer_1'))
        time.sleep(2)
        self.elementClick(*self.locator(self.postJobRequestPage_locators, 'choose_specific_flyer_2'))
        time.sleep(2)



