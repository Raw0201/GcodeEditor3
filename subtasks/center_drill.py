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
from subtasks.generators.center_drill_gen import center_drill_gen
from interfaces.ui_center_drill import Ui_frm_center_drill


class Center_drill(Subtask, Ui_frm_center_drill):
    def __init__(self, main_window):
        super().__init__()
        self.window = main_window
        self.task = sub_tasks.tasks_list["Center_drill"]["Description"]
        self.image = "center.png"

        self.cbx_sde.addItems(tape_sides_list)
        self.cbx_sde.setCurrentText(self.window.current_side)
        self.cbx_sys.addItems(coordinates_systems[1:])
        self.cbx_znd.addItems(retraction_positions[1:])

    def collector(self):
        """Recolecta los datos de la sub tarea ingresados por el usuario"""

        data = {
            "Dpt": self.tbx_dpt.text(),
            "Fed": self.tbx_fed.text(),
            "Xin": self.tbx_xin.text(),
            "Yin": self.tbx_yin.text(),
            "Zin": self.tbx_zin.text(),
            "Rtr": self.tbx_rtr.text(),
            "Dwl": self.tbx_dwl.text(),
            "Sde": self.cbx_sde.currentText(),
            "Sys": self.cbx_sys.currentText(),
            "Znd": self.cbx_znd.currentText(),
            "Blk": False,
        }

        self.validator(data)

    def validator(self, data: dict):
        """Valida los datos del diccionario recopilado

        Args:
            data (dict): Diccionario de datos recopilados
        """

        if all_empty(data):
            required_data_error(self)
            return
        self.converter(data)

        if data["Fed"] < 1 and self.window.current_machine == "OMNITURN":
            low_feed_information(self)

    def converter(self, data: dict):
        """Formatea los datos del diccionario recopilado

        Args:
            data (dict): Diccionario de datos recopilados
        """

        try:
            data["Dpt"] = foper(data["Dpt"])
            data["Fed"] = foper(data["Fed"])
            data["Xin"] = foper(data["Xin"])
            data["Yin"] = foper(data["Yin"])
            data["Zin"] = foper(data["Zin"])
            data["Rtr"] = foper(data["Rtr"])
            data["Dwl"] = foper(data["Dwl"])
        except ValueError:
            data_type_error(self)
            return

        self.packer(data)

    def packer(self, data: dict):
        """Agrega datos al paquete de datos a exportar

        Args:
            data (dict): Diccionario de datos recopilados
        """

        if data["Sde"] == "$1":
            tol = 21
        elif data["Sde"] == "$2":
            tol = 31
        else:
            tol = 16

        data1 = (self.task, data)
        data2 = prefab_space(data["Sde"])
        data3 = prefab_center_drill_tool_call(tol, 0, 0, -0.05, data["Sde"])
        data4 = prefab_comment(
            "AGUJERO CENTRO",
            data["Sde"],
        )
        data5 = prefab_tool_close(
            self.window.current_tool,
            data["Sde"],
            self.window.current_bar_diameter,
        )

        if self.modification:
            self.data_pack = [data1]
        else:
            self.data_pack = [data2, data3, data4, data1, data5]

        store_config_data(
            self.window,
            self.data_pack,
            self.modification,
        )

        self.close()
        self.modification = False

    def generator(self, machine: str, data: dict) -> list:
        """Genera la lista de líneas de tape

        Args:
            machine (str): Máquina actual
            data (dict): Diccionario de datos de configuración

        Returns:
            list: Lista de líneas de tape
        """

        return center_drill_gen(machine, data)

    def modifier(self, data: dict):
        """Modifica la línea de configuración seleccionada

        Args:
            data (dict): Diccionario de datos de configuración
        """

        self.modification = True
        dpt, fed, xin, yin, zin, rtr, dwl, sde, sys, znd, blk = data.values()

        self.tbx_dpt.setText(str(dpt))
        self.tbx_dpt.setSelection(0, 100)
        self.tbx_fed.setText(str(fed))
        self.tbx_xin.setText(str(xin))
        self.tbx_yin.setText(str(yin))
        self.tbx_zin.setText(str(zin))
        self.tbx_rtr.setText(str(rtr))
        self.tbx_dwl.setText(str(dwl))
        self.cbx_sde.setCurrentText(str(sde))
        self.cbx_sys.setCurrentText(str(sys))
        self.cbx_znd.setCurrentText(str(znd))
        self.btn_save.setText("Actualizar")
        self.show()

    def processor(self, window: QMainWindow, data: dict):
        """Procesa los datos de configuración para cambiar valores de variables

        Args:
            window (QMainWindow): Ventana principal
            data (dict): Diccionario de datos de configuración
        """

        window.save_required = True
        window.current_side = data["Sde"]

    def switcher(self, window: QMainWindow, data: dict):
        """Cambia el estado de los botones según los datos de configuración

        Args:
            window (QMainWindow): Ventana principal
            data (dict): Diccionario de datos de configuración
        """

        window.btn_center.setEnabled(True)
