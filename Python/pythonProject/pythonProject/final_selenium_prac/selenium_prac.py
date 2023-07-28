from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

import time

class test_selenium:

    def launch_app(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        time.sleep(2)

    def close_app(self):
        driver.quit()

    def Dropdown(self):
        driver.get("https://the-internet.herokuapp.com/dropdown")
        driver.implicitly_wait(10)
        select = Select(driver.find_element(By.ID, 'dropdown'))
        select.select_by_index(1)
        time.sleep(2)

    def download_file(self):
        driver.get("https://the-internet.herokuapp.com/")
        driver.implicitly_wait(7)
        driver.find_element(By.XPATH,"//a[text()='File Download']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//a[text()='Waterfall1.JPG']").click()
        time.sleep(50)

    def drag_and_drop(self):
        driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        driver.implicitly_wait(7)
        actionChains = ActionChains(driver)
        # a=driver.find_element(By.XPATH,"//div[@id='column-a']")
        # b=driver.find_element(By.XPATH,"//div[@id='column-b']")
        a = driver.find_element_by_id("draggable")
        b = driver.find_element_by_id("droppable")

        actionChains.drag_and_drop(b,a).perform()
        time.sleep(4)

    def fork_validation(self):
        driver.get("https://the-internet.herokuapp.com/")
        driver.implicitly_wait(7)
        if driver.find_element(By.XPATH,"//img[@alt='Fork me on GitHub']").is_displayed():
            print("ok")

    def rajasthan_selenium(self):
        driver.get("https://www.tourism.rajasthan.gov.in/")
        driver.implicitly_wait(7)
        # it will print top List of tourist destination..........
        touristlist = []
        driver.find_element(By.XPATH, "//li[@class='has-dropdown']/a[text()='Discover']").click()
        time.sleep(4)
        ele = driver.find_element(By.XPATH, "//li[@id='destinations']")
        ActionChains(driver).move_to_element(ele).perform()
        time.sleep(3)
        des =driver.find_elements(By.XPATH, "//li[@id='destinations']//ul//li/a/span")
        len_destination = len(des)
        print(len_destination)
        i = 1
        while i <= len_destination:
            el = driver.find_element(By.XPATH, "(//li[@id='destinations']//ul//li/a/span)['" + str(i) + "']").text

        # time.sleep(1)

            touristlist.append(el)

            print(touristlist)

        # it will print top muesuem list.........
        museumlist = []

        driver.find_element(By.XPATH, "//li[@class='has-dropdown']/a[text()='Discover']").click()

        time.sleep(4)

        ele = driver.find_element(By.XPATH, "//li[@id='museums']")

        ActionChains(driver).move_to_element(ele).perform()

        time.sleep(3)

        mueseum = driver.find_elements(By.XPATH, "//li[@id='museums']//ul//li/a/span")

        len_museum_lst = len(mueseum)

        print(len_museum_lst)

        i = 1

        while i <= len_museum_lst:
            el = driver.find_element(By.XPATH, "(//li[@id='museums']//ul//li/a/span)['" + str(i) + "']").text

            # time.sleep(1)

            museumlist.append(el)

        print(museumlist)








obj = test_selenium()
obj.launch_app()
#obj.Dropdown()
#obj.download_file()
#obj.drag_and_drop()
#obj.fork_validation()
obj.rajasthan_selenium()
obj.close_app()
