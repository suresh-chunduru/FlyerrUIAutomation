from base.basepage import BasePage
from utilities.teststatus import TestStatus
from navigation.homeNavigation import HomeNavigation
from navigation.loggedInNavigation import LoggedInNavigation
from pages.login_page import LoginPage
from pages.loggedin_page import LoggedInPage
from pages.submit_offer_page import SubmitOfferPage
import test_data.testData as td
import unittest
import pytest
import sys
import allure
from pytest_testrail.plugin import pytestrail

sys.path.insert(0, '../..')

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SubmitOffer(unittest.TestCase, BasePage):

    # @pytest.mark.order(1)
    @allure.story('Job Management') # epic/story of the test case
    # @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_submit_the_offer(self):

        self.homeNavigation = HomeNavigation(self.driver)
        self.loggedInNavigation = LoggedInNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.submitOfferPage = SubmitOfferPage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely", "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page", "Navigation to login page failed")

        with allure.step('Login with valid credentials'):
            self.loginPage.login(username=td.testData("loginData.flyer.username"), password=td.testData("loginData.flyer.password"))
            self.ts.markFinal(self.loggedInPage.isAt, "Login is successful", "Login failed")

        with allure.step('Navigate to find jobs page'):
            self.loggedInNavigation.goToFindJobsPage()
            self.ts.markFinal(self.submitOfferPage.isAt, "Navigation to find jobs page successful", "Navigation to find jobs page failed")

        with allure.step('Fill required details to submit the offer'):
            self.submitOfferPage.submitOfferWithMilestones_FillDetails(offerBudget=td.testData("SubmitOfferData.offer_budget"),
                                                   firstMilestoneTitle=td.testData("SubmitOfferData.first_milestone_title"),
                                                   firstMilestoneBudget=td.testData("SubmitOfferData.first_milestone_budget"),
                                                   firstMilestoneDesc=td.testData("SubmitOfferData.first_milestone_desc"),
                                                   offerDesc=td.testData("SubmitOfferData.offer_desc"))
            self.ts.markFinal(self.submitOfferPage.isAt, "Offer details filled", "Offer details filled is failed")

        with allure.step('Click on continue to submit the offer'):
            self.submitOfferPage.submitOfferWithMilestones_clickContinue()
            self.ts.markFinal(self.submitOfferPage.isAt, "Navigate to find more jobs page", "Navigate to find more jobs page failed")

        with allure.step('Click on find more jobs'):
                self.submitOfferPage.submitOfferWithMilestones_clickFindmorejobs()
                self.ts.markFinal(self.submitOfferPage.isAt, "Submit the offer is successful",
                                  "Submit the offer is failed")