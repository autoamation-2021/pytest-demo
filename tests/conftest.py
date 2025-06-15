import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome")

@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    options = Options()
    driver = None

    print(f"Setting up {browser} driver")

    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()

    elif browser == "firefox":
        driver = webdriver.Firefox()    

    driver.implicitly_wait(10)

    yield driver
    print(f"Tear down {browser}")
    driver.quit()    
