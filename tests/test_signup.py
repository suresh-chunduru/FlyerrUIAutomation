from base.basepage import BasePage
from navigation.loginNavigation import LoginNavigation
from pages.emailVerificationPage import EmailVerificationPage
from pages.signup_page import SignUpPage
from utilities.teststatus import TestStatus
from navigation.homeNavigation import HomeNavigation
from pages.login_page import LoginPage
from pages.loggedin_page import LoggedInPage
import test_data.testData as td
import unittest
import pytest
import sys
import allure
import random


sys.path.insert(1, '../..')


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SignUpTest(unittest.TestCase, BasePage):

    # @pytest.mark.order(1)
    @allure.story('KeyCloak')  # epic/story of the test case
    @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_Signup_Verify_Signup_page(self):
        self.homeNavigation = HomeNavigation(self.driver)
        self.loginNavigation = LoginNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.signUpPage = SignUpPage(self.driver)
        self.emailVerificationPage = EmailVerificationPage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely", "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page", "Navigation to login page failed")

        with allure.step('Navigate to signup page'):
            self.loginNavigation.goToSignUpPage()
            self.ts.markFinal(self.signUpPage.isAt, "Navigation to signup page", "Navigation to signup page failed")

        with allure.step('Verify signup page title'):
            self.ts.markFinal(self.signUpPage.verifySignUpPageTitle(td.testData("signUpPage.title")), "SignUp page title verified", "SignUp page title verification failed")

        with allure.step('Verify SignUp page header display'):
            self.ts.markFinal(self.signUpPage.verifyElementDisplayed('header_signUp'), "SignUp page header display verified", "SignUp page header display verification failed")

        with allure.step('Verify SignUp page firstname display'):
            self.ts.markFinal(self.signUpPage.verifyElementDisplayed('input_firstname'), "SignUp page firstname display verified", "SignUp page firstname display verification failed")

        with allure.step('Verify SignUp page lastname display'):
            self.ts.markFinal(self.signUpPage.verifyElementDisplayed('input_lastname'), "SignUp page lastname display verified", "SignUp page lastname display verification failed")

        with allure.step('Verify SignUp page email display'):
            self.ts.markFinal(self.signUpPage.verifyElementDisplayed('input_email'), "SignUp page email display verified", "SignUp page email display verification failed")

        with allure.step('Verify SignUp page username display'):
            self.ts.markFinal(self.signUpPage.verifyElementDisplayed('input_username'), "SignUp page username display verified", "SignUp page username display verification failed")

        with allure.step('Verify SignUp page iAcceptCheckBox display'):
            self.ts.markFinal(self.signUpPage.verifyElementDisplayed('checkbox_iAccept'), "SignUp page iAcceptCheckBox display verified", "SignUp page iAcceptCheckBox display verification failed")

        with allure.step('Verify SignUp page link_termsAndConditions display'):
            self.ts.markFinal(self.signUpPage.verifyElementDisplayed('link_termsAndConditions'), "SignUp page link_termsAndConditions display verified", "SignUp page link_termsAndConditions display verification failed")

        with allure.step('Verify SignUp page signup button display'):
            self.ts.markFinal(self.signUpPage.verifyElementDisplayed('btn_signUp'), "SignUp page signup button display verified", "SignUp page signup button display verification failed")

        with allure.step('Verify SignUp page txt_orRegisterWith display'):
            self.ts.markFinal(self.signUpPage.verifyElementDisplayed('txt_orRegisterWith'), "SignUp page txt_orRegisterWith display verified", "SignUp page txt_orRegisterWith display verification failed")

        with allure.step('Verify SignUp page btn_google display'):
            self.ts.markFinal(self.signUpPage.verifyElementDisplayed('btn_google'), "SignUp page btn_google display verified", "SignUp page btn_google display verification failed")

        with allure.step('Verify SignUp page txt_AlreadyHaveAnAccount display'):
            self.ts.markFinal(self.signUpPage.verifyElementDisplayed('txt_AlreadyHaveAnAccount'), "SignUp page txt_AlreadyHaveAnAccount display verified", "SignUp page txt_AlreadyHaveAnAccount display verification failed")

        with allure.step('Verify SignUp page link_signIn display'):
            self.ts.markFinal(self.signUpPage.verifyElementDisplayed('link_signIn'), "SignUp page link_signIn display verified", "SignUp page link_signIn display verification failed")

    # @pytest.mark.order(2)
    @allure.story('KeyCloak') # epic/story of the test case
    @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_Signup_CreateAccount_Individual(self):

        self.homeNavigation = HomeNavigation(self.driver)
        self.loginNavigation = LoginNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.signUpPage = SignUpPage(self.driver)
        self.emailVerificationPage = EmailVerificationPage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely", "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page", "Navigation to login page failed")

        with allure.step('Navigate to signup page'):
            self.loginNavigation.goToSignUpPage()
            self.ts.markFinal(self.signUpPage.isAt, "Navigation to signup page", "Navigation to signup page failed")

        with allure.step('Sign up with details'):
            randomValue = (random.randrange(1000, 9999, 4)).__str__()
            self.signUpPage.signUp(firstName=td.testData("signUpData.individual.firstname"),
                                   lastName=td.testData("signUpData.individual.lastname"),
                                   email=td.testData("signUpData.individual.email")+randomValue+"@gmaill.com",
                                   username=td.testData("signUpData.individual.username")+randomValue)

            self.ts.markFinal(self.emailVerificationPage.isAt, "Signup successful", "Signup failed")

    # @pytest.mark.order(3)
    @allure.story('KeyCloak') # epic/story of the test case
    @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_VerifyErrorSigup_with_existing_username(self):

        self.homeNavigation = HomeNavigation(self.driver)
        self.loginNavigation = LoginNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.signUpPage = SignUpPage(self.driver)
        self.emailVerificationPage = EmailVerificationPage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely", "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page", "Navigation to login page failed")

        with allure.step('Navigate to signup page'):
            self.loginNavigation.goToSignUpPage()
            self.ts.markFinal(self.signUpPage.isAt, "Navigation to signup page", "Navigation to signup page failed")

        with allure.step('Sign up with existing username details'):
            self.signUpPage.signUp(firstName=td.testData("signUpData.existingUserName.firstname"),
                                   lastName=td.testData("signUpData.existingUserName.lastname"),
                                   email=td.testData("signUpData.existingUserName.email"),
                                   username=td.testData("signUpData.existingUserName.username"))

            self.ts.markFinal(self.signUpPage.isAt, "SignUp with existing username verified", "SignUp with existing username failed")
            self.ts.markFinal(self.signUpPage.verifySignUpErrorMessage(td.testData("signUpPage.signUpErrorExistingUsername")),"Signup with existing username alert error message verified", "Signup with existing username alert error message verification failed")

    # @pytest.mark.order(4)
    @allure.story('KeyCloak') # epic/story of the test case
    @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_VerifyErrorSigup_with_existing_email(self):

        self.homeNavigation = HomeNavigation(self.driver)
        self.loginNavigation = LoginNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.signUpPage = SignUpPage(self.driver)
        self.emailVerificationPage = EmailVerificationPage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely", "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page", "Navigation to login page failed")

        with allure.step('Navigate to signup page'):
            self.loginNavigation.goToSignUpPage()
            self.ts.markFinal(self.signUpPage.isAt, "Navigation to signup page", "Navigation to signup page failed")

        with allure.step('Sign up with existing email details'):
            self.signUpPage.signUp(firstName=td.testData("signUpData.existingEmail.firstname"),
                                   lastName=td.testData("signUpData.existingEmail.lastname"),
                                   email=td.testData("signUpData.existingEmail.email"),
                                   username=td.testData("signUpData.existingEmail.username"))

            self.ts.markFinal(self.signUpPage.isAt, "SignUp with existing email verified", "SignUp with existing email failed")
            self.ts.markFinal(self.signUpPage.verifySignUpErrorMessage(td.testData("signUpPage.signUpErrorExistingEmail")),"Singup with existing email alert error message verified", "Singup with existing email alert error message verification failed")
