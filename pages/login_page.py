import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.loginPage_locators = self.pageLocators('LoginPage')
        self.loginPageGoogle_locators = self.pageLocators('LoginPageGoogle')

    @property
    def isAt(self):
        header_login = self.getElementList(*self.locator(self.loginPage_locators, 'header_login'))
        if len(header_login) > 0:
            return True
        return False

    def login(self, username, password):
        self.sendKeys(username, *self.locator(self.loginPage_locators, 'input_username'))
        self.sendKeys(password, *self.locator(self.loginPage_locators, 'input_password'))
        self.elementClick(*self.locator(self.loginPage_locators, 'btn_login'))
        time.sleep(5)

    def loginAndRefresh(self, username, password):
        self.sendKeys(username, *self.locator(self.loginPage_locators, 'input_username'))
        self.sendKeys(password, *self.locator(self.loginPage_locators, 'input_password'))
        self.elementClick(*self.locator(self.loginPage_locators, 'btn_login'))
        self.page_has_loaded()
        self.refresh()
        self.page_has_loaded()
        time.sleep(5)


    def verifyLoginPageTitle(self, expectedTitle):
        return self.verifyPageTitle(expectedTitle)

    def verifyElementDisplayed(self, element):
        return self.isElementDisplayed(*self.locator(self.loginPage_locators, element))

    def verifyLoginErrorMessage(self, expectedErrorMessage):
        return self.util.verifyTextMatch(self.getText(*self.locator(self.loginPage_locators, 'txt_alertError')), expectedErrorMessage)

    def loginWithGoogle(self, username, password):
        self.elementClick(*self.locator(self.loginPage_locators, 'btn_google'))
        self.sendKeys(username, *self.locator(self.loginPageGoogle_locators, 'input_username'))
        self.elementClick(*self.locator(self.loginPageGoogle_locators, 'btn_next'))
        self.sendKeys(password, *self.locator(self.loginPageGoogle_locators, 'input_password'))
        self.elementClick(*self.locator(self.loginPageGoogle_locators, 'btn_next'))
        self.page_has_loaded()

