*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${var1}=  https://www.einfochips.com/company-overview/


*** Test Cases ***
TC_001 execute javascript at runtime
    open browser  ${var1}  Chrome
    Maximize browser window
    #wait until page contains  Domains
    #wait until page contains element  (//span[text()='Domains'])[1]
    wait until element contains  (//span[text()='Domains'])[1]  Domains
    click element  (//span[text()='Domains'])[1]  

    sleep   2
    close browser