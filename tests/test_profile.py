from base.basepage import BasePage
from navigation.loggedInNavigation import LoggedInNavigation
from navigation.profileNavigation import ProfileNavigation
from pages.profilePage import ProfilePage
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
from pytest_testrail.plugin import pytestrail

sys.path.insert(0, '../..')


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ProfileTest(unittest.TestCase, BasePage):

    # # @pytest.mark.order(1)
    # @allure.story('KeyCloak') # epic/story of the test case
    # # @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # # @pytestrail.case('C48') # test case if on TestRail
    #
    # def test_Login_Verify_LoginPage(self):
    #
    #     self.homeNavigation = HomeNavigation(self.driver)
    #     self.loginPage = LoginPage(self.driver)
    #     self.loggedInPage = LoggedInPage(self.driver)
    #     self.ts = TestStatus(self.driver)
    #
    #     with allure.step('Navigate to login page'):
    #         self.homeNavigation.goToLoginPage()
    #         self.ts.markFinal(self.loginPage.isAt, "Navigation to login page", "Navigation to login page failed")
    #
    #     with allure.step('Verify login page title'):
    #         self.ts.markFinal(self.loginPage.verifyLoginPageTitle(td.testData("loginPage.title")), "Login page title verified", "Login page title verification failed")
    #
    #     with allure.step('Verify login page header display'):
    #         self.ts.markFinal(self.loginPage.verifyElementDisplayed('header_login'), "Login page header display verified", "Login page header display verification failed")
    #
    #     with allure.step('Verify login page username display'):
    #         self.ts.markFinal(self.loginPage.verifyElementDisplayed('input_username'), "Login page username display verified", "Login page username display verification failed")


    # @pytest.mark.order(2)
    @allure.story('Profile')  # epic/story of the test case
    # @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_Profile_Individual_Flyer_EditProfile(self):
        self.homeNavigation = HomeNavigation(self.driver)
        self.loggedInNavigation = LoggedInNavigation(self.driver)
        self.profileNavigation = ProfileNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely", "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page", "Navigation to login page failed")

        with allure.step('Login with IndividualAccount credentials'):
            self.loginPage.loginAndRefresh(username=td.testData("loginData.individual.username"), password=td.testData("loginData.individual.password"))
            self.ts.markFinal(self.loggedInPage.isAt, "Login with IndividualAccount successful", "Login with IndividualAccount failed")

        with allure.step('Navigate to Profile Page'):
            self.loggedInNavigation.goToProfilePage()
            self.ts.markFinal(self.profilePage.isAt, "Navigation to profile page", "Navigation to profile page failed")

        with allure.step('Navigate to Edit Profile Modal'):
                self.profileNavigation.goToEditProfile()
                self.ts.markFinal(self.profilePage.isEditProfileModalDisplayed(),
                                  "Edit profile modal displayed successfully",
                                  "Edit profile modal not displayed")

        with allure.step('Editing profile details - public name, min hour rate, max hour rate, project rate, responds time'):
            self.profilePage.editProfileDetails(publicName=td.testData("profileData.editProfile.publicDisplayName"),
                               minHourRate=td.testData("profileData.editProfile.minHourRate"),
                               maxHourRate=td.testData("profileData.editProfile.maxHourRate"),
                               projectRate=td.testData("profileData.editProfile.projectRate"),
                               respondsTime=td.testData("profileData.editProfile.respondsTime"))
            self.ts.markFinal(self.profilePage.isEditProfileModalDisplayed(),
                              "Edit profile - added profile details",
                              "Edit profile - adding details failed")
            time.sleep(2)
            self.profilePage.saveEditedProfileDetails()
            self.ts.markFinal(not self.profilePage.isEditProfileModalDisplayed(),
                                  "Edit profile modal dismissed successfully on Save Changes",
                                  "Edit profile modal not dismissed on Save Changes")
            self.ts.markFinal(not self.profilePage.isErrorPopUpDisplayed(), "Error popup not displayed after Save Changes", "Error popup displayed after Save Changes")
            # self.ts.markFinal(self.profilePage.isSuccessPopUpDisplayed(),
            #                   "Edit profile details saved and success popup displayed after Save Changes",
            #                   "Success popup not displayed after Save Changes")
            # self.profilePage.clickOKSuccessPopUp()

        # with allure.step('Verifying Edited profile details'):
        #     self.profilePage.verifyEditedProfileDetails()

    # @pytest.mark.order(3)
    @allure.story('Profile')  # epic/story of the test case
    # @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_Profile_Individual_Flyer_EditServiceLocation(self):
        self.homeNavigation = HomeNavigation(self.driver)
        self.loggedInNavigation = LoggedInNavigation(self.driver)
        self.profileNavigation = ProfileNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely", "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page", "Navigation to login page failed")

        with allure.step('Login with IndividualAccount credentials'):
            self.loginPage.loginAndRefresh(username=td.testData("loginData.individual.username"), password=td.testData("loginData.individual.password"))
            self.ts.markFinal(self.loggedInPage.isAt, "Login with IndividualAccount successful", "Login with IndividualAccount failed")

        with allure.step('Navigate to Profile Page'):
            self.loggedInNavigation.goToProfilePage()
            self.ts.markFinal(self.profilePage.isAt, "Navigation to profile page", "Navigation to profile page failed")

        with allure.step('Navigate to Edit Service Location modal'):
            self.profileNavigation.goToEditServiceLocation()
            self.ts.markFinal(self.profilePage.isEditServiceLocationModalDisplayed(), "Edit Service Location modal displayed successfully",
                              "Edit Service Location modal not displayed")

        with allure.step('Editing Service Location details'):
            self.profilePage.editServiceLocationDetails()
            self.ts.markFinal(self.profilePage.isEditServiceLocationModalDisplayed(),
                              "Edit Service Location - added details",
                              "Edit Service Location - adding details failed")
            time.sleep(2)
            self.profilePage.saveEditedServiceLocationDetails()
            self.ts.markFinal(not self.profilePage.isEditServiceLocationModalDisplayed(),
                              "Edit Service Location modal dismissed after save changes",
                              "Edit Service Location modal is not dismissed even after save changes")
            self.ts.markFinal(not self.profilePage.isErrorPopUpDisplayed(), "Edit Service Location saved successfully", "Edit Service Location details saving failed")
            # self.ts.markFinal(self.profilePage.isSuccessPopUpDisplayed(),
            #                   "Edit profile details saved and success popup displayed after Save Changes",
            #                   "Success popup not displayed after Save Changes")
            # self.profilePage.clickOKSuccessPopUp()

    # @pytest.mark.order(4)
    @allure.story('Profile')  # epic/story of the test case
    # @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_Profile_Individual_Flyer_EditSkills(self):
        self.homeNavigation = HomeNavigation(self.driver)
        self.loggedInNavigation = LoggedInNavigation(self.driver)
        self.profileNavigation = ProfileNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely", "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page", "Navigation to login page failed")

        with allure.step('Login with IndividualAccount credentials'):
            self.loginPage.loginAndRefresh(username=td.testData("loginData.individual.username"),
                                           password=td.testData("loginData.individual.password"))
            self.ts.markFinal(self.loggedInPage.isAt, "Login with IndividualAccount successful",
                              "Login with IndividualAccount failed")

        with allure.step('Navigate to Profile Page'):
            self.loggedInNavigation.goToProfilePage()
            self.ts.markFinal(self.profilePage.isAt, "Navigation to profile page", "Navigation to profile page failed")

        with allure.step('Navigate to Edit Skills Modal'):
            self.profileNavigation.goToEditSkills()
            self.ts.markFinal(self.profilePage.isEditSkillsModalDisplayed(),
                              "Edit Skills modal displayed successfully",
                              "Edit Skills modal not displayed")

        with allure.step('Editing Skills'):
            self.profilePage.clearSkills()
            self.profilePage.editSkills(td.testData("profileData.editSkills.skills"))
            self.ts.markFinal(self.profilePage.isEditSkillsModalDisplayed(),
                              "Edit Skills - added skills",
                              "Edit Skills - adding skills failed")
            self.profilePage.saveEditedSkills()
            time.sleep(5)
            self.ts.markFinal(not self.profilePage.isEditSkillsModalDisplayed(),
                              "Edit Skills modal dismissed successfully on Save Changes",
                              "Edit Skills modal not dismissed on Save Changes")
            self.ts.markFinal(not self.profilePage.isErrorPopUpDisplayed(), "Edit Skills saved successfully",
                              "Edit Skills saving failed")
            # self.ts.markFinal(self.profilePage.isSuccessPopUpDisplayed(),
            #                   "Edit profile details saved and success popup displayed after Save Changes",
            #                   "Success popup not displayed after Save Changes")
            # self.profilePage.clickOKSuccessPopUp()
        # with allure.step('Verifying Edited Skills'):
        #     self.profilePage.verifyEditedSkills()

    # @pytest.mark.order(5)
    @allure.story('Profile')  # epic/story of the test case
    # @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_Profile_Individual_Flyer_EditServices(self):
        self.homeNavigation = HomeNavigation(self.driver)
        self.loggedInNavigation = LoggedInNavigation(self.driver)
        self.profileNavigation = ProfileNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely",
                              "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page", "Navigation to login page failed")

        with allure.step('Login with IndividualAccount credentials'):
            self.loginPage.loginAndRefresh(username=td.testData("loginData.individual.username"),
                                           password=td.testData("loginData.individual.password"))
            self.ts.markFinal(self.loggedInPage.isAt, "Login with IndividualAccount successful",
                              "Login with IndividualAccount failed")

        with allure.step('Navigate to Profile Page'):
            self.loggedInNavigation.goToProfilePage()
            self.ts.markFinal(self.profilePage.isAt, "Navigation to profile page",
                              "Navigation to profile page failed")

        with allure.step('Navigate to Edit Services Modal'):
            self.profileNavigation.goToEditServices()
            self.ts.markFinal(self.profilePage.isEditServicesModalDisplayed(),
                              "Edit Services modal displayed successfully",
                              "Edit Services modal not displayed")

        with allure.step('Editing Services'):
            self.profilePage.clearServices()
            self.profilePage.editServices(td.testData("profileData.editServices.services"))
            self.ts.markFinal(self.profilePage.isEditServicesModalDisplayed(),
                              "Edit Services - added services",
                              "Edit Services - adding services failed")
            self.profilePage.saveEditedServices()
            time.sleep(5)
            self.ts.markFinal(not self.profilePage.isEditServicesModalDisplayed(),
                              "Edit Services modal dismissed successfully on Save Changes",
                              "Edit Services modal not dismissed on Save Changes")
            self.ts.markFinal(not self.profilePage.isErrorPopUpDisplayed(), "Edit Services saved successfully",
                              "Edit Services saving failed")

    # @pytest.mark.order(6)
    @allure.story('Profile')  # epic/story of the test case
    # @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_Profile_Individual_Flyer_EditListingAndPackages(self):
        self.homeNavigation = HomeNavigation(self.driver)
        self.loggedInNavigation = LoggedInNavigation(self.driver)
        self.profileNavigation = ProfileNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.ts = TestStatus(self.driver)

        with allure.step('Waiting for homepage to completely load'):
            self.ts.markFinal(self.page_has_loaded(), "Homepage loaded completely",
                              "Homepage not loaded completely")

        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "Navigation to login page", "Navigation to login page failed")

        with allure.step('Login with IndividualAccount credentials'):
            self.loginPage.loginAndRefresh(username=td.testData("loginData.individual.username"),
                                           password=td.testData("loginData.individual.password"))
            self.ts.markFinal(self.loggedInPage.isAt, "Login with IndividualAccount successful",
                              "Login with IndividualAccount failed")

        with allure.step('Navigate to Profile Page'):
            self.loggedInNavigation.goToProfilePage()
            self.ts.markFinal(self.profilePage.isAt, "Navigation to profile page",
                              "Navigation to profile page failed")

        with allure.step('Clear existing packages and navigate to Add ListingsAndPackages Modal'):
            self.profilePage.clearListingsAndPackages()
            self.profileNavigation.goToEditListingsAndPackages()
            self.ts.markFinal(self.profilePage.isAddorEditListingsAndPackagesModalDisplayed(),
                              "Add ListingsAndPackages modal displayed successfully",
                              "Add ListingsAndPackages modal not displayed")

        with allure.step('Adding ListingsAndPackages'):
            self.profilePage.addOrEditListingsAndPackages(title=td.testData("profileData.addListingsAndPackages.title"),
                                                          serviceCategory=td.testData("profileData.addListingsAndPackages.serviceCategory"),
                                                          minPrice=td.testData("profileData.addListingsAndPackages.minPrice"),
                                                          maxPrice=td.testData("profileData.addListingsAndPackages.maxPrice"),
                                                          details=td.testData("profileData.addListingsAndPackages.details"))
            self.ts.markFinal(self.profilePage.isAddorEditListingsAndPackagesModalDisplayed(),
                              "Add ListingsAndPackages - added details",
                              "Add ListingsAndPackages - adding details failed")
            self.profilePage.saveAddedOrEditedListingsAndPackages()
            time.sleep(5)
            self.ts.markFinal(not self.profilePage.isAddorEditListingsAndPackagesModalDisplayed(),
                              "Add ListingsAndPackages modal dismissed successfully on Save Changes",
                              "Add ListingsAndPackages modal not dismissed on Save Changes")
            self.ts.markFinal(not self.profilePage.isErrorPopUpDisplayed(), "Add ListingsAndPackages saved successfully",
                              "Add ListingsAndPackages saving failed")



