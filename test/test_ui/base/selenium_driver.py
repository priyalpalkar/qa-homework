from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class DriverFactory(object):

    def driver_factory(self):
        driver = webdriver.Remote(
           command_executor='http://chrome:4444/wd/hub',
           desired_capabilities=DesiredCapabilities.CHROME)
        return driver
