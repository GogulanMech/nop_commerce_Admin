from selenium import webdriver
import pytest
from PageObjects.Login_Page import Loginpage
from Utilities.readproperties import Readconfig
from Utilities.customlogger import loggen
class Test_001_login:
    baseurl= Readconfig.get_url()
    username=Readconfig.get_username()
    password=Readconfig.get_password()
    logger=loggen.loggen()

    def test_homepage_title(self,setup):
        self.logger.info("*******************Test_001_login***********************")
        self.logger.info("*******************Verifying Home Title ***********************")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        act_title=self.driver.title
        self.driver.quit()
        if act_title=="Your store. Login":
            assert True
            self.logger.info("*****************Home page test is passed*************************")
        else:
            self.driver.save_screenshot("ScreenShoots\\test_homepage_title.png")
            self.logger.error("*****************Home page test is failed*************************")
            assert False


    def test_login(self,setup):
        self.logger.info("*******************Verifying Login test***********************")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        lp=Loginpage(self.driver)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.login()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            # lp.logout()
            assert True
            self.logger.info("*******************Login test is passed***********************")
            self.driver.quit()

        else:
            self.driver.save_screenshot("ScreenShoots\\test_login.png")
            self.driver.quit()
            self.logger.error("*****************login test is failed*************************")
            assert False




