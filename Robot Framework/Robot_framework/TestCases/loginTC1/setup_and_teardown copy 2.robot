*** Settings ***
#test setup  Start browser and Maximize
#test teardown  close browser window  
Library  SeleniumLibrary 


*** Variables ***
${url}  https://www.youtube.com/
${browser}  Chrome

*** Test Cases ***
Robot fetch data

    open browser  https://www.facebook.com/  ${browser}
    Maximize browser window
    ${page_title}=  get title
    log to console  ${page_title}
    ${speed}=  get selenium speed
    log to console  ${speed}
    ${value}=  get value  //button[@name='login']
    log to console  ${value}
    #${text}=  get text  //a[@class='_8esh']
    #log to console  ${text}  
    close browser
    


    
    

