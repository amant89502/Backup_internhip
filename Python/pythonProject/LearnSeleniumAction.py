from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from Reusable import common
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains



import time

class test_selenium:

    def launch_app(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        # driver.get("https://www.webucator.com/")
        # driver.get(Common_method.readXmlAsPerNode("appUrl"))
        driver.maximize_window()
        time.sleep(2)
        return self

    def Check_validateBox(self):
        try:
            # driver.get(Common_method.readXmlAsPerNode("https://the-internet.herokuapp.com/checkboxes"))
            driver.get("https://the-internet.herokuapp.com/checkboxes")
            driver.implicitly_wait(10)
            time.sleep(2)
            # validation for 1 check box
            if not driver.find_element(By.XPATH, "(//form[@id='checkboxes']/input)[1]").is_selected():
                print("Checkbox 1 is not selected")
                driver.find_element(By.XPATH, "(//form[@id='checkboxes']/input)[1]").click()
                time.sleep(2)
            else:
                print("Checkbox 1 is selected by default")

            # validation for 2 check box
            if driver.find_element(By.XPATH, "(//form[@id='checkboxes']/input)[2]").is_selected():
                print("Checkbox 2 is selected by default")
                driver.find_element(By.XPATH, "(//form[@id='checkboxes']/input)[2]").click()
            if not driver.find_element(By.XPATH, "(//form[@id='checkboxes']/input)[2]").is_selected():
                print("Checkbox 2 is unchecked pass")
                time.sleep(2)
                time.sleep(2)
            else:
                print("Checkbox 1 is selected by default")
        except:
            print("Something went wrong")

    def close_app(self):
        driver.quit()


    def Sign_in(self):
        driver.get("https://www.webucator.com/account/login/")
        driver.implicitly_wait(10)
        time.sleep(2)
        driver.find_element(By.NAME, "login").click()
        driver.find_element(By.NAME, "login").send_keys(common.resdXMLAsPerNode("email"))
        driver.find_element(By.NAME, "password").click()
        driver.find_element(By.NAME, "password").send_keys(common.resdXMLAsPerNode("password"))
        driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
        time.sleep(3)
        # now clear screen...

        if driver.find_element(By.XPATH, "//strong").text == common.resdXMLAsPerNode("error"):
            #error = driver.find_element(By.XPATH,"//strong").text
            print("The email/password is not correct..pass.. and error is", common.resdXMLAsPerNode("error"))
        else:
            print("Login is accepting invalid id and pass...fail...")


    def Reset(self):
        driver.get("https://www.webucator.com/account/password/reset/")
        driver.implicitly_wait(10)
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[text()]").click()
        time.sleep(3)


    def Footer(self):
        driver.get("https://www.webucator.com/")
        driver.implicitly_wait(10)
        coun = driver.find_elements(By.XPATH, "//footer//h4[text()='About Us']/../ul/li/a")

        print("Total Links are", len(coun))
        for i in coun:
            print(i.text)
        time.sleep(2)

    def Dropdown(self):
        driver.get("https://the-internet.herokuapp.com/dropdown")
        driver.implicitly_wait(10)
        select = Select(driver.find_element(By.ID, 'dropdown'))
        select.select_by_index(2)
        time.sleep(2)

    def Hover(self):
        driver.get("https://www.docker.com/")
        driver.implicitly_wait(10)
        time.sleep(4)
        element = driver.find_element(By.XPATH,"(//a[contains(.,'Developers')])[1]")
        ActionChains(driver).move_to_element(element).perform()
        time.sleep(4)
        driver.find_element(By.XPATH, "(//a[contains(.,'Community')])[1]").click()
        driver.implicitly_wait(7)
        if "community" in driver.current_url:
            print("user went to community page")
        else:
            print("User was not able to go to community page")
        time.sleep(5)

    def Handle_alert(self):

        driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        driver.implicitly_wait(10)
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(.,'Click for JS Alert')]").click()
        time.sleep(2)
        alert = Alert(driver)
        if alert.text == "I am a JS Alert":
            alert.accept()
            time.sleep(1)
            driver.find_element(By.XPATH, "//p[text()='You successfully clicked an alert']").is_displayed()
            print("Click for Js Alert Pass.")
        else:
            print("Click for Js Alert Fail.")

        # Click for Js Confirmation.........
        driver.find_element(By.XPATH, "//button[contains(.,'Click for JS Confirm')]").click()
        time.sleep(2)
        alert = Alert(driver)
        if alert.text == "I am a JS Confirm":
            alert.dismiss()
            time.sleep(2)
            driver.find_element(By.XPATH, "//p[text()='You clicked: Cancel']").is_displayed()
            print("Click for Js confirm pass.")
        else:
            print("Click for Js confirm fail.")

        # Click for Js Confirmation.........
        driver.find_element(By.XPATH, "//button[contains(.,'Click for JS Prompt')]").click()
        time.sleep(2)
        alert = Alert(driver)
        if alert.text == "I am a JS prompt":
            alert.send_keys("Aman Tiwari is my name!")
            alert.accept()
            time.sleep(2)
            ele = driver.find_element(By.XPATH,"//p[text()='You entered: Aman Tiwari is my name!']").is_displayed()
            print("Click for Js Prompt With name pass.", ele)
        else:
            print("Click for Js Prompt With was not successful.")
        time.sleep(3)


    def get_attributes(self):
        driver.get("https://www.docker.com/")
        driver.implicitly_wait(10)
        time.sleep(2)
        ele = driver.find_element(By.XPATH, "//div[@class='os-item downloadable windows-stable']/a")
        print(ele.get_attribute("href"))


    def window(self):
        driver.get("https://www.docker.com/")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//img[@alt='twitter logo']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()

        windows = driver.window_handles
        size = len(windows)
        parent_window = driver.current_window_handle
        for x in range(size):
            if windows[x] != parent_window:
                print(driver.title)
                driver.close()
                time.sleep(3)
                break
        driver.switch_to.window(parent_window)
        print(driver.title)

    def speed_test(self):

        driver.get("https://www.google.com")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//input[@jsaction='paste:puy29d;']").send_keys("Speed Test")
        driver.find_element(By.XPATH, "(//input[@value='Google Search'])[2]").click()
        driver.find_element(By.XPATH, "//div[text()='RUN SPEED TEST']").click()
        time.sleep(20)

    # def custom_test(self):
    #
    #
    #     #driver = webdriver.Firefox(executable_path="C:\geckodriver.exe")
    #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #
    #     driver.get("url")
    #
    #     actions = ActionChains(driver)
    #
    #     actions.send_keys(value="amant89502")
    #
    #     actions.send_keys(keys.TAB)
    #
    #     actions.send_keys(value="hello")
    #
    #     actions.send_keys(keys.ENTER)
    #
    #     actions.perform()
    #
    #     driver.quit()
    def subham_watch(self):
        driver.get("https://www.amazon.in/")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("smart watch for men")
        driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
        ele = driver.find_element(By.XPATH, "(//img[@src='https://m.media-amazon.com/images/I/71e4q6+FZNL._AC_UY218_.jpg'])[1]")
        Actions = ActionChains(driver)
        Actions.move_to_element(ele).perform()
        time.sleep(2)
        ele.click()
        time.sleep(3)
        # for hover
        element = driver.find_element(By.XPATH, "//span[@id='a-autoid-7']")
        ActionChains(driver).move_to_element(element).perform()
        driver.find_element(By.XPATH, "//span[@id='a-autoid-7']").click()
        driver.implicitly_wait(7)
        # driver.get("https://www.docker.com/")
        # driver.implicitly_wait(10)
        # time.sleep(4)
        # element = driver.find_element(By.XPATH, "(//a[contains(.,'Developers')])[1]")
        # ActionChains(driver).move_to_element(element).perform()
        # time.sleep(4)
        # driver.find_element(By.XPATH, "(//a[contains(.,'Community')])[1]").click()
        # driver.implicitly_wait(7)
    def iframe(self):
        driver.get("https://www.amazon.in/")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("smart watch for men")
        # # to get in to the frame..
        # xpath = "//iframe[@id='mce_0_ifr']"
        # self.driver.switch_to.frame("mce_0_ifr")
        # self.driver.find_element(By.XPATH, Xpath).send_keys(text)
        # # to come out of the frame
        # self.driver.switch_to.default_content()

    def self_testing(self):
        driver.get("file:///C:/Users/158173/OneDrive%20-%20Arrow%20Electronics,%20Inc/Desktop/pythonProject4/CSS_LEVEL_ONE/part3.html")
        driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        time.sleep(3)


obj = test_selenium()
print(obj.launch_app())
#print(obj.Check_validateBox())
#print(obj.Sign_in())
#print(obj.close_app())
#print(obj.Reset())
#print(obj.Footer())
#print(obj.Dropdown())
print(obj.Hover())
#print(obj.Handle_alert())
#print(obj.get_attributes())
#print(obj.window())
#print(obj.speed_test())
#print(obj.subham_watch())
#obj.self_testing()










