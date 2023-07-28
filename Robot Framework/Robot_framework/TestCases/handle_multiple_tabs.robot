*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${var1}=  https://robotframework.org/

*** Test Cases ***
TC_001 handle multiple tabs
    open browser  ${var1}  Chrome
    Maximize browser window
    click link  //a[text()='Github issues.']
    @{list1}=   get window handles
    : FOR  ${win}  in  @{list1}
    \   log to console  ${win}
    END
    
    sleep   2
    close all browsers