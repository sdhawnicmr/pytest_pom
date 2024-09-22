import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utilities import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic info","browser") #(section, key)
    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome()
        # service = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        print("Provide valid browser name")
        return None

    app_url = ReadConfigurations.read_configuration("basic info","url")
    driver.get(app_url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()