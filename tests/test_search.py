import time
import pytest
from selenium.webdriver.common.by import By
from pages.HomePage import HomePage
from pages.Searchpage import SearchPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_valid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_in_search_box("HP")
        home_page.click_on_button()
        search_page = SearchPage(self.driver)
        assert search_page.display_status_of_hp_product()
        time.sleep(2)
        print(self.driver.title)

    def test_search_for_invalid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_in_search_box("Honda")
        home_page.click_on_button()
        expected_text = "There is no product that matches the search criteria."
        search_page = SearchPage(self.driver)
        assert search_page.product_not_found_msg() == expected_text
        time.sleep(2)
        print(self.driver.title)

    def test_search_without_any_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_in_search_box("")
        home_page.click_on_button()
        search_page = SearchPage(self.driver)
        expected_text = "There is no product that matches the search criteria."
        assert search_page.product_not_found_msg().__eq__(expected_text)
        time.sleep(2)
        print(self.driver.title)
