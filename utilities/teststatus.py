from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from traceback import print_stack


class TestStatus(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        """
        Inits CheckPoint class

        """
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, passResultMessage, failResultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: " + passResultMessage)
                    self.screenShot(passResultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: " + failResultMessage)
                    self.screenShot(failResultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: " + failResultMessage)
                self.screenShot(failResultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occurred !!!")
            self.screenShot(failResultMessage)
            print_stack()

    def mark(self, result, passResultMessage, failResultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, passResultMessage, failResultMessage)

    def markFinal(self, result, passResultMessage, failResultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setResult(result, passResultMessage, failResultMessage)
        if "FAIL" in self.resultList:
            self.resultList.clear()
            assert False, failResultMessage

        else:
            self.resultList.clear()
            assert True, passResultMessage
