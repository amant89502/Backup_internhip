import time

from selenium.webdriver.common.by import By

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
    def heroku_frame(self,Xpath,text):
        #to get in to the frame..
        self.driver.switch_to.frame("mce_0_ifr")
        self.driver.find_element(By.XPATH, Xpath).clear()
        self.driver.find_element(By.XPATH,Xpath).send_keys(text)
        time.sleep(5)
        # to come out of the frame
        self.driver.switch_to.default_content()
        time.sleep(5)
