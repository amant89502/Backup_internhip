*** Settings ***
Library  SeleniumLibrary
Library  Collections
*** Variables ***

*** Test Cases ***
TC_001 Variables test
    @{List}=    Create List     ${1}    ${2}    ${3}
    FOR   ${i}    IN  ${List}
        log to console  ${i}
    END

*** Keywords ***


