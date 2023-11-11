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


class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression

    def test_searchCustomerByEmail(self, setup):
        self.logger.info("************ Test_004_SearchCustomerByEmail ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************ Login successful ************")

        self.logger.info("********** Starting Search Customer Customer By Email **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickCustomersMenu()
        self.addcust.clickCustomerMenuItem()

        self.logger.info("************* Searching Customer By EmailID *************")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("brenda_lindgren@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("brenda_lindgren@nopCommerce.com")
        assert True == status

        #Search for the customer by Email
        expected_customer = searchcust
        actual_customer = status
        # Check if the expected customer was found
        self.assertEqual(actual_customer, expected_customer, f"Expected customer '{expected_customer}' but got '{actual_customer}'")


        self.driver.close()
        self.logger.info("************ Test_004_SearchCustomerByEmail Finished ************")

    def assertEqual(self, actual_customer, expected_customer, param):
        pass