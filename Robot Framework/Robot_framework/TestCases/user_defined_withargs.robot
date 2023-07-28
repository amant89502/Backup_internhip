*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/resources1.robot
Documentation  This file is youtube automation for playing video
*** Variables ***
${url}  https://www.youtube.com/
${browser}  Chrome

*** Test Cases *** 
Resource file in robot
    #start browser and Maximize
    [timeout]  30
    start browser and Maximize  ${url}  Chrome
    input text  //input[@id='search']  see you again
    sleep   1
    click element  //button[@id='search-icon-legacy']
    sleep   4
    click element  (//yt-formatted-string[@class='style-scope ytd-video-renderer'])[1]
    sleep   6
    #click element  (//span[@class='ytp-ad-button-icon'])[1]
    sleep   3
    close browser
    

