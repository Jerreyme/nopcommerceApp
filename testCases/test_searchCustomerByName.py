import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_005_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression

    def test_searchCustomerByName(self, setup):
        self.logger.info("************ Test_005_SearchCustomerByName ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************ Login successful ************")

        self.logger.info("********** Starting Search Customer Customer By Name **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickCustomersMenu()
        self.addcust.clickCustomerMenuItem()

        self.logger.info("************* Searching Customer By Name *************")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Brenda")
        searchcust.setLastName("Lindgren")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Brenda Lindgren")
        assert True == status
        self.driver.close()
        self.logger.info("************ Test_005_SearchCustomerByName Finished ************")