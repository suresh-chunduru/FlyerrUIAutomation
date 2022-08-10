import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class ProfilePage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.profilePage_locators = self.pageLocators('ProfilePage')

    @property
    def isAt(self):
        profileHeader = self.getElementList(*self.locator(self.profilePage_locators, 'headerTxt_profile'))
        if len(profileHeader) > 0:
            return True
        return False

    def isEditProfileModalDisplayed(self):
        if(self.isElementDisplayed(*self.locator(self.profilePage_locators, 'headerTxt_editProfile'))):
            self.log.info("Edit Profile modal window displayed")
            return True
        else:
            self.log.info("Edit Profile modal window not displayed")
            return False

    def isEditServiceLocationModalDisplayed(self):
        if(self.isElementDisplayed(*self.locator(self.profilePage_locators, 'headerTxt_editServiceLocation'))):
            self.log.info("Edit Profile modal window displayed")
            return True
        else:
            self.log.info("Edit Profile modal window not displayed")
            return False

    def isEditSkillsModalDisplayed(self):
        if(self.isElementDisplayed(*self.locator(self.profilePage_locators, 'headerTxt_editSkills'))):
            self.log.info("Edit Skills modal window displayed")
            return True
        else:
            self.log.info("Edit Skills modal window not displayed")
            return False

    def isEditServicesModalDisplayed(self):
        if(self.isElementDisplayed(*self.locator(self.profilePage_locators, 'headerTxt_editServices'))):
            self.log.info("Edit Services modal window displayed")
            return True
        else:
            self.log.info("Edit Services modal window not displayed")
            return False

    def isAddorEditListingsAndPackagesModalDisplayed(self):
        if(self.isElementDisplayed(*self.locator(self.profilePage_locators, 'headerTxt_editListingsAndPackages'))):
            self.log.info("Add ListingsAndPackages modal window displayed")
            return True
        else:
            self.log.info("Add ListingsAndPackages modal window not displayed")
            return False

    def isErrorPopUpDisplayed(self):
        if(self.isElementDisplayed(*self.locator(self.profilePage_locators, 'popup_errorPopUp'))):
            self.log.info("Error popup displayed")
            return True
        else:
            self.log.info("Error popup not displayed")
            return False

    def clickOKErrorPopUp(self):
        self.elementClick(*self.locator(self.profilePage_locators, 'btn_okErrorPopUp'))

    def isSuccessPopUpDisplayed(self):
        if(self.isElementDisplayed(*self.locator(self.profilePage_locators, 'popup_successPopUp'))):
            self.log.info("Success popup displayed")
            return True
        else:
            self.log.info("Success popup not displayed")
            return False

    def clickOKSuccessPopUp(self):
        self.elementClick(*self.locator(self.profilePage_locators, 'btn_okSuccessPopUp'))

    def editProfileDetails(self, publicName, minHourRate, maxHourRate, projectRate, respondsTime):
        self.clearAndSendKeys(publicName, *self.locator(self.profilePage_locators, 'input_publicDisplayName'))
        self.clearAndSendKeys(minHourRate, *self.locator(self.profilePage_locators, 'input_minHourlyRate'))
        self.clearAndSendKeys(maxHourRate, *self.locator(self.profilePage_locators, 'input_maxHourlyRate'))
        self.clearAndSendKeys(projectRate, *self.locator(self.profilePage_locators, 'input_projectRate'))
        self.elementClick(*self.locator(self.profilePage_locators, 'dropdown_respondsTime'))
        self.elementClick(*self.locator(self.profilePage_locators, 'option_respondsTimeHour'))

    def saveEditedProfileDetails(self):
        time.sleep(2)
        self.elementClick(*self.locator(self.profilePage_locators, 'btn_saveChangesEditProfile'))
        time.sleep(5)
        self.page_has_loaded()

    def verifyEditedProfileDetails(self, publicName, minHourRate, maxHourRate, projectRate, respondsTime):
        self.getText()

    def editServiceLocationDetails(self):
        self.elementClick(*self.locator(self.profilePage_locators, 'checkbox_inPerson'))
        self.elementClick(*self.locator(self.profilePage_locators, 'dropdown_radius'))
        self.elementClick(*self.locator(self.profilePage_locators, 'option_radius50KM'))
        self.elementClick(*self.locator(self.profilePage_locators, 'checkbox_remote'))


    def saveEditedServiceLocationDetails(self):
        time.sleep(2)
        self.elementClick(*self.locator(self.profilePage_locators, 'btn_saveChangesEditServiceLocation'))
        time.sleep(5)
        self.page_has_loaded()

    def verifyEditedServiceLocationDetails(self, publicName, minHourRate, maxHourRate, projectRate, respondsTime):
        self.getText()

    def clearSkills(self):
        existingSkills = self.getElementList(*self.locator(self.profilePage_locators, 'chip_addedSkills'))
        print("Length of existing skills: "+len(existingSkills).__str__())
        if len(existingSkills) > 0:
            self.log.info("Existing added skills displayed")
            self.log.info("Deleting existing added skills")
            for i in range(len(existingSkills)):
                self.elementClick(*self.locator(self.profilePage_locators, 'btn_skillDeleteIcon'))
        else:
            self.log.info("No existing added skills displayed")

    def editSkills(self, skills=[]):
        time.sleep(2)
        for skill in skills:
            self.sendKeys(skill, *self.locator(self.profilePage_locators, 'input_skills'))
            self.elementClick(*self.locator(self.profilePage_locators, 'btn_addSkills'))
        time.sleep(2)

    def saveEditedSkills(self):
        self.elementClick(*self.locator(self.profilePage_locators, 'btn_saveChangesEditSkills'))
        time.sleep(5)
        self.page_has_loaded()


    def verifyEditedSkills(self, publicName, minHourRate, maxHourRate, projectRate, respondsTime):
        self.getText()

    def clearServices(self):
        existingServices = self.getElementList(*self.locator(self.profilePage_locators, 'chip_addedServices'))
        print("Length of existing services: "+len(existingServices).__str__())
        if len(existingServices) > 0:
            self.log.info("Existing added services displayed")
            self.log.info("Deleting existing added services")
            for i in range(len(existingServices)):
                self.elementClick(*self.locator(self.profilePage_locators, 'btn_serviceDeleteIcon'))
        else:
            self.log.info("No existing added services displayed")

    def editServices(self, services=[]):
        time.sleep(2)
        dropdown_serviceList = self.getElement(*self.locator(self.profilePage_locators, 'dropdown_serviceList'))
        self.elementClick(*self.locator(self.profilePage_locators, 'dropdown_serviceList'))
        for service in services:
            for i in range(1,len(self.getElementList(*self.locator(self.profilePage_locators, 'options_serviceList')))):
                optionTextElement = dropdown_serviceList.find_element('xpath', "//mat-option[@role='option']["+i.__str__()+"]//span[contains(@class, 'mat-option-text')]")
                if self.getText(element=optionTextElement)==service:
                    self.elementClick(element=optionTextElement)
        self.clickOnScreen()
        # self.elementClick(*self.locator(self.profilePage_locators, 'overlayWrapper'))
        time.sleep(2)

    def saveEditedServices(self):
        self.elementClick(*self.locator(self.profilePage_locators, 'btn_saveChangesEditServices'))
        time.sleep(5)
        self.page_has_loaded()


    def verifyEditedServices(self, publicName, minHourRate, maxHourRate, projectRate, respondsTime):
        self.getText()


    def clearListingsAndPackages(self):
        existingListingsAndPackages = self.getElementList(*self.locator(self.profilePage_locators, 'items_addedListingsAndPackages'))
        sizeOfExistingListingsAndPackages = len(existingListingsAndPackages)
        print("Length of existing ListingsAndPackages: "+sizeOfExistingListingsAndPackages.__str__())

        if sizeOfExistingListingsAndPackages > 0:
            self.log.info("Existing added ListingsAndPackages displayed")
            self.log.info("Deleting existing added ListingsAndPackages")
            for i in range(sizeOfExistingListingsAndPackages+1):
                self.elementClick(*self.locator(self.profilePage_locators, 'btn_listingsAndPackagesDeleteIcon'))
                time.sleep(2)
                self.elementClick(*self.locator(self.profilePage_locators, 'btn_deleteConfirm'))
                time.sleep(3)
        else:
            self.log.info("No existing added ListingsAndPackages displayed")

    def addOrEditListingsAndPackages(self, title, serviceCategory, minPrice, maxPrice, details):
        time.sleep(2)
        self.sendKeys(title, *self.locator(self.profilePage_locators, 'input_listingsAndPackagesTitle'))
        dropdown_serviceCategoryList = self.getElement(*self.locator(self.profilePage_locators, 'dropdown_listingsAndPackagesServiceCategory'))
        self.elementClick(*self.locator(self.profilePage_locators, 'dropdown_listingsAndPackagesServiceCategory'))
        for i in range(1,len(self.getElementList(*self.locator(self.profilePage_locators, 'options_listingsAndPackagesServiceList')))):
            optionTextElement = dropdown_serviceCategoryList.find_element('xpath', "//mat-option[@role='option']["+i.__str__()+"]//span[contains(@class, 'mat-option-text')]")
            if self.getText(element=optionTextElement)==serviceCategory:
                self.elementClick(element=optionTextElement)
                break
        self.sendKeys(minPrice, *self.locator(self.profilePage_locators, 'input_listingsAndPackagesMinPrice'))
        self.sendKeys(maxPrice, *self.locator(self.profilePage_locators, 'input_listingsAndPackagesMaxPrice'))
        self.sendKeys(details, *self.locator(self.profilePage_locators, 'input_listingsAndPackagesDetails'))
        time.sleep(2)


    def saveAddedOrEditedListingsAndPackages(self):
        self.elementClick(*self.locator(self.profilePage_locators, 'btn_saveChangesEditListingsAndPackages'))
        time.sleep(5)
        self.page_has_loaded()


    def verifyEditedListingsAndPackages(self, publicName, minHourRate, maxHourRate, projectRate, respondsTime):
        self.getText()