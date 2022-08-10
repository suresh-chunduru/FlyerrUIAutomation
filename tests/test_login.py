from base.basepage import BasePage
from utilities.teststatus import TestStatus
from navigation.homeNavigation import HomeNavigation
from pages.login_page import LoginPage
from pages.loggedin_page import LoggedInPage
import test_data.testData as td
import unittest
import pytest
import sys
import allure
from pytest_testrail.plugin import pytestrail

sys.path.insert(0, '../..')


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase, BasePage):

    # @pytest.mark.order(1)
    @allure.story('KeyCloak') # epic/story of the test case
    # @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail

    def test_Login_Verify_LoginPage(self):

        self.homeNavigation = HomeNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely", "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page", "Navigation to login page failed")

        with allure.step('Verify login page title'):
            self.ts.markFinal(self.loginPage.verifyLoginPageTitle(td.testData("loginPage.title")), "Login page title verified", "Login page title verification failed")

        with allure.step('Verify login page header display'):
            self.ts.markFinal(self.loginPage.verifyElementDisplayed('header_login'), "Login page header display verified", "Login page header display verification failed")

        with allure.step('Verify login page username display'):
            self.ts.markFinal(self.loginPage.verifyElementDisplayed('input_username'), "Login page username display verified", "Login page username display verification failed")

        with allure.step('Verify login page password display'):
            self.ts.markFinal(self.loginPage.verifyElementDisplayed('input_password'), "Login page password display verified", "Login page password display verification failed")

        with allure.step('Verify login page checkbox_rememberme display'):
            self.ts.markFinal(self.loginPage.verifyElementDisplayed('checkbox_rememberme'), "Login page checkbox_rememberme display verified", "Login page checkbox_rememberme display verification failed")

        with allure.step('Verify login page link_forgotPassword display'):
            self.ts.markFinal(self.loginPage.verifyElementDisplayed('link_forgotPassword'), "Login page link_forgotPassword display verified", "Login page link_forgotPassword display verification failed")

        with allure.step('Verify login page btn_login display'):
            self.ts.markFinal(self.loginPage.verifyElementDisplayed('btn_login'), "Login page btn_login display verified", "Login page btn_login display verification failed")

        with allure.step('Verify login page txt_orLoginWith display'):
            self.ts.markFinal(self.loginPage.verifyElementDisplayed('txt_orLoginWith'), "Login page txt_orLoginWith display verified", "Login page txt_orLoginWith display verification failed")

        with allure.step('Verify login page btn_google display'):
            self.ts.markFinal(self.loginPage.verifyElementDisplayed('btn_google'), "Login page btn_google display verified", "Login page btn_google display verification failed")

        with allure.step('Verify login page txt_doNotHaveAnAccount display'):
            self.ts.markFinal(self.loginPage.verifyElementDisplayed('txt_doNotHaveAnAccount'), "Login page txt_doNotHaveAnAccount display verified", "Login page txt_doNotHaveAnAccount display verification failed")

        with allure.step('Verify login page link_signUp display'):
            self.ts.markFinal(self.loginPage.verifyElementDisplayed('link_signUp'), "Login page link_signUp display verified", "Login page link_signUp display verification failed")

    # @pytest.mark.order(2)
    @allure.story('KeyCloak')  # epic/story of the test case
    # @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_Login_Login_with_Admin(self):

        self.homeNavigation = HomeNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely", "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page", "Navigation to login page failed")

        with allure.step('Login with Admin credentials'):
            self.loginPage.login(username=td.testData("loginData.admin.username"), password=td.testData("loginData.admin.password"))
            self.ts.markFinal(self.loggedInPage.isAt, "Login with admin successful", "Login with admin failed")

    # @pytest.mark.order(3)
    @allure.story('KeyCloak')  # epic/story of the test case
    # @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_Login_Login_with_IndividualAccount(self):

        self.homeNavigation = HomeNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely", "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page", "Navigation to login page failed")

        with allure.step('Login with IndividualAccount credentials'):
            self.loginPage.login(username=td.testData("loginData.individual.username"), password=td.testData("loginData.individual.password"))
            self.ts.markFinal(self.loggedInPage.isAt, "Login with IndividualAccount successful", "Login with IndividualAccount failed")

    # @pytest.mark.order(4)
    @allure.story('KeyCloak')  # epic/story of the test case
    # @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_Login_Login_with_BusinessAccount(self):

        self.homeNavigation = HomeNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely", "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page", "Navigation to login page failed")

        with allure.step('Login with BusinessAccount credentials'):
            self.loginPage.login(username=td.testData("loginData.business.username"), password=td.testData("loginData.business.password"))
            self.ts.markFinal(self.loggedInPage.isAt, "Login with BusinessAccount successful", "Login with BusinessAccount failed")

    # @pytest.mark.order(5)
    @allure.story('KeyCloak')  # epic/story of the test case
    # @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_Login_Login_with_InvalidCredentials_VerifyErrorMessage(self):

        self.homeNavigation = HomeNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely", "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page", "Navigation to login page failed")

        with allure.step('Login with Invalid credentials'):
            self.loginPage.login(username=td.testData("loginData.invalid.username"), password=td.testData("loginData.invalid.password"))
            self.ts.markFinal(self.loginPage.isAt, "Login with InvalidCredentials verified", "Login with InvalidCredentials failed")
            self.ts.markFinal(self.loginPage.verifyLoginErrorMessage(td.testData("loginPage.loginErrorInvalidCredentials")), "Login alert error message verified", "Login alert error message verification failed")

    # @pytest.mark.order(6)
    @allure.story('KeyCloak')  # epic/story of the test case
    # @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_Login_Login_with_Google(self):
        self.homeNavigation = HomeNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely", "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page", "Navigation to login page failed")

        with allure.step('Login with Google credentials'):
            self.loginPage.loginWithGoogle(username=td.testData("loginData.google.username"), password=td.testData("loginData.google.password"))
            self.ts.markFinal(self.loggedInPage.isAt, "Login with Google successful", "Login with Google failed")
