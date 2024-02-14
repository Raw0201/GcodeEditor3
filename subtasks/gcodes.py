from PySide6.QtWidgets import (
    QMainWindow,
)

from main import *
from tools.sub_windows import key_pressed
from interfaces.ui_data_window import Ui_frm_data_window
from tools.constants import *
from tools.cnc_gcodes import *


class Gcodes(QMainWindow, Ui_frm_data_window):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)

        machine = main_window.current_machine
        self.setWindowTitle(f"{APP_NAME} - Códigos G - {machine}")

        code_lists_dict = {
            "": [],
            "B12": swiss_g_codes,
            "A16": swiss_g_codes,
            "K16": kswiss_g_codes,
            "E16": kswiss_g_codes,
            "OMNITURN": omni_g_codes,
            "ROMI": romi_g_codes,
            "HARDINGE":  hardinge_g_codes,
            "MAZAK": mill_g_codes
        }

        data = code_lists_dict[machine]
        data_widget_load(self, data, 4)

    def keyPressEvent(self, qKeyEvent):
        key_pressed(self, qKeyEvent)
