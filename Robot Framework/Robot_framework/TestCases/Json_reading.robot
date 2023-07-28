*** Settings ***
Library  SeleniumLibrary
Library  ../External_keywords/locators.py

*** Variables ***
${browser}  Chrome
${url}      https://www.facebook.com/
#${url1}     https://www.keynotesupport.com/internet/web-contact-form-example-radio-buttons.shtml
#${url2}     https://the-internet.herokuapp.com/

*** Test Cases ***
Robot first test Case

    set selenium speed  1
    Open browser  ${url}  ${browser}
    Maximize browser window
    ${username}=  Real Element locators  Registration.username_textbox_email
    Input Text  name:${username}  9790784254
    ${password}=  Real Element locators  Registration.password_textbox
    Input Text  name:${password}  Amantiw123@
    Clear Element Text  name:${username}
    Clear Element Text  name:${password}
    #Click Element  name:login
    Close browser

#Robot second test Case
    
    #Open browser  ${url1}  ${browser}
    #Maximize browser window
    #Select radio button  software  Excel
    #Close browser

#Robot third test Case
    
   # Open browser  ${url2}  ${browser}
    #sleep   2
    #Click Element  //a[text()='File Upload']
    #sleep   3
    #Input text  //input[@id='file-upload']  C:/Users/158173/OneDrive - Arrow Electronics, Inc/Pictures/ProfilePicFormal_1.png
   # Click Element  //input[@type='submit']
    #sleep   3
    #close browser

*** Keywords ***

Real Element locators
    [Arguments]  ${JsonPath}
    ${result}=  read_locators_from_json  ${JsonPath}
    [return]  ${result}

