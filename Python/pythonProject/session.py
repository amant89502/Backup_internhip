from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.webucator.com/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"SIGN IN").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"SIGN IN").click()
time.sleep(2)
