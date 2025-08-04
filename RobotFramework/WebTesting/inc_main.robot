*** Settings ***
Documentation     Essa suite utiliza o site INC Cloud
Resource          inc.robot
Variables         variaveis.robot
Test Setup        Abrir o navegador
Test Teardown     Fechar o navegador

*** Test Cases ***
Caso de teste - Criar SSIDs
    [Documentation]    Este teste cria múltiplos SSIDs conforme definido em variaveis.robot

    Acessar a home page do site inccloud.intelbras.com.br
    Preencher Login
    Preencher Senha
    Marcar o checkbox do User Agreement
    Clicar em login
    Alterar idioma
    Clicar em Organization
    Preencher nome do site
    Selecionar o site
    Clicar em Settings
    Clicar em CloudAPs
    Clicar em WLAN Settings
    Clicar em Wi-Fi Settings

    ${total}=     Convert To Integer    ${SSID_COUNT}

    FOR     ${i}    IN RANGE    1    ${total + 1}
        # Acessa as variáveis dinamicamente sem Set Variable e Get Variable Value
        ${ssid}=    Get Variable Value    ${SSID${i}}
        ${senha}=   Get Variable Value    ${SENHA${i}}
        ${freq24}=  Get Variable Value    ${FREQ24_${i}}
        ${freq5}=   Get Variable Value    ${FREQ5_${i}}
        ${vlan}=    Get Variable Value    ${VLAN${i}}

        Log    Criando SSID: ${ssid} - Senha: ${senha} - Freq24: ${freq24} - Freq5: ${freq5} - VLAN: ${vlan}

        Criar novo SSID    ${ssid}
        Run Keyword If    '${freq24}' == 'True'    Selecionar 2.4GHz
        Run Keyword If    '${freq5}' == 'True'     Selecionar 5GHz
        Colocar Senha SSID    ${senha}
        Colocar VLAN    ${vlan}
    END