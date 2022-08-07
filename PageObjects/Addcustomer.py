import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Addcustomer:
    link_customer_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_addnew_xpath="//a[@class='btn btn-primary']"
    txt_email_id="Email"
    txt_password_id = "Password"
    txt_firstname_id = "FirstName"
    txt_lastname_id = "LastName"
    rd_male_id="Gender_Male"
    rd_female_id = "Gender_Female"
    txt_dob_id = "DateOfBirth"
    txt_company_name_id = "Company"
    ckhbx_tax_id="IsTaxExempt"
    txt_newsletter_xpath="//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"
    lstitem_yourstorename_xpath='//*[@id="SelectedNewsletterSubscriptionStoreIds_listbox"]/li[1]'
    lstitem_teststore2_xpath='//*[@id="f109ae46-af41-47f7-99d4-8a2d1658bcfb"]'
    txt_customerrole_xpath="//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lstitem_administrators_xpath="//li[normalize-space()='Administrators']"
    lstitem_ForumModerators_xpath = "//li[normalize-space()='Forum Moderators']"
    lstitem_Guests_xpath = "//li[normalize-space()='Guests']"
    lstitem_Registered_xpath = "//li[normalize-space()='Registered']"
    lstitem_ventor_xpath = "//li[@id='2329b335-82f6-415c-b5a7-8d14713ef695']"
    drpdown_vendor_xpath="//select[@id='VendorId']"
    ckhbx_active_xpath="//input[@id='Active']"
    txt_admincomment_xpath="//textarea[@id='AdminComment']"
    btn_save_xpath="//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def click_customer_menu(self):
        self.driver.find_element(By.XPATH,self.link_customer_menu_xpath).click()
    def click_customer(self):
        self.driver.find_element(By.XPATH,self.link_customer_xpath).click()
    def click_addnew(self):
        self.driver.find_element(By.XPATH,self.btn_addnew_xpath).click()
    def set_email(self,email):
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)
    def set_password(self,password):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)
    def set_firstname(self,fname):
        self.driver.find_element(By.ID, self.txt_firstname_id).send_keys(fname)
    def set_lastname(self,lname):
        self.driver.find_element(By.ID, self.txt_lastname_id).send_keys(lname)
    def set_gender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.ID, self.rd_male_id).click()
        elif gender=="Female":
            self.driver.find_element(By.ID, self.rd_female_id).click()
        else:
            self.driver.find_element(By.ID, self.rd_male_id).click()
    def set_DOB(self,dob):
        self.driver.find_element(By.ID, self.txt_dob_id).send_keys(dob)
    def set_companyname(self,companyname):
        self.driver.find_element(By.ID, self.txt_company_name_id).send_keys(companyname)
    def click_tax(self):
        self.driver.find_element(By.ID,self.ckhbx_tax_id).click()
    def set_newsletter(self,store):
        self.driver.find_element(By.XPATH, self.txt_newsletter_xpath).click()
        time.sleep(3)
        if store == "Your store name":
            lstitem1 = self.driver.find_element(By.XPATH, self.lstitem_yourstorename_xpath).click()
        elif store == "Test store 2":
            lstitem1 = self.driver.find_element(By.XPATH, self.lstitem_teststore2_xpath).click()
        else:
            lstitem1 = self.driver.find_element(By.XPATH, self.lstitem_yourstorename_xpath).click()

        self.driver.execute_script("arguments[0].click();", lstitem1)
    def set_customerroll(self, roll):
        self.driver.find_element(By.XPATH, self.txt_customerrole_xpath).click()
        time.sleep(3)
        if roll == "Administrators":
            self.lstitem=self.driver.find_element(By.XPATH, self.lstitem_administrators_xpath).click()
        elif roll == "ForumModerators":
            self.lstitem=self.driver.find_element(By.XPATH, self.lstitem_ForumModerators_xpath).click()
        elif roll == "ventor":
            self.lstitem=self.driver.find_element(By.XPATH, self.lstitem_ventor_xpath).click()
        elif roll == "Registered":
            self.lstitem=self.driver.find_element(By.XPATH, self.lstitem_Registered_xpath).click()
        elif roll == "Guests":
            self.driver.find_element(By.XPATH,"//span[@title='delete']").click()
            self.lstitem=self.driver.find_element(By.XPATH, self.lstitem_Guests_xpath).click()
        else:
            self.driver.find_element(By.XPATH, "//span[@title='delete']").click()
            self.lstitem=self.driver.find_element(By.XPATH, self.lstitem_Guests_xpath).click()
        self.driver.execute_script("arguments[0].click();", self.lstitem)
    def set_mangerofventor(self,text):
        Select(self.driver.find_element(By.XPATH,self.drpdown_vendor_xpath)).select_by_visible_text(text)
    def click_active(self):
        self.driver.find_element(By.XPATH,self.ckhbx_active_xpath).click()
    def set_admincomment(self,comment):
        self.driver.find_element(By.XPATH, self.txt_admincomment_xpath).send_keys(comment)
    def click_save(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()






