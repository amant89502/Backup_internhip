*** Settings ***
Library  SeleniumLibrary
Resource  ../../Resources/resources2.robot
*** Variables ***
*** Test Cases ***
Test case in bdd format
    given Start browser and Maximize
    when close browser window
    then before each test suite
