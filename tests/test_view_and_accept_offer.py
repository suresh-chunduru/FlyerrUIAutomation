from base.basepage import BasePage
from utilities.teststatus import TestStatus
from navigation.homeNavigation import HomeNavigation
from navigation.loggedInNavigation import LoggedInNavigation
from pages.login_page import LoginPage
from pages.loggedin_page import LoggedInPage
from pages.view_offers_page import ViewOffersPage
import test_data.testData as td
import unittest
import pytest
import sys
import allure
from pytest_testrail.plugin import pytestrail

sys.path.insert(0, '../..')

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ViewOffersAndAcceptOffer(unittest.TestCase, BasePage):

    # @pytest.mark.order(1)
    @allure.story('Job Management') # epic/story of the test case
    # @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_view_the_offers_and_accept_the_offer(self):

        self.homeNavigation = HomeNavigation(self.driver)
        self.loggedInNavigation = LoggedInNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.viewOffersPage = ViewOffersPage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely", "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page", "Navigation to login page failed")

        with allure.step('Login with valid credentials'):
            self.loginPage.login(username=td.testData("loginData.requestor.username"), password=td.testData("loginData.requestor.password"))
            self.ts.markFinal(self.loggedInPage.isAt, "Login is successful", "Login failed")

        with allure.step('Navigate to my jobs page'):
            self.loggedInNavigation.goToMyJobsPage()
            self.ts.markFinal(self.viewOffersPage.isAt, "Navigation to my jobs page successful", "Navigation to my jobs page failed")

        with allure.step('Go to requestor my jobs page'):
            self.viewOffersPage.viewOffersAndSelectFirstJob()
            self.ts.markFinal(self.viewOffersPage.isAt, "requestor my jobs page loaded", "requestor my jobs page not loaded")

        with allure.step('Go to view offers page'):
            self.viewOffersPage.viewOffersAndSelectFirstOffer()
            self.ts.markFinal(self.viewOffersPage.isAt, "view offers page loaded", "view offers page not loaded")

        with allure.step('click on accept the offer'):
            self.viewOffersPage.viewOffersAndAcceptTheOffer()
            self.ts.markFinal(self.viewOffersPage.isAt, "accept the offer popup opened", "accept the offer popup not loaded")

        with allure.step('click on confirm to accept the offer'):
            self.viewOffersPage.viewOffersAndConfirmAcceptTheOffer()
            self.ts.markFinal(self.viewOffersPage.isAt, "confirm accept offer popup loaded", "confirm accept offer popup not loaded")

        with allure.step('click on ok to after accept the offer'):
            self.viewOffersPage.viewOffersAndConfirmAcceptTheOfferContinue()
            self.ts.markFinal(self.viewOffersPage.isAt, "Offer accepted successfully", "Offer acceptance failed")
