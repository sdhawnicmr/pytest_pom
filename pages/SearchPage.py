from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self,driver):
        # constructor is called automatically when an object is created for the class
        self.driver = driver

    valid_hp_product_link_text = "HP LP3065"
    no_product_found_xpath = "//input[@id='button-search']/following-sibling::p"

    def display_status_of_hp_product(self):
        return self.driver.find_element(By.LINK_TEXT, self.valid_hp_product_link_text).is_displayed()

    def product_not_found_msg(self):
        return self.driver.find_element(By.XPATH,self.no_product_found_xpath).text