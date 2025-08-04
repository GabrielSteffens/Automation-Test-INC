# Automation-Test

Visão Geral do Projeto
Este projeto em Robot Framework foi desenvolvido para automatizar a criação e configuração de múltiplos SSIDs (Service Set Identifiers) na plataforma INC Cloud da Intelbras. Ele foi projetado para otimizar o processo de provisionamento de redes Wi-Fi, permitindo a criação em massa de SSIDs com configurações personalizadas de nome, senha, frequência (2.4GHz e 5GHz) e VLANs.
A grande novidade é a inclusão de uma Interface Gráfica do Usuário (GUI) desenvolvida em Python com PySide6. Esta GUI facilita a entrada de dados (credenciais, nome do site e configurações de múltiplos SSIDs) de forma interativa, eliminando a necessidade de edição manual do arquivo de variáveis. Após a inserção dos dados, a GUI gera o arquivo de variáveis (variaveis.robot) e executa a automação do Robot Framework.

Funcionalidades
- Interface Gráfica Amigável (GUI): Permite a entrada de credenciais do INC Cloud, nome do site e detalhes de múltiplos SSIDs de forma intuitiva.
- Criação Dinâmica de Variáveis: A GUI gera automaticamente o arquivo variaveis.robot com base nas informações fornecidas pelo usuário.
- Autenticação Automatizada: Realiza login na plataforma INC Cloud.
- Seleção de Organização e Site: Navega até a organização e o site específicos para a configuração.
- Criação Dinâmica de SSIDs: Itera sobre uma lista de dados de SSIDs (agora gerados pela GUI) e cria cada um deles.
- Configuração Detalhada por SSID:
- Definição do nome do SSID.
- Atribuição de senha (PSK).
- Seleção de bandas de frequência (2.4GHz, 5GHz ou ambas).
- Associação a VLANs específicas.
- Controle de Idioma: Ajusta o idioma da interface para Inglês para consistência.
- Execução Integrada: A GUI aciona a execução do script Robot Framework após a coleta e salvamento dos dados.

Pré-requisitos:
Certifique-se de ter os seguintes softwares instalados em sua máquina:
- Python 3.x: Link para Download do Python
- pip: Gerenciador de pacotes do Python (geralmente vem com o Python).
- Robot Framework: Uma suíte de automação genérica de código aberto.
- SeleniumLibrary: Biblioteca do Robot Framework para automação web.
- PySide6: Biblioteca Python para criação da GUI.
- ChromeDriver: O driver do navegador Chrome compatível com a sua versão do Chrome. Baixe e coloque-o em um local acessível pelo PATH do sistema, ou na pasta raiz do projeto. Link para ChromeDriver

Para rodar este projeto de automação, siga os passos abaixo:
- Primeiro, clone este repositório para sua máquina local usando o Git:
git clone https://github.com/GabrielSteffens/Automation-Test-INC
cd Automation-Test

- Configurar o Ambiente Virtual (Recomendado)

- python -m venv venv

No Windows:
- .\venv\Scripts\activate

No macOS/Linux:
- source venv/bin/activate

Com o ambiente virtual ativado, instale as bibliotecas necessárias:
pip install robotframework robotframework-seleniumlibrary PySide6

A execução da automação agora começa pela interface gráfica. Abra seu terminal ou prompt de comando na raiz do projeto e execute o script interface.py:
python interface.py

Configurar e Executar via GUI:
- Uma janela de "Configurar SSIDs e Executar Teste" será aberta.
- Preencha os campos de Usuário do INC, Senha do INC e Site.
- Selecione a Quantidade de SSIDs desejada no dropdown. Campos adicionais para cada SSID (Nome, Senha, Frequência 2.4GHz/5GHz e VLAN) aparecerão dinamicamente.
- Preencha os detalhes para cada SSID.
- Clique no botão "Salvar e Executar".
- A GUI irá salvar as informações no arquivo variaveis.robot e, em seguida, iniciará a execução da automação do Robot Framework. Uma mensagem de sucesso ou erro será exibida na GUI ao final do processo.

Estrutura do Projeto:
- interface.py: O script Python que fornece a Interface Gráfica do Usuário (GUI) para coletar os dados de entrada e acionar a automação.
- main.robot: Contém o caso de teste principal (Caso de teste - Criar SSIDs) e a orquestração das keywords.
- inc.robot: Define todas as keywords de interação com a interface web da INC Cloud (cliques, preenchimento de campos, esperas, etc.).
- variaveis.robot: Este arquivo é gerado/atualizado automaticamente pela GUI (interface.py) com base nas informações fornecidas pelo usuário. Ele armazena as variáveis configuráveis do projeto, como credenciais de login, nome do site e os dados de cada SSID a ser criado.
