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

from subtasks.generators.end_gen import end_gen


class End(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.window = main_window
        self.task = sub_tasks.tasks_list["End"]["Description"]
        self.modification = False

    def collector(self):
        """Recolecta los datos de la sub tarea ingresados por el usuario"""

        data = {
            "Mta": self.window.main_tape_active,
            "Bar": self.window.current_bar_diameter,
            "Lgt": self.window.current_part_length,
            "Chk": self.window.current_chuck_position,
            "Cof": self.window.current_cutoff_tool,
            "Tol": self.window.first_tool_number,
            "Typ": self.window.first_tool_type,
            "Dia": self.window.first_tool_diameter,
            "Spc": self.window.first_tool_spec,
            "Xps": self.window.first_xps,
            "Yps": self.window.first_yps,
            "Zps": self.window.first_zps,
        }
        self.packer(data)

    def validator(self, data: dict):
        """Valida los datos del diccionario recopilado

        Args:
            data (dict): Diccionario de datos recopilados
        """

        self.converter(data)

    def converter(self, data: dict):
        """Formatea los datos del diccionario recopilado

        Args:
            data (dict): Diccionario de datos recopilados
        """

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

    def generator(self, machine: str, data: dict) -> list:
        """Genera la lista de líneas de tape

        Args:
            machine (str): Máquina actual
            data (dict): Diccionario de datos de configuración

        Returns:
            list: Lista de líneas de tape
        """

        data["Mta"] = self.main_tape_active
        data["Bar"] = self.current_bar_diameter
        data["Lgt"] = self.current_part_length
        data["Chk"] = self.current_chuck_position
        data["Cof"] = self.current_cutoff_tool
        data["Tol"] = self.first_tool_number
        data["Typ"] = self.first_tool_type
        data["Dia"] = self.first_tool_diameter
        data["Spc"] = self.first_tool_spec
        data["Xps"] = self.first_xps
        data["Yps"] = self.first_yps
        data["Zps"] = self.first_zps

        return end_gen(machine, data)

    def modifier(self, data: dict):
        """Modifica la línea de configuración seleccionada

        Args:
            data (dict): Diccionario de datos de configuración
        """

        pass

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

        window.btn_end.setEnabled(False)
