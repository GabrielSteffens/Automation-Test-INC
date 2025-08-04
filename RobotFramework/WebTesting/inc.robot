*** Settings ***
Library    SeleniumLibrary
Library    custom_browser.py
Resource    variaveis.robot

*** Variables ***
${URL}    https://inccloud.intelbras.com.br
${BROWSER}    chrome

*** Keywords ***
Abrir o navegador
    Open Browser    browser=${BROWSER} 
    Maximize Browser Window

Fechar o navegador
    Capture Page Screenshot
    Close Browser   

Acessar a home page do site inccloud.intelbras.com.br
    Go To    url=${URL}
    Wait Until Element Is Visible    locator=//p[@class='login-title importantFont']

Preencher Login
    Input Text    locator=//input[@id='name']    text=${USER_INC}
    Sleep    1s

Preencher Senha
    Input Text    locator=//input[@id='password']    text=${PASS_INC}
    Sleep    1s

Marcar o checkbox do User Agreement
    Select Checkbox    locator=//div[@class='mt10']//label[1]//span[1]//input[1]
    Sleep    1s

Clicar em login
    Click Element    locator=loginBtn
    Sleep    5s
Clicar em Sites
    Click Element    locator=//li[@title='Sites']
    Sleep    5s

Ver todos os Sites
    Click Element    locator=//div[@class='sever-content-arrow']//i[@class='ivu-icon ivu-icon-ios-arrow-down']
Selecionar o site
    Click Element    locator=//html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]/a[1]
    Sleep    3s
Clicar em Settings
    Click Element    locator=(//i[@class='ivu-icon ivu-icon-ios-arrow-down ivu-menu-submenu-title-icon'])[4]
Clicar em CloudAPs
    Sleep    2s
    Mouse Over    locator=//li[@data-id='NM.Settings.CloudAPs']//div[@class='menu-dropdown ivu-dropdown']
    Sleep    2s
Clicar em WLAN Settings
    Click Element    locator=//li[normalize-space()='WLAN Settings']
    Sleep    5s
Clicar em Radio Configuration
    Click Element    locator=//a[normalize-space()='Radio Configuration']
    Sleep    2s

Clicar em Edit
    Click Element    locator=(//*[name()='use'])[186]
    Sleep    5s
Clicar em Band
    Click Element    locator=//div[contains(@class,'ivu-select-selection ivu-select-selection-focused')]//div//i[contains(@class,'ivu-icon ivu-icon-ios-arrow-down ivu-select-arrow')]
    Sleep    10s

Clicar em Organization
    Click Element    locator=//li[@title='Organization']
    Sleep    3s

Clicar em pesquisar
    Click Element    locator=//div[contains(@class,'el-table singleTable fixed-columns-roll-style el-table--fit el-table--border el-table--fluid-height el-table--scrollable-x el-table--enable-row-transition')]//div[contains(@class,'el-table__fixed-right')]//div[contains(@class,'el-table__fixed-header-wrapper')]//table[contains(@class,'el-table__header')]//thead//tr//th[contains(@class,'is-leaf')]//div[contains(@class,'cell umy-table-beyond')]//div//i[contains(@class,'ivu-icon ivu-icon-ios-search')]
    Sleep    3s

Preencher nome do site
    Click Element    locator=//div[contains(@class,'el-table singleTable fixed-columns-roll-style el-table--fit el-table--border el-table--fluid-height el-table--scrollable-x el-table--enable-row-transition')]//div[contains(@class,'el-table__fixed-right')]//div[contains(@class,'el-table__fixed-header-wrapper')]//table[contains(@class,'el-table__header')]//thead//tr//th[contains(@class,'is-leaf')]//div[contains(@class,'cell umy-table-beyond')]//div//i[contains(@class,'ivu-icon ivu-icon-ios-search')]
    Sleep    3s
    Input Text    locator=//div[4]//div[1]//table[1]//thead[1]//tr[1]//th[2]//div[1]//div[1]//input[1]   text=${SITE}
    Sleep    3s

Clicar em Wi-Fi Settings
    Click Element    locator=//a[normalize-space()='Wi-Fi Settings']
    Sleep    1s

Criar novo SSID
    [Arguments]    ${SSID}
    Click Element    locator=//div[@id='addService']//button[@type='button']//span//span[contains(text(),'Add')]
    Input Text    locator=//input[@placeholder='Please enter the SSID.']    text=${SSID}
    Input Text    locator=//input[@placeholder='Please enter the SSID.']    text=${SSID}
Selecionar 2.4GHz
    Select Checkbox    locator=(//input[@value='2.4GHz'])[1]
    Sleep    3s
Selecionar 5GHz
    Select Checkbox    locator=(//input[@value='5GHz'])[1]
    Sleep    3s
Colocar Senha SSID
    [Arguments]    ${SENHA}
    Click Element    locator=//label[normalize-space()='PSK']
    Sleep    1s 
    Input Text    locator=//div[@class='v-transfer-dom']//div[12]//div[1]//div[1]//div[1]//input[1]    text=${SENHA}
    Input Text    locator=//div[@class='ivu-form-item ivu-form-item-required']//div[@class='ivu-form-item-content']//div//input[@type='password']    text=${SENHA}
    Sleep    1s 
Colocar VLAN
    [Arguments]    ${vlan}
    Click Element    //input[@placeholder='1-4000']
    Sleep            3s
    Press Keys       //input[@placeholder='1-4000']    CTRL+A
    Sleep            3s
    Press Keys       //input[@placeholder='1-4000']    BACKSPACE
    Sleep            3s
    Input Text       //input[@placeholder='1-4000']    ${vlan}
    Click Element    //div[@class='ivu-modal ivu-modal-fullscreen']//div[@class='ivu-modal-content']//div[@class='ivu-modal-footer']//div//span[contains(text(),'OK')]
    Sleep            10s


Alterar idioma
    Mouse Over    locator=(//*[name()='svg'][@class='_icon_oasis'])[161]
    Sleep    1s
    Mouse Over    locator=(//div[@class='ivu-select-dropdown'])[3]
    Sleep    1s
    Click Element    locator=//li[normalize-space()='English']
    Sleep    5s

