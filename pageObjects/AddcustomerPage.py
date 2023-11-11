import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_xpath = "//input[@id='Gender_Male']"
    rdFemaleGender_xpath = "//input[@id='Gender_Female']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    chckbxTaxExempt_xpath = "//input[@id='IsTaxExempt']"
    lstNewsletter_xpath = "(//div[@role='listbox'])[1]"
    lstitemYourStoreName_xpath = "//li[@id='d8749800-681c-4b3c-9de5-84c6a7828941']"
    lstitemTestStore2_xpath = "//li[normalize-space()='Test store 2']"
    txtCustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lstitemAdministrators_xpath = "//li[@id='3321e5ff-e11a-4e6f-b85d-b87542b5cdc8']"
    lstitemForumModerators_xpath = "//li[normalize-space()='Forum Moderators']"
    lstitemGuests_xpath = "//li[normalize-space()='Guests']"
    lstitemRegistered_xpath = "//li[normalize-space()='Registered']"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    lstitemRegistered_clear_xpath = "(//span[@title='delete'])[2]"
    drpMgrOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminContext_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"


    def __init__(self, driver):
        self.driver = driver

    def clickCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()
        time.sleep(3)

    def clickCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()
        time.sleep(3)

    def clickAddNewbutton(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()
        time.sleep(3)

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lastname)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.rdFemaleGender_xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.rdFemaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, compname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(compname)

    def checkboxTaxExempt(self):
        self.driver.find_element(By.XPATH, self.chckbxTaxExempt_xpath).click()
        time.sleep(3)

    def setNewsletter(self, newsletter):
        self.driver.find_element(By.XPATH, self.lstNewsletter_xpath).click()
        time.sleep(3)
        if newsletter == 'Your store name':
            self.lstNewsItem = self.driver.find_element(By.XPATH, self.lstitemYourStoreName_xpath)
        elif newsletter == 'Test store 2':
            self.lstNewsItem = self.driver.find_element(By.XPATH, self.lstitemTestStore2_xpath)
        else:
            self.lstNewsItem = self.driver.find_element(By.XPATH, self.lstitemTestStore2_xpath,
                                                        self.lstitemYourStoreName_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.lstNewsItem)
        time.sleep(3)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered (or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.lstitemRegistered_clear_xpath).click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == 'Forum Moderators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemForumModerators_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        time.sleep(3)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)
        time.sleep(3)

    def setManagerOfVender(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpMgrOfVendor_xpath))
        drp.select_by_visible_text(value)
        time.sleep(3)

    def setAdminComment(self, comment):
        self.driver.find_element(By.XPATH, self.txtAdminContext_xpath).send_keys(comment)
        time.sleep(3)

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()

