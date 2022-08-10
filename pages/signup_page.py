import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class SignUpPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.signUpPage_locators = self.pageLocators('SignUpPage')

    @property
    def isAt(self):
        header_signUp = self.getElementList(*self.locator(self.signUpPage_locators, 'header_signUp'))
        if len(header_signUp) > 0:
            return True
        return False

    def signUp(self, firstName, lastName, email, username):
        self.sendKeys(firstName, *self.locator(self.signUpPage_locators, 'input_firstname'))
        self.sendKeys(lastName, *self.locator(self.signUpPage_locators, 'input_lastname'))
        self.sendKeys(email, *self.locator(self.signUpPage_locators, 'input_email'))
        self.sendKeys(username, *self.locator(self.signUpPage_locators, 'input_username'))
        self.elementClick(*self.locator(self.signUpPage_locators, 'btn_signUp'))
        self.page_has_loaded()

    def verifySignUpPageTitle(self, expectedTitle):
        return self.verifyPageTitle(expectedTitle)

    def verifyElementDisplayed(self, element):
        return self.isElementDisplayed(*self.locator(self.signUpPage_locators, element))

    def verifySignUpErrorMessage(self, expectedErrorMessage):
        return self.util.verifyTextMatch(self.getText(*self.locator(self.signUpPage_locators, 'txt_alertError')), expectedErrorMessage)