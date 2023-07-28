from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
#from webdrivermanager import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class Automation:
    def automation_website(self):
        global driver
        driver=webdriver.Chrome()
        driver.get("https://www.tourism.rajasthan.gov.in/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        print(driver.title)
        ele=driver.find_element(By.XPATH,"(//li[@class='has-dropdown'])[1]")
        actions=ActionChains(driver)
        actions.move_to_element(ele).perform()
        time.sleep(2)
        dest=driver.find_element(By.XPATH,"//span[text()='Destinations']")
        actions.move_to_element(dest).perform()
        time.sleep(2)
        l1=[]
        array_dest=driver.find_element(By.XPATH,"//ul[@class='nav-dropdown']").text
        time.sleep(2)
        l1.append(array_dest)
        print("top destinations: ",l1)
        time.sleep(1)
        l2=[]
        museum=driver.find_element(By.XPATH,"//span[text()='Museums']")
        actions.move_to_element(museum).perform()
        time.sleep(2)
        text=driver.find_element(By.XPATH,"//ul[@class='nav-dropdown']").text
        l2.append(text)
        print("top museums: ",l2)

    def codeforces(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://codeforces.com/contest/1672")
        driver.maximize_window()
        driver.implicitly_wait(5)
        time.sleep(2)
        # l3=[]
        # elems=driver.find_elements(By.TAG_NAME,'a')
        # for elem in elems:
        #     href=elem.get_attribute("href")
        #     print(href)
        # ele=driver.find_elements(By.TAG_NAME,'a')
        # for i in ele:
        #     text=i.text
        #     print(text)
        list1 = []
        #driver.get("https://codeforces.com/contest/1672")
        c = driver.find_elements(By.XPATH, "//tr//td[2]//a")
        for i in range(len(c)):
            list1.append(c[i].get_attribute("href"))

        print(list1)



obj=Automation()
#obj.automation_website()
obj.codeforces()