import sys
from AppWindow import AppWindow
from Controller import Controller
from PyQt5.QtWidgets import QApplication, QWidget, QDialog


def main():
    app = QApplication(sys.argv)
    appWindow = AppWindow()
    controller = Controller(appWindow.gui)
    appWindow.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()