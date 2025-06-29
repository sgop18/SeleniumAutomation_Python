import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver = webdriver.Chrome()  # ✅ Instantiate the Chrome driver properly
    elif browser =="edge":
        driver = webdriver.Edge()  # ✅ Instantiate the Chrome driver properly
    else:
        driver=webdriver.Chrome() #default launch chrome
    yield driver
    driver.quit()  # ✅ Quit the driver properly
    
    
def pytest_addoption(parser): #This will get the browser value from the browser
    parser.addoption("--browser")
    
@pytest.fixture()    
def browser(request):
    return request.config.getoption("--browser") #This will pass the browser value to the setup method








#Original without browser input from command line 
# @pytest.yield_fixture()
# def setup():
#     driver = webdriver.Chrome()  # ✅ Instantiate the Chrome driver properly
#     yield driver
#     driver.quit()  # ✅ Quit the driver properly
