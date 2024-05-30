*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library    SeleniumLibrary
Library    Resource/Library/send_mail.py
Library    Resource/Library/captcha_solver.py
Library    Resource/Library/get_credentials.py

Suite Setup    Setup WebDriver
Suite Teardown    Close All Browsers

*** Variables ***
${LOGIN_URL}         https://carings.wcd.gov.in/Parents/PAPslogin.aspx
${CHILDREN_AVL_URL}     https://carings.wcd.gov.in/parents/TempIP_NormalChild.aspx
${DASHBOARD_URL}    https://carings.wcd.gov.in/Parents/papdshboard.aspx
${LOGOUT_URL}    https://carings.wcd.gov.in/parents/PapLogout.aspx
${SCREENSHOT_PATH}   ${CURDIR}/children_details.png
${CAPTCHA_PATH}   ${CURDIR}/captcha.png

*** Test Cases ***
Login To Dashboard
    [Tags]    test:retry(2)
    Go To    ${LOGIN_URL}
    Sleep    5
    Capture Page Screenshot    ${CAPTCHA_PATH}
    ${USERNAME}  ${PASSWORD}=    Run Keyword    Load Credentials
    Sleep    1
    Input Text    id=ContentPlaceHolder1_txtuserid    ${USERNAME}
    Sleep    1
    Input Text    id=ContentPlaceHolder1_txtpassword    ${PASSWORD}
    Sleep    1
    ${CAPTCHA_TEXT}=    Run Keyword    Call Captcha Solver    ${CAPTCHA_PATH}
    Log    "Captcha text is ${CAPTCHA_TEXT}"
    Input Text    id=ContentPlaceHolder1_txtsecpin    ${CAPTCHA_TEXT}
    Sleep    1
    Click Button    css:input[type="submit"]
    Wait Until Element Contains    xpath://*[text()="Dashboard"]    Dashboard    20
    Log    Logged In successfully

Check For Updates And Send Email
    [Documentation]    Check the dashboard for updates and send a screenshot via email.
    Go To    ${CHILDREN_AVL_URL}
    Sleep    3
    Capture Page Screenshot    ${SCREENSHOT_PATH}
    Run Keyword    send_email    ${SCREENSHOT_PATH}
    Log    Got Child details

Logout Cara
    [Tags]    test:retry(2)
    Scroll Element Into View    css:[href="../parents/PapLogout.aspx"]
    Sleep    2
    Execute Javascript    document.querySelector('[href="../parents/PapLogout.aspx"]').click();
    Sleep    3
    Wait Until Element Contains    xpath://*[text()="Go to Home page"]    Go to Home page    20
    Log    Logged Out successfully

*** Keywords ***
Setup WebDriver
    Create Webdriver    Chrome
    Maximize Browser Window

Call Captcha Solver
    [Arguments]    ${CAPTCHA_PATH}
    ${TEXT}=    solve_captcha    ${CAPTCHA_PATH}
    RETURN    ${TEXT}

Get Cara Credentials
    [Arguments]    ${USERNAME}    ${PASSWORD}
    ${USERNAME}  ${PASSWORD}=    load_credentials
    RETURN    ${USERNAME}    ${PASSWORD}
