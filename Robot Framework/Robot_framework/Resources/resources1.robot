*** Settings ***
Library  SeleniumLibrary
Library  ../External_keywords/external_keywords.py

*** Variables ***
#${url}  https://www.einfochips.com/company-overview/
#${browser}  Chrome

*** Keywords ***
start browser and Maximize
    [Documentation]  This is resources1 file which is being called to main file for keywords.
    [Arguments]  ${userurl}  ${inputbrowser}
    #open browser  ${url}  ${browser}
    open browser  ${userurl}  ${inputbrowser}
    Maximize browser window
    ${title}=  get title
    log  ${title}
    [return]  ${title}
create folder at runtime
    [Arguments]  ${foldername}  ${subfoldername}
    create_folder  ${foldername}
    create_sub_folder  ${subfoldername}
    log to console  "task successfully done!"
concatenate username and password
    [Arguments]  ${username}  ${password}
    ${result_val}=  concat_two_values  ${username}  ${password}
    log  ${result_val}


