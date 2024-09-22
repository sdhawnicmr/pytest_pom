from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    #locators for login pages
    email_field_xpath= "//input[@name='email']"
    password_field_xpath = "//input[@name='password']"
    login_button_xpath ="//input[@type='submit']"

    def enter_email_id_box(self, email_id):
        self.driver.find_element(By.XPATH, self.email_field_xpath).click()
        self.driver.find_element(By.XPATH, self.email_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_field_xpath).send_keys(email_id)

    def enter_password_in_box(self,password):
        self.driver.find_element(By.XPATH, self.password_field_xpath).click()
        self.driver.find_element(By.XPATH, self.password_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_field_xpath).send_keys(password)

    def login_button_click(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()