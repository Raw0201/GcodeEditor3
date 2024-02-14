from PySide6.QtWidgets import (
    QMainWindow,
)

from main import *
from tools.sub_windows import key_pressed
from interfaces.ui_data_window import Ui_frm_data_window
from tools.constants import *
from tools.tool_tables import *


class Thread_data(QMainWindow, Ui_frm_data_window):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle(f"{APP_NAME} - Tabla de roscas")

        data = thread_table
        data_widget_load(self, data, 2)

    def keyPressEvent(self, qKeyEvent):
        key_pressed(self, qKeyEvent)
