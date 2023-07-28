*** Settings ***
Library  SeleniumLibrary

*** Variables ***
#${url}  https://www.einfochips.com/company-overview/
#${browser}  Chrome

*** Keywords ***
Start browser and Maximize
    open browser  https://www.facebook.com/  Chrome
    Maximize browser window
close browser window
    ${title}=  get title
    log to console  ${title}
    close browser


before each test suite
    log to console  before exectuting the test suite

after each test suite
    log to console  after exectuting the test suite
