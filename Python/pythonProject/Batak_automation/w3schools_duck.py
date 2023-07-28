from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class Test_selenium:

    def launch_app(self):

        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        time.sleep(2)
    def slide(self):
        MobileElementel1 = (MobileElement1)
        driver.findElementById("com.android.permissioncontroller:id/permission_allow_button");
        el1.click();
        (new TouchAction(driver)).tap(695, 542).perform()
        (new TouchAction(driver))
        .press(PointOption.point(635, 2157}))
        .moveTo(PointOption.point(663, 816}))
        .release() \
            .perform();

        MobileElement
        el2 = (MobileElement)
        driver.findElementById("naukriApp.appModules.login:id/tv_view_all");
        el2.click();

    def batak_ka_requirement(self):
        try:
            driver.get("https://www.w3schools.com/python/")

            driver.implicitly_wait(10)
            element = driver.find_element(By.XPATH, "(//a[text()='Python File Handling'])[1]")
            Actions = ActionChains(driver)
            Actions.move_to_element(element).perform()
            time.sleep(2)
            driver.find_element(By.XPATH, "(//a[text()='Python File Handling'])[1]").click()
            time.sleep(4)
            if driver.find_element(By.XPATH, "(//a[text()='Python File Handling'])[1]").is_displayed():
                print("It is scrolled to the desired link")
            element1 = driver.find_element(By.XPATH, "(//h2[text()='File Handling'])[2]")
            Actions = ActionChains(driver)
            Actions.move_to_element(element1).perform()
            time.sleep(4)
            element2 = driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/div[1]/div[8]/a[2]")
            Actions = ActionChains(driver)
            Actions.move_to_element(element2).perform()
            element2 = driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/div[1]/div[8]/a[2]").click()
            time.sleep(4)


        except:

            print("Something suspicious happened ldki!")


obj = Test_selenium()
obj.launch_app()
obj.batak_ka_requirement()









