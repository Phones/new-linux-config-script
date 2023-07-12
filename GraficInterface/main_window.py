from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QPushButton, QHBoxLayout


class CheckboxData:
    def __init__(self, option, install_type):
        self.option = option
        self.install_type = install_type
        self.checked = True

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.checkboxes = []

        options = [
            CheckboxData("git", "apt"),
            CheckboxData("wget", "apt"),
            CheckboxData("g++", "apt"),
            CheckboxData("python3-pip", "apt"),
            CheckboxData("python-is-python3", "apt"),
            CheckboxData("snapd", "apt"),
            CheckboxData("spotify", "snap"),
            CheckboxData("google-chrome", "download"),
            CheckboxData("vscode", "download"),
            CheckboxData("discord", "download"),
            CheckboxData("steam", "apt"),
            CheckboxData("OBS", "flatpak"),
            CheckboxData("docker", "script"),
            CheckboxData("docker-compose", "download"),
            CheckboxData("obsidian", "download"),
            CheckboxData("extensões-vscode", "code")
        ]

        for option in options:
            checkbox = QCheckBox(option.option)
            checkbox.setChecked(option.checked)
            vbox.addWidget(checkbox)
            checkbox.stateChanged.connect(self.on_checkbox_state_changed)
            self.checkboxes.append(option)

        hbox = QHBoxLayout()
        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Cancelar")
        hbox.addWidget(ok_button)
        hbox.addWidget(cancel_button)

        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setWindowTitle("Interface de Checkbox")
        self.setGeometry(100, 100, 300, 300)

        ok_button.clicked.connect(self.get_clicked_options)  # Conecta o botão "OK" ao fechamento da janela
        cancel_button.clicked.connect(self.exit_application)  # Conecta o botão "Cancelar" ao encerramento do programa

        self.show()

    def on_checkbox_state_changed(self, state):
        checkbox = self.sender()
        for option in self.checkboxes:
            if checkbox.text() == option.option:
                option.checked = state == Qt.Checked

    def get_clicked_options(self):
        marked_options = []
        for option in self.checkboxes:
            if option.checked:
                marked_options.append(option)

        # print("Opções marcadas:")
        # for label, value in marked_options:
        #     print(label, "- Valor:", value)

        # self.close()

        return marked_options

    def exit_application(self):
        QApplication.quit()