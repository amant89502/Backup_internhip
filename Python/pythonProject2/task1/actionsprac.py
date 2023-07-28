from selenium.webdriver.chrome.service import Service as Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from reusable import common
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager



import time
class test_selenium:
    def launch_app(self):
        global driver
        driver = webdriver.Chrome(Service(ChromeDriverManager().install()))
        driver.implicitly_wait(10)
        #driver.get("https://www.webucator.com/")
        #driver.get(common.resdXMLAsPerNode("URL"))
        driver.maximize_window()
        time.sleep(2)
        return self

    def Check_validateBox(self):
        try:
            #driver.get(common.readXmlAsPerNode("https://the-internet.herokuapp.com/checkboxes"))
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
            # error = driver.find_element(By.XPATH,"//strong").text
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
        time.sleep(3)
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
            print("Click for Js Prompt With name pass.",ele)
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
        driver.get("https://docker.com")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
        driver.find_element(By.XPATH, "//img[@alt='twitter logo']").click()
        time.sleep(5)
        # get the count of window...
        windows = driver.window_handles
        size = len(windows)
        parent_window = driver.current_window_handle
        for x in range(size):
            if windows[x] != parent_window:
                driver.switch_to.window(windows[x])
                print(driver.title)
                driver.close()
                time.sleep(3)
                break
        # moving back to parent window
        driver.switch_to.window(parent_window)
        print(driver.title)
    def capture_screenshot(self):
        try:
            driver.get("https://kubernetes.io/")
            driver.implicitly_wait(10)
            if driver.find_element(By.XPATH, "(//a[@class='navbar-brand img-flui'])[2]").is_displayed():
                print("Kubernates logo is present")
                driver.save_screenshot(
                    "C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/pythonProject/fail_ss/logo.png")
                time.sleep(3)
        except:
            driver.save_screenshot("C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/pythonProject2/task1/fail_ss/logo.png")
            print("Kubernates logo is not present!")

    def selectdropdown(self):
        try:
            driver.get("https://www.pizzahut.co.in/")
            driver.implicitly_wait(5)

    # Type Address in Address Search Box ...
            time.sleep(5)
            try:
                if driver.find_element(By.XPATH, "//button[@data-testid='close-offer-collection']").is_displayed():
                    driver.find_element(By.XPATH, "//button[@data-testid='close-offer-collection']").click()
            except:
                print("Preselect option is not available....")

            if driver.find_element(By.XPATH, "//input[@placeholder='Enter your location for delivery']").is_displayed():
                driver.find_element(By.XPATH, "//input[@placeholder='Enter your location for delivery']").send_keys(
                    "Lulu mall bangalore")
                time.sleep(3)
                if driver.find_element(By.XPATH, "//div[text()='Lulu Mall Bengaluru']").is_displayed():
                    driver.find_element(By.XPATH, "//div[text()='Lulu Mall Bengaluru']").click()
                    if driver.find_element(By.XPATH, "//button[@data-testid='close-offer-collection']").is_displayed():
                        print("User successfully selected the Auto Select drop down option....")
            time.sleep(3)
        except:
            driver.save_screenshot("/Users/mithunroy/PycharmProjects/simplePythonSelenium/FailScreenShot/addressSelection.png")
            print("User is unable to select the Pizza address ....")

    def scroll_to_view_then_click(self):
        try:
            driver.get("https://kubernetes.io/")

            driver.implicitly_wait(10)
            # if driver.find_element(By.XPATH,"(//a[text()='Case Studies'])[2]").is_displayed():
            # driver.find_element(By.XPATH, "(//a[text()='Case Studies'])[2]").location_once_scrolled_into_view
            # time.sleep(3)
            #
            # driver.find_element(By.XPATH, "(//a[text()='Case Studies'])[2]").click()
            # time.sleep(3)
            ele = driver.find_element(By.XPATH, "(//a[text()='Case Studies'])[2]")
            Actions = ActionChains(driver)
            Actions.move_to_element(ele).perform()
            time.sleep(2)
            ele.click()
            time.sleep(3)
        except:
            print("done")
    def right_click(self):
        try:
            driver.get("https://kubernetes.io/")
            driver.implicitly_wait(10)
            logo = driver.find_element(By.XPATH,"(//a[@class='navbar-brand img-fluid'])[1]")
            if logo.is_displayed():
                actionChains = ActionChains(driver)
                actionChains.context_click(logo).perform()
                time.sleep(3)
        except:
            print("error")
    def Double_click(self):
        try:
            driver.get("https://kubernetes.io/")
            driver.implicitly_wait(10)
            logo = driver.find_element(By.XPATH,"(//a[@class='navbar-brand img-fluid'])[1]")
            if logo.is_displayed():
                actionChains = ActionChains(driver)
                if actionChains.double_click(logo).perform():
                    time.sleep(3)
                    print("It is done")
        except:
            print("error")
    def Kubernet_HeaderMenu(self):
        list_of_header = common.resdXMLAsPerNode("HeaderMenu")
        value = list_of_header.split(",")
        for i in value:
            print(i)
    def Validate_Kubernet_HeadeMenu(self):
        driver.get("https://kubernetes.io/")
        driver.implicitly_wait(10)
        list_of_header = common.resdXMLAsPerNode("HeaderMenu")
        value = list_of_header.split(",")
        for i in value:
            try:
                if driver.find_element(By.XPATH,"//ul[@class='navbar-nav mt-2 mt-lg-0']//a[text()='" + i + "']").is_displayed():
                    print("Header Got .........>>", i)

            except:
                print("Header Not Found!!")
    def upload_image(self):
        driver.get("https://the-internet.herokuapp.com/upload")
        driver.implicitly_wait(10)
        time.sleep(3)
        driver.find_element(By.XPATH,"// input[ @ id = 'file-upload']").send_keys("C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/pythonProject/fail_ss/logo.png")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@value='Upload']").click()
        time.sleep(7)
    def English_drop(self):
        driver.get("https://kubernetes.io/")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,"//a[@id='navbarDropdownMenuLink']").click()
        time.sleep(3)
        ele = driver.find_element(By.XPATH, "//div[@class='dropdown-menu dropdown-menu-right show']").text
        print(ele)
        driver.implicitly_wait(10)
        #time.sleep(2)
        # driver.get("https://kubernetes.io/")
        # driver.implicitly_wait(10)
        # time.sleep(3)
        for i in range(1, 14):
            xpath = "(//div[@class='dropdown-menu dropdown-menu-right show']/a)[" + str(i) + "]"
            lang_name = driver.find_element(By.XPATH, xpath).text
            print(lang_name, " --> ", driver.find_element(By.XPATH, xpath).get_attribute("href"))

    def read_book_html(self, bookname, whattoread):
        driver.get("https://testautomationpractice.blogspot.com/")

        driver.implicitly_wait(10)
        value = "null"
        if whattoread == "Author":
            value = driver.find_element(By.XPATH,
                                        "//table[@name='BookTable']/tbody/tr/td[text()='" + bookname + "']/../td[2]").text
        if whattoread == "Subject":
            value = driver.find_element(By.XPATH,
                                        "//table[@name='BookTable']/tbody/tr/td[text()='" + bookname + "']/../td[3]").text
        if whattoread == "Price":
            value = driver.find_element(By.XPATH,
                                        "//table[@name='BookTable']/tbody/tr/td[text()='" + bookname + "']/../td[4]").text
        return value

    def Google_css(self):
        driver.get("https://www.google.com/")
        driver.implicitly_wait(10)
        #time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, "input.gLFyf").send_keys("Aman Tiwari")
        driver.find_element(By.CSS_SELECTOR, "input.gLFyf[name=q]").send_keys("Aman")
        driver.find_element(By.CSS_SELECTOR, "input[name=q]").send_keys("Aman")

        time.sleep(3)

    def chatgpt(self):
        driver.get("https://chat.openai.com/chat")
        driver.implicitly_wait(10)
        #if driver.find_element(By.XPATH,"//input[@type='checkbox']").is_displayed():
        # driver.find_element(By.XPATH,"//span[@class='mark']").click()



        # driver.find_element(By.CSS_SELECTOR, "input.gLFyf").send_keys("Aman Tiwari")
        # driver.find_element(By.CSS_SELECTOR, "input.gLFyf[name=q]").send_keys("Aman")
        # driver.find_element(By.CSS_SELECTOR, "input[name=q]").send_keys("Aman")

        time.sleep(200)


obj = test_selenium()
obj.launch_app()
#print(obj.Check_validateBox())
#print(obj.Sign_in())
#print(obj.Reset())
#print(obj.Footer())
#print(obj.Dropdown())
#print(obj.Hover())
#print(obj.Handle_alert())
#print(obj.get_attributes())
#print(obj.window())
#print(obj.capture_screenshot())
#print(obj.selectdropdown())
#print(obj.scroll_to_view_then_click())
#print(obj.right_click())
#print(obj.Double_click())
print(obj.Kubernet_HeaderMenu())
#print(obj.Validate_Kubernet_HeadeMenu())
#pri#nt(obj.upload_image())
#print(obj.English_drop())
#rint(obj.read_book_html("Learn Java","Author"))
#obj.Google_css()
#print(obj.eInfochips())
#obj.chatgpt()
#obj.close_app()




