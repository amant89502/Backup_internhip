import json
import sys
sys.path.append('C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/pythonProject1')
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as Service
from webdriver_manager.chrome import ChromeDriverManager

from webdriver_manager.firefox import GeckoDriverManager
#from TestData import testdata

@pytest.fixture()
def browser(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome()
    request.instance.driver = driver
    driver.maximize_window()
    yield driver

    driver.close()

#
# @pytest.fixture(scope="class")
# def browser_cls(request):
#     print("initiating chrome driver")
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     request.cls.driver = driver
#     driver.maximize_window()
#     yield driver
#     driver.close()
#
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store",help="input browser")
#
# @pytest.fixture()
# def params(request):
#     params ={}
#     params['browser'] = request.config.getoption('--browser')
#     return params
#
# @pytest.fixture()
# def crossbrowsertesting(request, params):
#     print("initiating chrome driver")
#     driver = ""
#     if params["browser"] == 'chrome':
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     if params["browser"] == 'firefox':
#         driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#
#     request.cls.driver = driver
#     driver.maximize_window()
#     yield driver
#     driver.close()
#
# @pytest.fixture()
# def jsonData():
#     with open('TestData/testData.json') as config_file:
#         data = json.load(config_file)
#     return data
#
#
#


