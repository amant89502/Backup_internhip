from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from Reusable import common
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

class test_selenium:

    def launch_app(self):

        #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        global driver
        #options = Options()
        #options.add_argument("--headless")
        driver = webdriver.Chrome()
        #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        #driver.get(common.resdXMLAsPerNode("URL"))
        #driver.implicitly_wait(10)
        driver.maximize_window()
        time.sleep(2)

    def capture_screenshot(self):
        try:
            driver.get("https://kubernetes.io/")
            driver.implicitly_wait(10)
            if driver.find_element(By.XPATH, "(//a[@class='navbar-brand img-fluid'])[2]").is_displayed():
                print("Kubernates logo is present")
                driver.save_screenshot(
                    "C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/pythonProject/fail_ss/logo.png")
                time.sleep(3)
        except:
            driver.save_screenshot("C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/pythonProject/fail_ss/logo.png")
            print("Kubernates logo is not present!")

    def drop_down(self):

        driver.get("https://www.pizzahut.co.in/")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,"//input[@placeholder='Enter your location for delivery']").send_keys("Gorakhpur")
        time.sleep(5)
        if driver.find_element(By.XPATH,"//div[@class='pt-5 border-t overflow-scrolling-touch']//button[1]").is_displayed():
            driver.find_element(By.XPATH, "//div[@class='pt-5 border-t overflow-scrolling-touch']//button[1]").click()
        print("Find Pizza")
        time.sleep(2)

        driver.implicitly_wait(10)

        def scroll(self):

            try:
                driver.get("https://kubernetes.io/")
                driver.implicitly_wait(10)
                if driver.find_element(By.XPATH,"(//a[text()='Case Studies'])[2]").is_displayed():
                    driver.find_element(By.XPATH,"(//a[text()='Case Studies'])[2]").location_once_scrolled_into_view
                    time.sleep(4)
                    driver.find_element(By.XPATH,"(//a[text()='Case Studies'])[2]").click()
                    time.sleep(3)
            except:
                print("hello")

    def scroll_click(self):
        try:
            driver.get("https://kubernetes.io/")

            driver.implicitly_wait(10)

            if driver.find_element(By.XPATH, "(//a[text()='Case Studies'])[2]").is_displayed():
                driver.find_element(By.XPATH, "(//a[text()='Case Studies'])[2]").location_once_scrolled_into_view
                time.sleep(2)
                driver.find_element(By.XPATH, "(//a[text()='Case Studies'])[2]").click()
                time.sleep(3)
            time.sleep(2)

        except:
            print("error")

    def right_click(self):
        try:
            driver.get("https://kubernetes.io/")
            driver.implicitly_wait(10)
            logo = driver.find_element(By.XPATH,"(//a[@class='navbar-brand img-fluid'])[1]")
            if logo.is_displayed():
                actionChains=ActionChains(driver)
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
                actionChains.double_click(logo).perform()
                time.sleep(3)
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

    def close_app(self):
        driver.quit()
    def upload_image(self):
        driver.get("https://the-internet.herokuapp.com/upload")
        driver.implicitly_wait(10)
        time.sleep(3)
        driver.find_element(By.XPATH,"// input[ @ id = 'file-upload']").send_keys("C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/pythonProject/fail_ss/logo.png")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@value='Upload']").click()
        time.sleep(7)

    def English_drop(self):
      # driver.get("https://kubernetes.io/")
       # driver.implicitly_wait(10)
        #driver.find_element(By.XPATH,"//a[@id='navbarDropdownMenuLink']").click()
        #time.sleep(3)
        #ele = driver.find_element(By.XPATH, "//div[@class='dropdown-menu dropdown-menu-right show']").text
        #print(ele)
        #driver.implicitly_wait(10)
        #time.sleep(2)
        driver.get("https://kubernetes.io/")
        driver.implicitly_wait(10)
        time.sleep(3)
        for i in range(1, 14):
            xpath = "(//div[@class='dropdown-menu dropdown-menu-right show']/a)[" + str(i) + "]"
            lang_name = driver.find_element(By.XPATH, xpath).text
            print(lang_name, " --> ", driver.find_element(By.XPATH, xpath).get_attribute("href"))

    def kubernet_HeaderMenu1(self):
        try:
            driver.get("https://kubernetes.io/")
            driver.implicitly_wait(10)
            head_menu = common.resdXMLAsPerNode('HeaderMenu').split(',')
            print(head_menu)
            for i in head_menu:
                if not driver.find_element(By.XPATH, "//ul[@class='navbar-nav mt-2 mt-lg-0']/li/a[text()='" + i + "']"):
                    print("Menu is not their", i)
                    break
                else:
                    print("Kubernetes Menu validate successfully")
                # links=driver.find_elements(By.XPATH, "//ul[@class='navbar-nav mt-2 mt-lg-0']/li/a")
                # for i in links:
                # if not i.text in head_menu:
                # print("Menu is not in header")
                # break
                # print("Menu is their",i.text)
        except:
            print('somthing went wrong')

    def self_practice(self):
        driver.get("https://kubernetes.io/community/")
        driver.implicitly_wait(10)
        time.sleep(3)
        driver.find_element(By.XPATH,"//a[text()='announcement']").click()
        a = driver.current_url
        print(a)


    def Google_css(self):
        driver.get("https://www.google.com/")
        driver.implicitly_wait(10)
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, "input.gLFyf").send_keys("Aman Tiwari")
        time.sleep(3)


    def Google_css1(self):
        driver.get("https://www.google.com/")
        driver.implicitly_wait(10)
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, "input.gLFyf[name=q]").send_keys("Aman Tiwari")
        time.sleep(3)

    def read_book_html(self, bookname, whattoread):
        driver.get("https://intranet.einfochips.com/employee_intranet/portal/user/dashboard")

        driver.implicitly_wait(10)
        value = "null"
        driver.find_element(By.XPATH,"//a[text()='Holiday List']").click()
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
    def makemytrip(self):
        driver.get("https://www.makemytrip.com/")
        driver.implicitly_wait(10)
        if driver.find_element(By.XPATH,"//span[@class='ic_circularclose_grey']").is_displayed():
            driver.find_element(By.XPATH,"//span[@class='ic_circularclose_grey']").click()

        #driver.find_element(By.XPATH,"//img[@src='https://promos.makemytrip.com/notification/xhdpi/900x590-ATW-Roadbloack-050623.jpg']").click()

        driver.find_element(By.XPATH,"(//span[@class='tabsCircle appendRight5'])[2]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"(//span[@class='lbl_input  appendBottom10'])[1]").click()
        #time.sleep(1)
        driver.find_element(By.XPATH,"//input[@placeholder='From']").send_keys("Chennai")
        time.sleep(2)
        driver.find_element(By.XPATH,"//p[text()='Chennai, India']").click()
        #time.sleep(1)
        driver.find_element(By.XPATH,"//span[text()='To']").click()
        #time.sleep(1)
        driver.find_element(By.XPATH,"//input[@placeholder='To']").send_keys("Ahmedabad")
        time.sleep(1)
        driver.find_element(By.XPATH,"(//p[@class='font14 appendBottom5 blackText'])[1]").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"(//p[text()='15'])[1]").click()
        time.sleep(1)

        element3 = driver.find_element(By.XPATH,"(//p[text()='19'])[1]")
        ActionChains(driver).move_to_element(element3).perform()
        time.sleep(2)

        driver.find_element(By.XPATH, "(//p[text()='19'])[1]").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//p[text()='Armed Forces ']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//a[text()='Search']").click()
        time.sleep(11)
        if driver.find_element(By.XPATH,"//button[text()='OKAY, GOT IT!']").is_displayed():
            driver.find_element(By.XPATH,"//button[text()='OKAY, GOT IT!']").click()
        time.sleep(3)

        # en = driver.find_element_by_xpath("//div[@class='rangeslider rangeslider-horizontal']")
        # move = ActionChains(driver)
        # move.click_and_hold(en).move_by_offset(10, 5).release().perform()
        # time.sleep(5)

        # move.click_and_hold(en).move_by_offset(10, 0).release().perform()
        # time.sleep(5)
        #
        # move.click_and_hold(en).move_by_offset(10, 0).release().perform()
        # time.sleep(5)

        # element = driver.find_element(By.XPATH, "(//p[contains(.,'Vistara ')])")
        # ActionChains(driver).move_to_element(element).perform()
        # time.sleep(2)
        driver.find_element(By.XPATH,"(//p[contains(.,'Vistara ')])").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[@class='splitFooterButton button buttonPrimary buttonBig appendBottom8 ']").click()
        time.sleep(10)

        driver.find_element(By.XPATH,"//button[text()='Book Now']").click()
        #driver.switch_to.alert.accept()

        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//button[@class='addBtn'])[1]")))
        driver.find_element(By.XPATH, "(//button[@class='addBtn'])[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//div[@class='baglistItem relative']//span[text()='Additional 5 KG']/../following-sibling::div//span[@class='qtyActions']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//button[text()='DONE']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@class='baglistItem relative']//span[text()='Additional 5 KG']/../following-sibling::div//span[@class='qtyActions']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[text()='DONE']").click()
        time.sleep(1)
        element2 = driver.find_element(By.XPATH, "//div[@class='claimSection']//div[@class='slider-control-centerright']/button[@aria-label='next']")
        ActionChains(driver).move_to_element(element2).perform()
        time.sleep(2)
        for i in range (3):
            driver.find_element(By.XPATH,"//div[@class='insuaranceDeals']//div[@class='slider-control-centerright']/button[@aria-label='next']").click()
            time.sleep(2)








    def taskjp_mmt(self):
        Faretype = "Armed Forces "
        driver.get("https://www.makemytrip.com/")
        driver.implicitly_wait(10)

        # driver.find_element(By.XPATH,"//img[@src='https://promos.makemytrip.com/notification/xhdpi/900x590-ATW-Roadbloack-050623.jpg']").click()
        # round trip button
        driver.find_element(By.XPATH, "(//span[@class='tabsCircle appendRight5'])[2]").click()
        time.sleep(2)
        # from button
        driver.find_element(By.ID, "fromCity").click()
        # time.sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='From']").send_keys("Chennai")
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[text()='Chennai, India']").click()
        # time.sleep(1)
        driver.find_element(By.XPATH, "//span[text()='To']").click()
        # time.sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='To']").send_keys("Ahmedabad")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//p[@class='font14 appendBottom5 blackText'])[1]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//p[text()='16'])[1]").click()
        time.sleep(1)

        element3 = driver.find_element(By.XPATH, "(//p[text()='21'])[1]")
        ActionChains(driver).move_to_element(element3).perform()
        time.sleep(2)

        driver.find_element(By.XPATH, "(//p[text()='21'])[1]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//p[text()='"+Faretype+"']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[text()='Search']").click()
        time.sleep(11)
        if driver.find_element(By.XPATH, "//button[text()='OKAY, GOT IT!']").is_displayed():
            driver.find_element(By.XPATH, "//button[text()='OKAY, GOT IT!']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//p[contains(.,'IndiGo')]").click()
        time.sleep(4)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        e=len(driver.find_elements(By.XPATH,"//div[@class='listingCard ']//font[text()='"+Faretype.strip().upper()+"']"))
        print("No of armed forces flights are",e)


    def flights(self):
        global webdriver
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(
            "https://www.makemytrip.com/flight/reviewDetails/?itineraryId=a7d8c32b0b9c69dd8a20bce18087702e2b3ea815&crId=cac86830-417a-4fa6-84b7-8b49bb5a85a3&cur=INR&rKey=RKEY:dd78ac84-13e1-41f2-91f4-63b659076d10:3_0~~~RKEY:dd78ac84-13e1-41f2-91f4-63b659076d10:30_0&ccde=IN&xflt=eyJjIjoiRSIsInAiOiJBLTFfQy0wX0ktMCIsInQiOiIiLCJzIjoiTUFBLUFNRC0yMDIzMDYxNSRBTUQtTUFBLTIwMjMwNjE5In0=")
        driver.find_element(By.XPATH, "(//button[@class='addBtn'])[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//span[text()='Additional 5 KG']/../following-sibling::div/p[@class='qtyCounter textCenter']/span[@class='qtyActions']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[@class='bgProperties icon20 overlayCrossIcon']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//div[@class='slider-control-centerright'])[1]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//div[@class='slider-control-centerright'])[1]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//div[@class='slider-control-centerright'])[1]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "(//b[text()=' ₹ 2,000 '])[1]").click()
        time.sleep(3)










obj = test_selenium()
obj.launch_app()
#print(obj.test_cases())
#print(obj.close_app())
#print(obj.capture_screenshot())
#print(obj.drop_down())
#print(obj.scroll_click())
#print(obj.right_click())
#print(obj.Double_click())
#print(obj.Kubernet_HeaderMenu())
#print(obj.Validate_Kubernet_HeadeMenu())
#print(obj.upload_image())
#print(obj.English_drop())
#print(obj.self_practice())
#print(obj.Kubernet_HeaderMenu1())
#print(obj.Google_css1())
#obj.self_testing()
#print(obj.read_book_html("Learn Selenium","Author"))
#obj.makemytrip()
#obj.scroll_mmt()
obj.taskjp_mmt()
#obj.flights()
obj.close_app()








