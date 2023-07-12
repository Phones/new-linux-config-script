from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QPushButton, QHBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        options = [
            "git",
            "wget",
            "g++",
            "python3-pip",
            "python-is-python3",
            "snapd",
            "spotify",
            "google-chrome",
            "vscode",
            "discord",
            "steam",
            "OBS",
            "docker",
            "docker-compose",
            "obsidian",
            "extensões-vscode"
        ]

        for option in options:
            checkbox = QCheckBox(option)
            checkbox.setChecked(True)
            vbox.addWidget(checkbox)

        hbox = QHBoxLayout()
        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Cancelar")
        hbox.addWidget(ok_button)
        hbox.addWidget(cancel_button)

        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setWindowTitle("Interface de Checkbox")
        self.setGeometry(100, 100, 300, 300)

        ok_button.clicked.connect(self.close)  # Conecta o botão "OK" ao fechamento da janela
        cancel_button.clicked.connect(self.exit_application)  # Conecta o botão "Cancelar" ao encerramento do programa

        self.show()

    def return_clicked_options(self):
        marked_options = []
        for checkbox in self.checkboxes:
            if checkbox.isChecked():
                marked_options.append(checkbox.text())

        return marked_options

    def exit_application(self):
        QApplication.quit()