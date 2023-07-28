import json
import time
import sys

sys.path.append('C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/pythonProject2')
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

# appium



@pytest.fixture()
def browser(request):
    print("initial chrome driver")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.instance.driver = driver
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def browser_cls(request):
    print("initial chrome driver")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver = driver
    driver.maximize_window()

    yield driver
    driver.quit()
@pytest.fixture()
def browser(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.instance.driver = driver
    driver.maximize_window()
    yield driver

    driver.close()


@pytest.fixture(scope="class")
def browser_cls(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.cls.driver = driver
    driver.maximize_window()
    yield driver
    driver.close()



def pytest_addoption(parser):
    parser.addoption("--browser", action="store",help="input browser")

@pytest.fixture()
def params(request):
    params ={}
    params['browser'] = request.config.getoption('--browser')
    return params

@pytest.fixture()
def crossbrowsertesting(request, params):
    print("initiating chrome driver")
    driver = ""
    if params["browser"] == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    if params["browser"] == 'firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    request.cls.driver = driver
    driver.maximize_window()
    yield driver
    driver.close()

@pytest.fixture()
def jsonData():
    with open('C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/pythonProject2/task4/testData/testjsondata.json') as config_file:
        data = json.load(config_file)
    return data

