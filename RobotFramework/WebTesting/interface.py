import sys
import subprocess
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox, QComboBox,
    QGroupBox, QHBoxLayout, QCheckBox, QScrollArea
)
from PySide6.QtGui import QFont, QIntValidator
from PySide6.QtCore import Qt


class SSIDConfigurator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configurar SSIDs e Executar Teste")
        self.setFixedSize(420, 600)
        self.setStyleSheet("background-color: #00a335; color: white;")

        self.font_label = QFont("Arial", 10, QFont.Bold)
        self.font_input = QFont("Arial", 10)

        layout = QVBoxLayout()

        # Usuário do INC
        label_user = QLabel("Usuário do INC:")
        label_user.setFont(self.font_label)
        self.input_user = QLineEdit()
        self.input_user.setFont(self.font_input)
        self.input_user.setStyleSheet("background-color: #ffffff; color: black;")  # Fundo branco
        layout.addWidget(label_user)
        layout.addWidget(self.input_user)

        # Senha do INC
        label_pass = QLabel("Senha do INC:")
        label_pass.setFont(self.font_label)
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.Password)
        self.input_pass.setFont(self.font_input)
        self.input_pass.setStyleSheet("background-color: #ffffff; color: black;")  # Fundo branco
        layout.addWidget(label_pass)
        layout.addWidget(self.input_pass)

        # Site
        label_site = QLabel("Site:")
        label_site.setFont(self.font_label)
        self.input_site = QLineEdit()
        self.input_site.setFont(self.font_input)
        self.input_site.setStyleSheet("background-color: #ffffff; color: black;")  # Fundo branco
        layout.addWidget(label_site)
        layout.addWidget(self.input_site)

        # Quantidade de SSIDs
        label_qtd = QLabel("Quantidade de SSIDs:")
        label_qtd.setFont(self.font_label)
        layout.addWidget(label_qtd)

        self.combo_ssid_qtd = QComboBox()
        self.combo_ssid_qtd.addItems(["1", "2", "3"])
        self.combo_ssid_qtd.setFont(self.font_input)
        self.combo_ssid_qtd.currentIndexChanged.connect(self.gerar_campos_ssids)
        layout.addWidget(self.combo_ssid_qtd)

        # Área de rolagem
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.ssid_area = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)
        layout.addWidget(self.scroll_area)

        # Botão principal
        self.botao = QPushButton("Salvar e Executar")
        self.botao.setFont(QFont("Arial", 10, QFont.Bold))
        self.botao.clicked.connect(self.salvar_e_executar)
        layout.addWidget(self.botao)

        self.setLayout(layout)
        self.gerar_campos_ssids()

    def gerar_campos_ssids(self):
        while self.ssid_area.count():
            item = self.ssid_area.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        self.ssid_fields = []

        quantidade = int(self.combo_ssid_qtd.currentText())
        for i in range(quantidade):
            group = QGroupBox(f"SSID {i + 1}")
            group.setStyleSheet("""
                QGroupBox {
                    background-color: #00863F;
                    color: white;
                    border-radius: 5px;
                    margin-top: 5px;
                    padding: 5px;
                }
                QLabel {
                    color: white;
                }
                QLineEdit {
                    background-color: #ffffff;
                    color: black;
                    border: 1px solid #444;
                    padding: 4px;
                }
                QCheckBox {
                    color: white;
                }
            """)
            group_layout = QVBoxLayout()

            # Nome do SSID
            label_nome = QLabel("Nome do SSID:")
            label_nome.setFont(self.font_label)
            label_nome.setStyleSheet("background-color: #00863F; color: white;")  # Fundo verde escuro

            input_nome = QLineEdit()
            input_nome.setFont(self.font_input)
            input_nome.setStyleSheet("background-color: #ffffff; color: black;")  # Campo branco

            # Frequências
            check_24 = QCheckBox("2.4GHz")
            check_24.setStyleSheet("background-color: #00863F; color: white;")  # Fundo verde escuro

            check_5 = QCheckBox("5GHz")
            check_5.setStyleSheet("background-color: #00863F; color: white;")  # Fundo verde escuro

            freq_layout = QHBoxLayout()
            freq_layout.addWidget(check_24)
            freq_layout.addWidget(check_5)

            # Senha do SSID
            label_senha = QLabel("Senha do SSID:")
            label_senha.setFont(self.font_label)
            label_senha.setStyleSheet("background-color: #00863F; color: white;")  # Fundo verde escuro

            input_senha = QLineEdit()
            input_senha.setEchoMode(QLineEdit.Password)
            input_senha.setFont(self.font_input)
            input_senha.setStyleSheet("background-color: #ffffff; color: black;")  # Campo branco

            # VLAN
            label_vlan = QLabel("VLAN:")
            label_vlan.setFont(self.font_label)
            label_vlan.setStyleSheet("background-color: #00863F; color: white;")  # Fundo verde escuro

            input_vlan = QLineEdit()
            input_vlan.setFont(self.font_input)
            input_vlan.setStyleSheet("background-color: #ffffff; color: black;")  # Campo branco
            input_vlan.setValidator(QIntValidator(1, 4000, self))  # Aceita apenas números entre 1 e 4000

            # Adiciona ao layout do grupo
            group_layout.addWidget(label_nome)
            group_layout.addWidget(input_nome)
            group_layout.addLayout(freq_layout)
            group_layout.addWidget(label_senha)
            group_layout.addWidget(input_senha)
            group_layout.addWidget(label_vlan)
            group_layout.addWidget(input_vlan)

            group.setLayout(group_layout)
            self.ssid_area.addWidget(group)

            # Armazena os campos
            self.ssid_fields.append({
                "nome": input_nome,
                "senha": input_senha,
                "vlan": input_vlan,
                "check_24": check_24,
                "check_5": check_5,
            })

    def salvar_e_executar(self):
        user_inc = self.input_user.text().strip()
        pass_inc = self.input_pass.text().strip()
        site = self.input_site.text().strip()
        quantidade = len(self.ssid_fields)

        try:
            with open("variaveis.robot", "w", encoding="utf-8") as f:
                f.write("*** Variables ***\n")
                f.write(f"${{USER_INC}}    {user_inc}\n")
                f.write(f"${{PASS_INC}}    {pass_inc}\n")
                f.write(f"${{SITE}}    {site}\n")
                f.write(f"${{SSID_COUNT}}    {quantidade}\n")

                for i, ssid in enumerate(self.ssid_fields, start=1):
                    nome = ssid["nome"].text().strip()
                    senha = ssid["senha"].text().strip()
                    vlan = ssid["vlan"].text().strip()
                    freq_24 = ssid["check_24"].isChecked()
                    freq_5 = ssid["check_5"].isChecked()

                    f.write(f"${{SSID{i}}}    {nome}\n")
                    f.write(f"${{SENHA{i}}}    {senha}\n")
                    f.write(f"${{FREQ24_{i}}}    {freq_24}\n")
                    f.write(f"${{FREQ5_{i}}}    {freq_5}\n")
                    f.write(f"${{VLAN{i}}}    {vlan}\n")

            subprocess.run(["robot", "inc_main.robot"], check=True)
            QMessageBox.information(self, "Sucesso", "Teste executado com sucesso!")
        except subprocess.CalledProcessError:
            QMessageBox.critical(self, "Erro", "Erro ao executar o teste. Verifique o console.")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro inesperado: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SSIDConfigurator()
    window.show()
    sys.exit(app.exec())
