*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library    SeleniumLibrary
Library    Resource/Library/send_mail.py

Suite Setup    Create webdriver    Chrome
Suite Teardown    Close All Browsers

*** Variables ***
${LOGIN_URL}         https://practicetestautomation.com/practice-test-login/
${DASHBOARD_URL}     https://practicetestautomation.com/logged-in-successfully/
${USERNAME}          student
${PASSWORD}          Password123
${SCREENSHOT_PATH}   ${CURDIR}/screenshot.png

*** Test Cases ***
Login To Dashboard
    Open Browser        ${LOGIN_URL}    Chrome
    Maximize Browser Window
    Input Text    id=username    ${USERNAME}
    Input Text    id=password    ${PASSWORD}
    Click Button    id=submit

Check For Updates And Send Email
    [Documentation]    Check the dashboard for updates and send a screenshot via email.
    Go To    ${DASHBOARD_URL}
    Sleep    5s  # Wait for the page to load
    Capture Page Screenshot    ${SCREENSHOT_PATH}
    Run Keyword    send_email    ${SCREENSHOT_PATH}

*** Keywords ***
Setup WebDriver
    Create WebDriver    chrome
    Maximize Browser Window
