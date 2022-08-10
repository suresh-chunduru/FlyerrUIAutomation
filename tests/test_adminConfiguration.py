from base.basepage import BasePage
from navigation.adminNavigation import AdminNavigation
from navigation.countrySettingsNavigation import CountrySettingsNavigation
from pages.adminConfiguration_page import AdminConfigurationPage
from navigation.loginNavigation import LoginNavigation
from pages.countrySettingsPage import CountrySettingsPage
from utilities.teststatus import TestStatus
from navigation.homeNavigation import HomeNavigation
from pages.login_page import LoginPage
from pages.loggedin_page import LoggedInPage
import test_data.testData as td
import unittest
import pytest
import sys
import allure
import time
import random
from pytest_testrail.plugin import pytestrail

sys.path.insert(1, '../..')


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AdminConfigurationsTest(unittest.TestCase, BasePage):

    # @pytest.mark.order(1)
    @allure.story('AdminConfiguration')  # epic/story of the test case
    @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_Admin_Verify_Admin_Page(self):
        self.homeNavigation = HomeNavigation(self.driver)
        self.loginNavigation = LoginNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.adminConfigurationPage = AdminConfigurationPage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely", "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page", "Navigation to login page failed")

        with allure.step('Login with Admin credentials'):
            self.loginPage.login(username=td.testData("loginData.admin.username"),
                                 password=td.testData("loginData.admin.password"))
            self.ts.markFinal(self.loggedInPage.isAt, "Login with admin successful", "Login with admin failed")
            self.ts.markFinal(self.adminConfigurationPage.isAt, "Landing/Navigating to admin config page","Landing/Navigating to admin config page failed")

        with allure.step('Verify admin page title'):
            self.ts.markFinal(self.adminConfigurationPage.verifyAdminPageTitle(td.testData("adminPage.title")),"Admin page title verified failed", "Admin page title verification failed")

        with allure.step('Verify profile navigation item display'):
            self.ts.markFinal(self.adminConfigurationPage.verifyElementDisplayed('link_profile'), "Admin page profile navigation item display verified", "Admin page profile navigation item display verification failed")

        with allure.step('Verify account navigation item display'):
            self.ts.markFinal(self.adminConfigurationPage.verifyElementDisplayed('link_account'), "Admin page account navigation item display verified", "Admin page account navigation item display verification failed")

        with allure.step('Verify countrySettings navigation item display'):
            self.ts.markFinal(self.adminConfigurationPage.verifyElementDisplayed('link_countrySettings'), "Admin page countrySettings navigation item display verified", "Admin page countrySettings navigation item display verification failed")

    # @pytest.mark.order(2)
    @allure.story('AdminConfiguration')  # epic/story of the test case
    @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_Admin_Verify_CountrySettings_Pagination(self):
        self.homeNavigation = HomeNavigation(self.driver)
        self.loginNavigation = LoginNavigation(self.driver)
        self.adminNavigation = AdminNavigation(self.driver)
        self.countrySettingsNavigation = CountrySettingsNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.adminConfigurationPage = AdminConfigurationPage(self.driver)
        self.countrySettingsPage = CountrySettingsPage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely", "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page", "Navigation to login page failed")

        with allure.step('Login with Admin credentials'):
            self.loginPage.login(username=td.testData("loginData.admin.username"),
                                 password=td.testData("loginData.admin.password"))
            self.ts.markFinal(self.loggedInPage.isAt, "Login with admin successful", "Login with admin failed")
            self.ts.markFinal(self.adminConfigurationPage.isAt, "Landing/Navigating to admin config page","Landing/Navigating to admin config page failed")

        with allure.step('Navigate to Country Settings'):
            self.adminNavigation.goToCountrySettings()
            self.ts.markFinal(self.countrySettingsPage.isAt, "Navigation to CountrySettings", "Navigation to Country Settings failed")

        with allure.step('Verify Country Settings header text'):
            self.ts.markFinal(self.countrySettingsPage.verifyTextMatch("header_countrySettings", td.testData("countrySettingsPage.headerTextCountrySettings")), "Country Settings header text verified", "Country Settings header text verification failed")

        with allure.step('Verify Country Settings headers text'):
            self.ts.markFinal(self.countrySettingsPage.verifyCountrySettingsColumnHeaders(td.testData("countrySettingsPage.columnHeaders")),"Country Settings column headers text verified","Country Settings column headers text verification failed")

        with allure.step('Verify Country Settings first page first row CountryName'):
            self.ts.markFinal(self.countrySettingsPage.verifyFirstRowCountryName(td.testData("countrySettingsPage.firstPageFirstRowCountryName")),"Country Settings first page first row CountryName verified","Country Settings first page first row CountryName verification failed")

        with allure.step('Navigate to next page of Country List'):
            self.countrySettingsNavigation.goToNextPage()

        with allure.step('Verify Country Settings 2nd page last row CountryName'):
            self.ts.markFinal(self.countrySettingsPage.verifyLastRowCountryName(td.testData("countrySettingsPage.2ndPageLastRowCountryName")),"Country Settings 2nd page last row CountryName verified","Country Settings 2nd page last row CountryName verification failed")

        with allure.step('Navigate to last page of Country List'):
            self.countrySettingsNavigation.goToLastPage()

        with allure.step('Verify Country Settings last page last row CountryName'):
            self.ts.markFinal(self.countrySettingsPage.verifyLastRowCountryName(td.testData("countrySettingsPage.lastPageLastRowCountryName")),"Country Settings last page last row CountryName verified","Country Settings last page last row CountryName verification failed")

        with allure.step('Navigate to Prev page of Country List'):
            self.countrySettingsNavigation.goToPreviousPage()

        with allure.step('Verify Country Settings lastPrev page first row CountryName'):
            self.ts.markFinal(self.countrySettingsPage.verifyFirstRowCountryName(td.testData("countrySettingsPage.LastPrevPageFirstRowCountryName")),"Country Settings lastPrev page first row CountryName verified","Country Settings lastPrev page first row CountryName verification failed")

