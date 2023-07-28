*** Settings ***
suite setup  before each test suite
suite teardown  after each test suite    

*** Variables ***

*** Keywords ***
before each test suite
    log  test suite Started

after each test suite
    log  test suite ended

