from PySide6.QtWidgets import QMainWindow

from main import *
from tools import sub_tasks
from tools.formatting import *
from tools.config_list import *
from tools.validations import *
from tools.directories import *
from tools.main_window import *
from tools.default_data import *
from tools.message_boxes import *
from tools.prefab_blocks import *
from tools.combo_box_lists import *
from tools.file_management import *

from subtasks.sub_task import Subtask
from subtasks.generators.radial_turn_gen import radial_turn_gen
from interfaces.ui_radial_turn import Ui_frm_radial_turn


class Radial_turn(Subtask, Ui_frm_radial_turn):
    def __init__(self, main_window):
        super().__init__()
        self.window = main_window
        self.task = sub_tasks.tasks_list["Radial_turn"]["Description"]
        self.image = "radial_turn.png"

        self.btn_switch.clicked.connect(
            lambda: self.change_to(self.window, "Lineal_turn")
        )

        self.cbx_mov.addItems(radial_moves_list)
        self.cbx_sde.addItems(tape_sides_list)
        self.cbx_sde.setCurrentText(self.window.current_side)

    def collector(self):
        """Recolecta los datos de la sub tarea ingresados por el usuario"""

        data = {
            "Xin": self.tbx_xin.text(),
            "Zin": self.tbx_zin.text(),
            "Fed": self.tbx_fed.text(),
            "Xcn": self.tbx_xcn.text(),
            "Zcn": self.tbx_zcn.text(),
            "Mov": self.cbx_mov.currentText(),
            "Sde": self.cbx_sde.currentText(),
            "Blk": False,
        }

        self.validator(data)

    def validator(self, data: dict):
        """Valida los datos del diccionario recopilado

        Args:
            data (dict): Diccionario de datos recopilados
        """

        if data["Xin"] == "" or data["Zin"] == "" or data["Xcn"] == "":
            required_data_error(self)
            return
        self.converter(data)

        if (
            data["Fed"] != ""
            and float(data["Fed"]) < 1
            and self.window.current_machine == "OMNITURN"
        ):
            low_feed_information(self)

    def converter(self, data: dict):
        """Formatea los datos del diccionario recopilado

        Args:
            data (dict): Diccionario de datos recopilados
        """

        try:
            data["Xin"] = foper(data["Xin"])
            data["Zin"] = foper(data["Zin"])
            data["Fed"] = foper(data["Fed"])
            data["Xcn"] = foper(data["Xcn"])
            data["Zcn"] = foper(data["Zcn"])

        except ValueError:
            data_type_error(self)
            return

        self.packer(data)

    def packer(self, data: dict):
        """Agrega datos al paquete de datos a exportar

        Args:
            data (dict): Diccionario de datos recopilados
        """

        data1 = (self.task, data)
        self.data_pack = [data1]
        store_config_data(
            self.window,
            self.data_pack,
            self.modification,
        )

        self.close()
        self.modification = False
        collect_data(self.window, "Radial_turn")

    def generator(self, machine: str, data: dict) -> list:
        """Genera la lista de líneas de tape

        Args:
            machine (str): Máquina actual
            data (dict): Diccionario de datos de configuración

        Returns:
            list: Lista de líneas de tape
        """

        return radial_turn_gen(machine, data)

    def modifier(self, data: dict):
        """Modifica la línea de configuración seleccionada

        Args:
            data (dict): Diccionario de datos de configuración
        """

        self.modification = True
        xin, zin, fed, xcn, zcn, mov, sde, blk = data.values()

        self.tbx_xin.setText(str(xin))
        self.tbx_xin.setSelection(0, 100)
        self.tbx_zin.setText(str(zin))
        self.tbx_fed.setText(str(fed))
        self.tbx_xcn.setText(str(xcn))
        self.tbx_zcn.setText(str(zcn))
        self.cbx_mov.setCurrentText(str(mov))
        self.cbx_sde.setCurrentText(str(sde))
        self.btn_save.setText("Actualizar")
        self.btn_switch.setEnabled(False)
        self.show()

    def processor(self, window: QMainWindow, data: dict):
        """Procesa los datos de configuración para cambiar valores de variables

        Args:
            window (QMainWindow): Ventana principal
            data (dict): Diccionario de datos de configuración
        """

        window.save_required = True

    def switcher(self, window: QMainWindow, data: dict):
        """Cambia el estado de los botones según los datos de configuración

        Args:
            window (QMainWindow): Ventana principal
            data (dict): Diccionario de datos de configuración
        """

        pass
