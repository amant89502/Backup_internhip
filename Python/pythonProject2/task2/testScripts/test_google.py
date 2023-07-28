import time
import sys
sys.path.append('C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/pythonProject2')
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_google_Logo():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    logo=driver.find_elements(By.XPATH, "//img[@id='hplogo']")
    assert len(logo) > 0
    driver.quit()


def test_google_Search():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@name='q']").send_keys("Selenium WebDriver")
    # driver.switch_to.frame("")
    # driver.switch_to.default_content()
    time.sleep(3)
    driver.quit()

def test_google_title():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    assert driver.title == "Google"
    time.sleep(2)
    #print(driver.title)
    driver.quit()



