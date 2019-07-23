*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary
Create Webdriver    Chrome    executable_path=/usr/bin/chromedriver

*** Variables ***
${LOGIN URL}      http://127.0.0.1:8000/accounts/login/
${REGISTER URL}      http://127.0.0.1:8000/accounts/register/
${BROWSER}        Chrome

*** Test Cases ***
Invalid Login
    Open Browser To Login Page
    Input Username    demo
    Input Password    test
    Submit Credentials
    Login Page Should Remain
    [Teardown]    Close Browser

Invalid Registration
    Open Browser To Register Page
    Input Email     konrad.staszewski@gmail.com
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Logowanie

Open Browser To Register Page
    Open Browser    ${REGISTER URL}   ${BROWSER}
    Title Should Be     Arte Laguna

Input Email
    [Arguments]     ${email}
    Input Text     email   ${email}

Input Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Input Password
    [Arguments]     ${password}
    Input Text  password  ${password}

Submit Credentials
    Click Button    login

Login Page Should Remain
    Title Should Be    Logowanie