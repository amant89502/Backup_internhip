*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${var1}=  https://www.einfochips.com/company-overview/
${var2}=  https://formstone.it/components/checkbox/

*** Test Cases ***
TC_001 validations
    open browser  ${var1}  Chrome
    Maximize browser window
    #page should contain  Services
    #page should not contain  Services:
    #click element  (//span[text()='Contact Us'])[1]
    #page should contain element  //input[@placeholder='Full Name*']
    #input text  //input[@placeholder='Full Name*']  amant
    #checkbox should be selected  //input[@id='checkbox-1']
    #click element  //input[@id='checkbox-2']
    #element should contains  //div[@id='text-block-6']  eInfochips, an Arrow company, is a leading global provider of product engineering and semiconductor design services. With over 500+ products developed and 40M deployments in 140 countries, eInfochips continues to fuel technological innovations in multiple verticals. The company’s service offerings include digital transformation and connected IoT solutions across various cloud platforms, including AWS and Azure.
    title should be  Corporate Overviews
    sleep   4
    close all browsers