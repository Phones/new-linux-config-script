import sys
from PyQt5.QtWidgets import QApplication
from GraficInterface.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    checkbox_widget = MainWindow()
    sys.exit(app.exec_())