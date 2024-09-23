import time
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        #Homepage.py
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_dd_menu()
        home_page.click_on_login_option()
        time.sleep(3)
        # LoginPage.py
        login_page = LoginPage(self.driver)
        login_page.enter_email_id_box("sdhawnicmr@gmail.com")
        time.sleep(1)
        login_page.enter_password_in_box("12345")
        login_page.login_button_click()
        #AccountPage.py
        account_page = AccountPage(self.driver)
        assert account_page.dis_msg_account_infor()

    def test_login_with_invalid_email_valid_password(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name='email']").send_keys(self.generate_email_timestamp())
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys('12345')
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        expected_warnng_mgs = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_warnng_mgs)

    # generate a new invalid email id everytime
    def test_login_with_valid_email_invalid_password(self):
        #Email_id = "By.XPATH, //input[@name='email']"
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys('sdhawnicmr@gmail.com')
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys('12345987')
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        expected_warnng_mgs = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(
            expected_warnng_mgs)

    def test_login_without_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys('')
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys('')
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        expected_warnng_mgs = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(
            expected_warnng_mgs)

    def generate_email_timestamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "sdhawnicmr" + time_stamp + '@gmail.com'
