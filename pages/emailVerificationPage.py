import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class EmailVerificationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.emailVerificationPage_locators = self.pageLocators('EmailVerificationPage')

    @property
    def isAt(self):
        header_emailVerificationPage = self.getElementList(*self.locator(self.emailVerificationPage_locators, 'header_emailVerification'))
        if len(header_emailVerificationPage) > 0:
            return True
        return False

    def verifyEmailVerificationPageTitle(self, expectedTitle):
        return self.verifyPageTitle(expectedTitle)

    def verifyElementDisplayed(self, element):
        return self.isElementDisplayed(*self.locator(self.emailVerificationPage_locators, element))

    def resendEmail(self):
        self.elementClick(*self.locator(self.emailVerificationPage_locators, 'btn_resend'))
        self.page_has_loaded()
