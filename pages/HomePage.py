from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        # constructor is called automatically when an object is created for the class
        self.driver = driver

    #locators for Homepage elements
    search_box_field_name = "search"
    search_button_xpath = "//button[@class='btn btn-default btn-lg']"
    my_account_drop_menu_xpath = "//span[text()='My Account']"
    login_option_link_text= "Login"

    def enter_product_in_search_box(self, product_name):
        self.driver.find_element(By.NAME, self.search_box_field_name).click()
        self.driver.find_element(By.NAME, self.search_box_field_name).clear()
        self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product_name)

    def click_on_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()

    def click_on_my_account_dd_menu(self):
        self.driver.find_element(By.XPATH, self.my_account_drop_menu_xpath).click()

    def click_on_login_option(self):
        self.driver.find_element(By.LINK_TEXT, self.login_option_link_text).click()