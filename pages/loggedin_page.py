import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class LoggedInPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.loggedInPage_locators = self.pageLocators('LoggedInPage')

    @property
    def isAt(self):
        btn_hiMenu = self.getElementList(*self.locator(self.loggedInPage_locators, 'btn_hiMenu'))
        if len(btn_hiMenu) > 0:
            return True
        return False
