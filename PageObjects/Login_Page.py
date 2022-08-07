import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class Loginpage:
    txt_username_id="Email"
    txt_password_id="Password"
    btn_login_xpath="//button[@type='submit']"
    link_logout_xpath="//*[@id='navbarText']/ul/li[3]/a"

    def __init__(self,driver):
       self.driver=driver

    def set_username(self,username):
        self.driver.find_element(By.ID,self.txt_username_id).clear()
        self.driver.find_element(By.ID, self.txt_username_id).send_keys(username)
    def set_password(self,password):
        self.driver.find_element(By.ID,self.txt_password_id).clear()
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)
    def login(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()
    def logout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()
        # mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=None)
        # logout=mywait.until(EC.element_to_be_clickable(self.driver.find_element(By.LINK_TEXT,self.link_logout_linktxt)))
        # logout.click()



