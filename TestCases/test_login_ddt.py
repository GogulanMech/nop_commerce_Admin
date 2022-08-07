import time

from selenium import webdriver
import pytest
from PageObjects.Login_Page import Loginpage
from Utilities.readproperties import Readconfig
from Utilities.customlogger import loggen
from Utilities import Goexcelmodule
class Test_002_login:
    baseurl=Readconfig.get_url()
    path="TestData/nop_ddt_login_data.xlsx"
    logger=loggen.loggen()

    def test_login_ddt(self,setup):
        self.logger.info("*******************Test_002_login_DDT***********************")
        self.logger.info("*******************Verifying Home Title ***********************")
        self.driver = setup
        self.driver.get(self.baseurl)
        # self.driver.maximize_window()
        lp=Loginpage(self.driver)
        rows = Goexcelmodule.get_row_count(self.path, "Sheet1")
        lst_status=[]
        for r in range(2, rows + 1):
            username = Goexcelmodule.readdata(self.path, "Sheet1",r,1)
            password = Goexcelmodule.readdata(self.path, "Sheet1", r, 2)
            expt = Goexcelmodule.readdata(self.path, "Sheet1", r, 3)
            exp_title = "Dashboard / nopCommerce administration"
            lp.set_username(username)
            lp.set_password(password)
            lp.login()
            act_title = self.driver.title
            time.sleep(5)
            if exp_title==act_title:
                if expt=="pass":
                    time.sleep(30)
                    lp.logout()
                    self.logger.info("******************* DDT test1 is pass***********************")
                    lst_status.append("pass")
                elif expt=="fail":
                    time.sleep(30)
                    lp.logout()
                    self.driver.save_screenshot("ScreenShoots\\test_loginDDT1.png")
                    self.logger.error("******************* DDT test1 is fail***********************")
                    lst_status.append("fail")
            elif exp_title !=act_title:
                if expt=="fail":
                    self.logger.info("******************* DDT test2 is pass***********************")
                    lst_status.append("pass")
                else:
                    self.driver.save_screenshot("ScreenShoots\\test_loginDDT2.png")
                    self.logger.error("******************* DDT test2 is fail***********************")
                    lst_status.append("fail")
        if "fail" not in lst_status:
            self.driver.quit()
            self.logger.info("*******************Login DDT test is passed***********************")
            assert True
        else:
            self.driver.quit()
            self.logger.error("*****************login DDT test is failed*************************")
            assert False

        self.logger.info("*****************End of login DDT test*************************")
        self.logger.info("*****************Completed Test_002_login_DDT*************************")



