"""
@package base

WebDriver Factory class implementation
It creates a web-driver instance based on browser configurations

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
import test_data.testData as td


class WebDriverFactory:

    def __init__(self):
        """
        Inits WebDriverFactory class
        :Returns None:
        """
        self.browser = td.testData("browser")
        self.baseUrl = td.testData("environment")

    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration

        :return 'WebDriver Instance':
        """

        if self.browser == "firefox":

            # Set Firefox driver
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            driver.maximize_window()

        elif self.browser == "chrome":

            # Set Chrome driver
            options = webdriver.ChromeOptions()
            # options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            options.add_argument("--window-size=1920,1080")
            options.add_argument('headless')
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            driver.maximize_window()

        elif self.browser == "edge":

            # Set Edge driver
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
            driver.maximize_window()

        else:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            driver.maximize_window()

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(15)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(self.baseUrl)

        return driver
