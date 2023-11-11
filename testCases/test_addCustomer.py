import random
import string

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression

    def test_addCustomer(self, setup):
        self.logger.info("************ Test_003_AddCustomer ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************ Login successful ************")

        self.logger.info("********** Starting Add Customer Test **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickCustomersMenu()
        self.addcust.clickCustomerMenuItem()
        self.addcust.clickAddNewbutton()

        self.logger.info("************* Providing customer info *************")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Jem")
        self.addcust.setLastName("Tester")
        self.addcust.setGender("Male")
        self.addcust.setDOB("07/05/1985") # Format: D/MM/YYYY
        self.addcust.setCompanyName("busyQA")
        self.addcust.checkboxTaxExempt()
        self.addcust.setNewsletter("Test store 2")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVender("Vendor 2")
        self.addcust.setAdminComment("This is for testing............")
        self.addcust.clickSave()

        self.logger.info("************** Saving customer info *************")
        self.logger.info("************** Add customer validation started **************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("********** Add customer Test Passed **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png") # Screenshot
            self.logger.info("********** Add customer Test Failed **********")
            assert True == False

        self.driver.close()
        self.logger.info("********** Ending Test_003_AddCustomer **********")