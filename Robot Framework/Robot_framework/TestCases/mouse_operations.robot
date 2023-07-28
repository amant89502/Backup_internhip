*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${var1}=  https://kubernetes.io/
${var2}=  https://www.einfochips.com/company-overview/

*** Test Cases ***
TC_001 execute javascript at runtime
    open browser  ${var2}  Chrome
    Maximize browser window
    #open context menu  (//a[text()='Versions'])[1]
    # context menu is the right clicks
    #double click element  (//a[text()='Documentation'])[1]
    #mouse down  (//a[text()='Documentation'])[1]
    #mouse up  (//a[text()='Documentation'])[1]
    mouse over  (//span[text()='Partnerships'])[1]

    sleep   2
    close browser