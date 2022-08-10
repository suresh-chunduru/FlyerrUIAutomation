import utilities.custom_logger as cl
import logging
from base.basepage import BasePage



class CountrySettingsPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.countrySettings_locators = self.pageLocators('CountrySettings')

    @property
    def isAt(self):
        header_countrySettings = self.getElementList(*self.locator(self.countrySettings_locators, 'header_countrySettings'))
        if len(header_countrySettings) > 0:
            return True
        return False

    def verifyCountrySettingsColumnHeaders(self, expectedHeaders):
        column_headers = self.getElementList(*self.locator(self.countrySettings_locators, 'txt_columnHeaders'))
        if len(column_headers) == len(expectedHeaders):
            for i, columnHeader in enumerate(column_headers):
                if self.util.verifyTextMatch(self.getText(element=columnHeader), expectedHeaders[i]):
                    self.log.info("CountrySettings ColumnHeader matched- Actual: "+self.getText(element=columnHeader)+", Expected: "+expectedHeaders[i])
                else:
                    self.log.info("CountrySettings ColumnHeader not matched- Actual: " + self.getText(element=columnHeader) + ", Expected: " + expectedHeaders[i])
                    return False
                    break
            return True
        else:
            self.log.error("CountrySettings ColumnHeaders size not matched with expectedColumnHeaders ")
            return False

    def verifyFirstRowCountryName(self, expectedName):
        table = self.getElement(*self.locator(self.countrySettings_locators, 'table_body'))
        rowSize = len(table.find_elements('xpath', "//tbody//tr[@role= 'row']"))
        # for i in range(rowSize):
        #     print("RowSize:" + rowSize.__str__())
        #     row = table.find_element('xpath',"//tbody//tr[@role= 'row']["+(i+1).__str__()+"]")
        #     colSize= len(row.find_elements('xpath',"//tbody//tr[@role= 'row']["+(i+1).__str__()+"]"+"//td[@role='gridcell']"))
        #     print("ColSize:"+ colSize.__str__())
        #     for j in range(colSize):
        #         col = row.find_element('xpath',"//tbody//tr[@role= 'row']["+(i+1).__str__()+"]"+"//td[@role='gridcell']"+"["+(j+1).__str__()+"]")
        #         print(self.getText(element=col))
        #     # for column in columns:
        #     #     print(self.getText(element=column))
        firstRow = table.find_element('xpath', "//tbody//tr[@role= 'row'][1]")
        firstRow2ndCol = firstRow.find_element('xpath', "//tbody//tr[@role= 'row'][1]" + "//td[@role='gridcell'][2]")
        return self.util.verifyTextMatch(self.getText(element=firstRow2ndCol), expectedName)

    def verifyLastRowCountryName(self, expectedName):
        table = self.getElement(*self.locator(self.countrySettings_locators, 'table_body'))
        rowSize = len(table.find_elements('xpath',"//tbody//tr[@role= 'row']"))
        # for i in range(rowSize):
        #     print("RowSize:" + rowSize.__str__())
        #     row = table.find_element('xpath',"//tbody//tr[@role= 'row']["+(i+1).__str__()+"]")
        #     colSize= len(row.find_elements('xpath',"//tbody//tr[@role= 'row']["+(i+1).__str__()+"]"+"//td[@role='gridcell']"))
        #     print("ColSize:"+ colSize.__str__())
        #     for j in range(colSize):
        #         col = row.find_element('xpath',"//tbody//tr[@role= 'row']["+(i+1).__str__()+"]"+"//td[@role='gridcell']"+"["+(j+1).__str__()+"]")
        #         print(self.getText(element=col))
        #     # for column in columns:
        #     #     print(self.getText(element=column))
        lastRow = table.find_element('xpath',"//tbody//tr[@role= 'row']["+(rowSize).__str__()+"]")
        lastRow2ndCol = lastRow.find_element('xpath', "//tbody//tr[@role= 'row'][" + (rowSize).__str__() + "]" + "//td[@role='gridcell'][2]")
        return self.util.verifyTextMatch(self.getText(element=lastRow2ndCol), expectedName)

    def verifyElementDisplayed(self, element):
        return self.isElementDisplayed(*self.locator(self.countrySettings_locators, element))

    def verifyTextMatch(self, element, expectedText):
        return self.util.verifyTextMatch(self.getText(*self.locator(self.countrySettings_locators, element)),expectedText)