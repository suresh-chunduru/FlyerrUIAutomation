from base.basepage import BasePage
from utilities.teststatus import TestStatus
from navigation.homeNavigation import HomeNavigation
from navigation.loggedInNavigation import LoggedInNavigation
from navigation.marketPlaceNavigation import MarketPlaceNavigation
from pages.login_page import LoginPage
from pages.loggedin_page import LoggedInPage
from pages.post_job_request_page import PostJobRequestPage
import test_data.testData as td
import unittest
import pytest
import sys
import allure
from pytest_testrail.plugin import pytestrail

sys.path.insert(0, '../..')

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class PostJobRequest(unittest.TestCase, BasePage):

    # @pytest.mark.order(1)
    @allure.story('Job Management') # epic/story of the test case
    # @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_post_a_remote_job_request_with_flexible_date(self):

        self.homeNavigation = HomeNavigation(self.driver)
        self.loggedInNavigation = LoggedInNavigation(self.driver)
        self.marketPlaceNavigation = MarketPlaceNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.postJobRequestPage = PostJobRequestPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely", "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page successful", "Navigation to login page failed")

        with allure.step('Login with valid credentials'):
            self.loginPage.login(username=td.testData("loginData.requestor.username"), password=td.testData("loginData.requestor.password"))
            self.ts.markFinal(self.loggedInPage.isAt, "Login is successful", "Login failed")

        with allure.step('Navigate to Post Job Request page'):
            self.loggedInNavigation.goToPostJobRequestPage()
            self.ts.markFinal(self.postJobRequestPage.isAt, "Navigation to post job request page successful", "Navigation to post job request page failed")

        with allure.step('Fill required details in describe your job page'):
            self.postJobRequestPage.postRemoteJobRequestFlexibleDate_DescribeJobPage(serviceCategory=td.testData("PostJobRequestData.service_category"),
                                                   setBudget=td.testData("PostJobRequestData.budget"))
            self.ts.markFinal(self.postJobRequestPage.isAt, "Describe your job", "Post Job Request failed")

        with allure.step('Fill required details in give details page'):
            self.postJobRequestPage.postRemoteJobRequestFlexibleDate_GiveDetailsPage(setJobTitle=td.testData("PostJobRequestData.job_title"),
                                                   setJobDesc=td.testData("PostJobRequestData.job_desc"))
            self.ts.markFinal(self.postJobRequestPage.isAt, "Give details", "Post Job Request failed")

        with allure.step('Choose flyers in find flyers page'):
            self.postJobRequestPage.postRemoteJobRequestFlexibleDate_FindFlyersPage()
            self.ts.markFinal(self.postJobRequestPage.isAt, "Choose flyers", "Post Job Request failed")

        with allure.step('Job Created successfully'):
            self.postJobRequestPage.postRemoteJobRequestFlexibleDate_JobCreatedSuccessfully()
            self.ts.markFinal(self.postJobRequestPage.isAt, "Job created successfully", "Post Job Request failed")



    # @pytest.mark.order(1)
    @allure.story('Job Management')  # epic/story of the test case
    # @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_post_a_remote_job_request_with_preferred_date(self):

        self.homeNavigation = HomeNavigation(self.driver)
        self.loggedInNavigation = LoggedInNavigation(self.driver)
        self.marketPlaceNavigation = MarketPlaceNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.postJobRequestPage = PostJobRequestPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely", "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page successful", "Navigation to login page failed")

        with allure.step('Login with valid credentials'):
            self.loginPage.login(username=td.testData("loginData.requestor.username"), password=td.testData("loginData.requestor.password"))
            self.ts.markFinal(self.loggedInPage.isAt, "Login is successful", "Login failed")

        with allure.step('Navigate to Post Job Request page'):
            self.loggedInNavigation.goToPostJobRequestPage()
            self.ts.markFinal(self.postJobRequestPage.isAt, "Navigation to post job request page successful", "Navigation to post job request page failed")

        with allure.step('Fill required details in describe your job page'):
            self.postJobRequestPage.postRemoteJobRequestPreferredDate_DescribeJobPage(serviceCategory=td.testData("PostJobRequestData.service_category"),
                                                   setBudget=td.testData("PostJobRequestData.budget"))
            self.ts.markFinal(self.postJobRequestPage.isAt, "Describe your job", "Post Job Request failed")

        with allure.step('Fill required details in give details page'):
            self.postJobRequestPage.postRemoteJobRequestPreferredDate_GiveDetailsPage(setJobTitle=td.testData("PostJobRequestData.job_title"),
                                                   setJobDesc=td.testData("PostJobRequestData.job_desc"))
            self.ts.markFinal(self.postJobRequestPage.isAt, "Give details", "Post Job Request failed")

        with allure.step('Choose flyers in find flyers page'):
            self.postJobRequestPage.postRemoteJobRequestPreferredDate_FindFlyersPage()
            self.ts.markFinal(self.postJobRequestPage.isAt, "Choose flyers", "Post Job Request failed")

        with allure.step('Job Created successfully'):
            self.postJobRequestPage.postRemoteJobRequestPreferredDate_JobCreatedSuccessfully()
            self.ts.markFinal(self.postJobRequestPage.isAt, "Job created successfully", "Post Job Request failed")




    # @pytest.mark.order(1)
    @allure.story('Job Management')  # epic/story of the test case
    # @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_post_a_remote_job_request_and_choose_flyers(self):

        self.homeNavigation = HomeNavigation(self.driver)
        self.loggedInNavigation = LoggedInNavigation(self.driver)
        self.marketPlaceNavigation = MarketPlaceNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.postJobRequestPage = PostJobRequestPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely", "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page successful", "Navigation to login page failed")

        with allure.step('Login with valid credentials'):
            self.loginPage.login(username=td.testData("loginData.business.username"), password=td.testData("loginData.business.password"))
            self.ts.markFinal(self.loggedInPage.isAt, "Login is successful", "Login failed")

        with allure.step('Navigate to Post Job Request page'):
            self.loggedInNavigation.goToPostJobRequestPage()
            self.ts.markFinal(self.postJobRequestPage.isAt, "Navigation to post job request page successful", "Navigation to post job request page failed")

        with allure.step('Fill required details in describe your job page'):
            self.postJobRequestPage.postRemoteJobRequestChooseFlyers_DescribeJobPage(serviceCategory=td.testData("PostJobRequestData.service_category"),
                                                   setBudget=td.testData("PostJobRequestData.budget"))
            self.ts.markFinal(self.postJobRequestPage.isAt, "Describe your job", "Post Job Request failed")

        with allure.step('Fill required details in give details page'):
            self.postJobRequestPage.postRemoteJobRequestChooseFlyers_GiveDetailsPage(setJobTitle=td.testData("PostJobRequestData.job_title"),
                                                   setJobDesc=td.testData("PostJobRequestData.job_desc"))
            self.ts.markFinal(self.postJobRequestPage.isAt, "Give details", "Post Job Request failed")

        with allure.step('Choose flyers in find flyers page'):
            self.postJobRequestPage.postRemoteJobRequestChooseFlyers_FindFlyersPage()
            self.ts.markFinal(self.postJobRequestPage.isAt, "Choose flyers", "Post Job Request failed")

        with allure.step('Job Created and choose flyers page dispalyed'):
            self.postJobRequestPage.postRemoteJobRequestChooseFlyers_JobCreated()
            self.ts.markFinal(self.postJobRequestPage.isAt, "Job created successfully", "Post Job Request failed")

        with allure.step('Job successfully created and invited flyers'):
            self.postJobRequestPage.postRemoteJobRequestChooseFlyers_SelectFlyers()
            self.ts.markFinal(self.postJobRequestPage.isAt, "Post Job Request is successful", "Post Job Request failed")

        with allure.step('Navigate to My Jobs page'):
            self.loggedInNavigation.goToMyJobsPage()
            self.ts.markFinal(self.postJobRequestPage.isAt, "Navigation to my jobs page successful", "Navigation to my jobs page failed")



