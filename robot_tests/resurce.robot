*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      http://127.0.0.1:8000/accounts/login/
${REGISTER URL}      http://127.0.0.1:8000/accounts/register/
${BROWSER}        Chrome

*** Test Cases ***
Invalid Login
    Open Browser To Login Page
    Login   example@gmail.com    test
    Login Page Should Remain
    [Teardown]    Close Browser

Invalid Registration
    Open Browser To Register Page
    Set Basic Data     konrad.staszewski@gmail.com   Konrad  Staszewski  password
    Set Additional Data  26.01.1995  Kalisz  rolnik   +48 12 345 6789

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Logowanie

Open Browser To Register Page
    Open Browser    ${REGISTER URL}   ${BROWSER}
    Title Should Be     Arte Laguna

Login
    [Arguments]    ${email}     ${password}
    Input Text     username    ${email}
    Input Text  password  ${password}
    Click Button    login

Set Basic Data
    [Arguments]    ${email}  ${fist_name}   ${last_name}   ${password}
    Input Text  email    ${email}
    Input Text  first_name  ${fist_name}
    Input Text  last_name   ${last_name}   
    Input Text  password  ${password}
    Input Text  password2  ${password}

Set Additional Data
    [Arguments]   ${birthday}   ${placeOfBirth}   ${Alias}  ${phone}
    Input Text  birthday    ${birthday}
    Input Text  place_of_birth  ${placeOfBirth}
    Input Text  alias   ${Alias}
    Input Text  phone_number    ${phone}  

Login Page Should Remain
    Title Should Be    Logowanie