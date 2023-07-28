*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}=     https://macpaw.com/how-to/remove-bootcamp-mac     

*** Test Cases ***
Validate
    Validate Open browser
    Validate Close browser


*** Keywords ***
Validate Open browser
    open browser    ${url}  Chrome

Validate Close browser
    close browser