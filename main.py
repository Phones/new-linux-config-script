import sys
from PyQt5.QtWidgets import QApplication
from install_programs import InstallPrograms

if __name__ == '__main__':
    app = QApplication(sys.argv)
    checkbox_widget = InstallPrograms()
    checkbox_widget.install_programs()
    sys.exit(app.exec_())