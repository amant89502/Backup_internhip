*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${var1}=  https://www.einfochips.com/company-overview/
${var2}=  https://www.google.com/


*** Test Cases ***
TC_001 execute multiple browser
    open browser  ${var1}  Chrome
    Maximize browser window
    open browser  ${var2}  Chrome
    Maximize browser window
    switch browser  1
    ${url1}=  get location
    log to console  ${url1}
    switch browser  2
    ${url2}=  get location
    log to console  ${url2}

     
    sleep   2
    close all browsers