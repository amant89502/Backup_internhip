*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${var1}=  https://www.facebook.com

*** Test Cases ***
TC_001 goto and go back
    open browser  ${var1}  Chrome
    go to  https://www.google.com  
    ${url1}=    get location
    log to console  ${url1}
    go back
    ${url2}=    get location
    log to console  ${url2}
    # it clicks back button on browser
    close browser