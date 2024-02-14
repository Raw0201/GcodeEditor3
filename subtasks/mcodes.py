from PySide6.QtWidgets import (
    QMainWindow,
)

from main import *
from tools.sub_windows import key_pressed
from interfaces.ui_data_window import Ui_frm_data_window
from tools.constants import *
from tools.cnc_mcodes import *


class Mcodes(QMainWindow, Ui_frm_data_window):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)

        machine = main_window.current_machine
        self.setWindowTitle(f"{APP_NAME} - Códigos M - {machine}")

        code_lists_dict = {
            "": [],
            "B12": swiss_m_codes,
            "A16": swiss_m_codes,
            "K16": kswiss_m_codes,
            "E16": kswiss_m_codes,
            "OMNITURN": omni_m_codes,
            "ROMI": romi_m_codes,
            "HARDINGE":  hardinge_m_codes,
            "MAZAK": mill_m_codes
        }

        data = code_lists_dict[machine]
        data_widget_load(self, data, 3)

    def keyPressEvent(self, qKeyEvent):
        key_pressed(self, qKeyEvent)
