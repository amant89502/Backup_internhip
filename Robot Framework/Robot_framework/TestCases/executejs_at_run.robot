*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${var1}=  https://www.facebook.com

*** Test Cases ***
TC_001 execute javascript at runtime
    open browser  ${var1}  Chrome
    Maximize browser window
    execute javascript  window.scrollTo(0,1000)
    # it is used to scroll down the browser through javascript
    sleep   3
    close browser