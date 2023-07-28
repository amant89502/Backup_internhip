*** Settings ***
Library  SeleniumLibrary 
Resource  ../../Resources/resources1.robot


*** Variables ***
${url}  https://the-internet.herokuapp.com/dropdown
${browser}  Chrome

*** Test Cases ***
Robot fetch data
    concatenate username and password  testing  world
    open browser  ${url}  ${browser}
    Maximize browser window
    set selenium speed  1
    #select from list by index  //select[@id='dropdown']  1
    #${val}=  get selected list label  //select[@id='dropdown']
    #log to console  ${val}
    #${all_list}=  get list items  //select[@id='dropdown']
    #log to console  ${all_list}
    #${actual_url}=  get location
   # log to console  ${actual_url}
   # ${page_html}=  get source
   # log  ${page_html}
    #${element_attribute}=  get element attribute  //select[@id='dropdown']  id
    #log  ${element_attribute} 
    #${cnt}=  get element count  id:dropdown
    #log  ${cnt} 
    close browser

    


    
    

