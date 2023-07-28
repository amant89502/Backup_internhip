import time

from selenium.webdriver.common.by import By
import pytest

class Google_Home:
    def __init__(self,driver):
        self.driver =driver

    def launch_app_with_url(self,url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    def google_logo_validation(self,Xpath):
        # click Text box tab
        print(self.driver.title)
        Xpath =self.driver.find_elements(By.XPATH,Xpath)
        assert  len(Xpath)>0
    def google_search_type(self,Xpath,text):
        self.driver.find_element(By.XPATH,Xpath).send_keys(text)
        time.sleep(5)
    def validate_google_title(self,title):
        assert self.driver.title==title

# @pytest.mark.regression
#     def test_google_Search(self):
#         obj1 = exam_home(self.driver)
#         obj1.launch_app_with_url("https://www.google.com/")
#         obj1.google_search_type(examlocators.google_search_text_box(),"Selenium WebDriver")
#
#     @pytest.mark.regression
#     def test_google_title(self):
#         obj1 = exam_home(self.driver)
#         obj1.launch_app_with_url("https://www.google.com/")
#         obj1.validate_google_title("Google")