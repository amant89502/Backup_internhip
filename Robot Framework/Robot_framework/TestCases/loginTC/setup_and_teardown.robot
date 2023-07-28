*** Settings ***
Library  SeleniumLibrary
Resource  ../../Resources/resources2.robot
Documentation  This file is for facebook login 
test setup  Start browser and Maximize
test teardown  close browser window    
# here, test setup and teardown applies to all test Cases
suite setup  before each test suite
suite teardown  after each test suite
default tags  deft
force tags  all_tc

*** Variables ***
${url}  https://www.youtube.com/
${browser}  Chrome

*** Test Cases ***
Resource file in robot
    #[tags]  smoke
    #[setup]  Start browser and Maximize
    set selenium speed  2
    #[teardown]  close browser window
    input text  name:email  amant89502@gmail.com
    input text  name:pass  0987654

Resource next test Case
    [tags]  smoke  sanity  testing
    #[setup]  Start browser and Maximize
    #[teardown]  close browser window
    click element  name:login
    
    

