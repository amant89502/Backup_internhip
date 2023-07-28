*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
TC_001 close all browser
    open browser  https://www.facebook.com/  Chrome
    Maximize browser window
    sleep   3
    input text  name:email  amant
    input text  name:pass  1234
    open browser  https://www.google.com/  Chrome
    close all browsers
    
