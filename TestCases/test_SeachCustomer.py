import time

import pytest

from PageObjects.SeachCustomer import Search_Customer
from PageObjects.Addcustomer import Addcustomer
from PageObjects.Login_Page import Loginpage
# from Utilities.customlogger import loggen
from Utilities.readproperties import Readconfig


class Test_004_SearchCustomer:
    baseurl = Readconfig.get_url()
    username = Readconfig.get_username()
    password = Readconfig.get_password()

    @pytest.mark.sanity
    def test_by_name(self, setup):
        driver = setup
        driver.get(self.baseurl)
        lp = Loginpage(driver)
        ac = Addcustomer(driver)
        sc = Search_Customer(driver)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.login()
        ac.click_customer_menu()
        ac.click_customer()
        sc.set_firstname("Victoria")
        sc.click_search()
        time.sleep(3)
        status = sc.search_by_name("Victoria")
        assert True == status

    def test_byemail(self, setup):
        driver = setup
        driver.get(self.baseurl)
        lp = Loginpage(driver)
        ac = Addcustomer(driver)
        sc = Search_Customer(driver)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.login()
        ac.click_customer_menu()
        ac.click_customer()
        sc.set_email("brenda_lindgren@nopCommerce.com")
        time.sleep(3)
        sc.click_search()
        status = sc.search_by_email("brenda_lindgren@nopCommerce.com")
        assert True == status
        driver.quit()
