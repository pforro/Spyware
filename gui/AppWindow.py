from PyQt5.QtWidgets import QDialog
from Gui import Gui


class AppWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Gui(self)
        self.show()


    @property
    def gui(self):
        return self.ui