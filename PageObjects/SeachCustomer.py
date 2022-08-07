

from selenium.webdriver.common.by import By


class Search_Customer:
    txt_email_id = "SearchEmail"
    txt_firstname_id = "SearchFirstName"
    txt_lastname_id = "SearchLastName"
    btn_search_id = "search-customers"
    tbl_row_xpath = "//table[@id='customers-grid']/tbody/tr"
    tbl_column_xpath = "//table[@id='customers-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def set_firstname(self, fname):
        self.driver.find_element(By.ID, self.txt_firstname_id).clear()
        self.driver.find_element(By.ID, self.txt_firstname_id).send_keys(fname)

    def set_lasttname(self, lname):
        self.driver.find_element(By.ID, self.txt_lastname_id).clear()
        self.driver.find_element(By.ID, self.txt_lastname_id).send_keys(lname)

    def set_email(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).clear()
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def search_by_name(self, name):
        self.rows = self.driver.find_elements(By.XPATH, self.tbl_row_xpath)
        flag = False
        for r in range(1, len(self.rows)+1):
            column = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if name in column:
                flag = True
        return flag

    def search_by_email(self, email):
        self.rows = self.driver.find_elements(By.XPATH, self.tbl_row_xpath)
        flag = False
        for r in range(1, len(self.rows)+1):
            column = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
            if column == email:
                flag = True
        return flag

    def click_search(self):
        self.driver.find_element(By.ID, self.btn_search_id).click()
