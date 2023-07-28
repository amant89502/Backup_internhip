*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${browser}  Chrome
${url}  https://www.facebook.com/
${url1}  https://www.keynotesupport.com/internet/web-contact-form-example-radio-buttons.shtml
${url2}  https://the-internet.herokuapp.com/
${url3}  https://practicetestautomation.com/practice-test-login/
*** Test Cases ***
#Robot first test Case facebook
    #Open browser  ${url}  ${browser}
    #Maximize browser window
    #Input Text  name:email  9790784254
    #Input Text  name:pass  Amantiw123@
    #Clear Element Text  name:email
    #Clear Element Text  name:pass
    #Click Element  name:login
    #Close browser

#Robot second test Case radiobutton
    #Open browser  ${url1}  ${browser}
    #Maximize browser window
    #Select radio button  software  Excel
    #Close browser

#Robot third test Case file upload
    #Open browser  ${url2}  ${browser}
    #sleep   2
    #Click Element  //a[text()='File Upload']
    #sleep   3
    #Input text  //input[@id='file-upload']  C:/Users/158173/OneDrive - Arrow Electronics, Inc/Pictures/ProfilePicFormal_1.png
    #Click Element  //input[@type='submit']
    #sleep   3
    #close browser

#Robot fourth test Case Checkboxes  
    #Open browser  ${url2}  ${browser}
    #sleep   3
   # Click Element  //a[text()='Checkboxes']
    #sleep   4
    #Click Element  (//input[@type='checkbox'])[1]
    #sleep   2
    #Click Element   (//input[@type='checkbox'])[2]
    #sleep   2
    #close browser

#Robot fifth test case dropdown or list
   # Open browser  ${url2}  ${browser}
   # sleep   2
   # Click Element  //a[text()='Dropdown']
    #set selenium speed 2seconds
    #Select from list by index  id:dropdown  2
    #Select from list by value  id:dropdown  2
    #Select from list by label  id:dropdown  Option 2
    #sleep   3
    #close browser

Robot sixth test case keywords login
    Open browser  ${url3}  ${browser}
    Enter username password
    
    close browser

*** Keywords ***
Enter username password
    Input Text  //input[@id='username']  amant
    Input Text  //input[@id='password']  98711
    sleep   3



