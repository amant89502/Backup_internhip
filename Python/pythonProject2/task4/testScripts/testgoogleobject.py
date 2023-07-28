import time
import sys
sys.path.append('C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/pythonProject2')
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from task4.pageObjects.googleHome import Google_Home
from task4.Locators import googlelocators

@pytest.mark.usefixtures("browser_cls")
class TestGoogleApp:
        @pytest.mark.smoke
    def test_google_Logo(self):
        obj1=Google_Home(self.driver)
        obj1.launch_app_with_url("https://www.google.com/")
        obj1.google_logo_validation(googlelocators.google_logo())

    @pytest.mark.regression
    def test_google_Search(self):
        obj1 = Google_Home(self.driver)
        obj1.launch_app_with_url("https://www.google.com/")
        obj1.google_search_type(googlelocators.google_search_text_box(),"Selenium WebDriver")

    @pytest.mark.regression
    def test_google_title(self):
        obj1 = Google_Home(self.driver)
        obj1.launch_app_with_url("https://www.google.com/")
        obj1.validate_google_title("Google")




