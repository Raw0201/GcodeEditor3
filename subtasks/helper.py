from PySide6.QtWidgets import QMainWindow
from interfaces.ui_helper import Ui_frm_helper


class Helper(QMainWindow, Ui_frm_helper):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def closeEvent(self, event):
        self.close()
