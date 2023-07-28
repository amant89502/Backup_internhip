*** Settings ***
Library  SeleniumLibrary
Library  Collections

*** Test Cases ***
#TC_001 Validate login and logout
   # ${speed}=   get selenium speed
   # log to console  ${speed}
   # open browser  https://www.facebook.com/  Chrome
    #Maximize browser window
    #set selenium speed  3
    #input text  name:email  amant
    #input text  name:pass    1234
    #${speed}=   get selenium speed
    #log to console  ${speed}
    #close browser

#TC_001 sleep
   # open browser  https://www.facebook.com/  Chrome
   # Maximize browser window
    #sleep   3
    #input text  name:email  amant
    #input text  name:pass    1234
    #close browser

TC_002 selenium timeout
    open browser  https://www.facebook.com/  Chrome
    Maximize browser window
    #${tm}=  Get Selenium Page Timeout
    #log to console  ${tm}
    set selenium speed  1
    #wait until page timeout  amant
    input text  name:email  amant
    input text  name:pass    1234
    #capture page screenshot  C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/Robot_framework/TC_1.png
    capture page screenshot  ./Snapshots/TC_2.png
    close browser

    

