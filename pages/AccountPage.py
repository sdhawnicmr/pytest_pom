from selenium.webdriver.common.by import By


class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    #Locators
    edit_your_account_information_option_link_text = "Edit your account information"

    def dis_msg_account_infor(self):
        return self.driver.find_element(By.LINK_TEXT, self.edit_your_account_information_option_link_text).is_displayed()


