import random
import string
import time

from selenium.webdriver.common.by import By

from PageObjects.Login_Page import Loginpage
from PageObjects.Addcustomer import Addcustomer
from Utilities.readproperties import Readconfig
from Utilities.customlogger import loggen


class Test_003_AddCustomer:
    baseurl = Readconfig.get_url()
    username = Readconfig.get_username()
    password = Readconfig.get_password()
    logger = loggen.loggen()

    def test_addcustomer(self, setup):
        self.logger.info("********************Test_003_AddCustomer************************")
        driver = setup
        driver.get(self.baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)
        lp = Loginpage(driver)
        ac = Addcustomer(driver)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.login()
        self.logger.info("******************Login is successful**************************")
        time.sleep(3)
        self.logger.info("*******************Providing customer info*************************")
        ac.click_customer_menu()
        ac.click_customer()
        ac.click_addnew()
        email = random_generator() + "@gmail.com"
        ac.set_email(email)
        ac.set_password("admin")
        ac.set_firstname("gogulan")
        ac.set_lastname("M")
        ac.set_gender("Male")
        ac.set_DOB("07/01/1995")
        ac.set_companyname("gogulan shop")
        ac.click_tax()
        # ac.set_newsletter("hi")
        # ac.set_customerroll("Administrators")
        # ac.set_customerroll("Registered")
        ac.set_customerroll("Guests")
        ac.set_mangerofventor("Vendor 1")
        ac.click_active()
        ac.set_admincomment("This is for testing")
        ac.click_save()
        self.logger.info("********************Saving customer info************************")
        msg = driver.find_element(By.TAG_NAME, "body").text
        self.logger.info("******************Add customer Validation is started **************************")
        if "The new customer has been added successfully." in msg:
            driver.quit()
            self.logger.info("*****************Customer info added successfully ***************************")
            assert True
        else:
            driver.save_screenshot("ScreenShoots/test_Addcustomer.png")
            self.logger.error("********************Customer info adding fail************************")
            driver.quit()

            assert False
        self.logger.info("********************Ending Test_003_AddCustomer************************")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
