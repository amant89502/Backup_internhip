# this is modern for loop syntaxes and it works
*** Settings ***
Documentation       A simple for loop example.
Library  SeleniumLibrary
Library  Collections


*** Variables ***
@{ROBOTS}=      1    2    3    4    5



*** Test Cases ***
Loop over    a list of items and log each of them
    FOR    ${robot}    IN    @{ROBOTS}
        Log to console    ${robot}
    END

