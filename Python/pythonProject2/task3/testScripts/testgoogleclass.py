import time
import sys
sys.path.append('C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/pythonProject2')
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from task3.pageObjects.googlehome import Google_Home


class TestGoogleApp:

    def test_google_Logo(self,browser):
        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.get("https://www.google.com/")
        #driver.maximize_window()
        browser.implicitly_wait(10)
        logo=browser.find_elements(By.XPATH,"//img[@class='lnXdpd']")
        assert len(logo)>0
        #driver.quit()


    def test_google_Search(self,browser):
        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.get("https://www.google.com/")
        #driver.maximize_window()
        browser.implicitly_wait(10)
        browser.find_element(By.XPATH,"//textarea[@class='gLFyf']").send_keys("Selenium WebDriver")
        time.sleep(3)
        #driver.quit()

    def test_google_title(self,browser):
        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.get("https://www.google.com/")
        #driver.maximize_window()
        browser.implicitly_wait(10)
        assert browser.title == "Google"
        time.sleep(2)
        #print(driver.title)
        #driver.quit()



