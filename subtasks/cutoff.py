from PySide6.QtWidgets import QMainWindow

from main import *
from tools import sub_tasks
from tools.formatting import *
from tools.config_list import *
from tools.validations import *
from tools.directories import *
from tools.main_window import *
from tools.default_data import *
from tools.cutoff_table import *
from tools.message_boxes import *
from tools.prefab_blocks import *
from tools.combo_box_lists import *
from tools.file_management import *

from subtasks.sub_task import Subtask
from subtasks.generators.cutoff_gen import cutoff_gen
from interfaces.ui_cutoff import Ui_frm_cutoff


class Cutoff(Subtask, Ui_frm_cutoff):
    def __init__(self, main_window):
        super().__init__()
        self.window = main_window
        self.task = sub_tasks.tasks_list["Cutoff"]["Description"]
        self.image = "cutoff.png"

    def collector(self):
        """Recolecta los datos de la sub tarea ingresados por el usuario"""

        data = {
            "Dia": self.tbx_dia.text(),
            "Cfr": self.tbx_cfr.text(),
            "Lgt": self.window.current_part_length,
            "Chk": self.window.current_chuck_position,
            "Cof": self.window.current_cutoff_tool,
            "Blk": False,
        }

        self.validator(data)

    def validator(self, data: dict):
        """Valida los datos del diccionario recopilado

        Args:
            data (dict): Diccionario de datos recopilados
        """

        if any_empty(data):
            required_data_error(self)
            return
        self.converter(data)

    def converter(self, data: dict):
        """Formatea los datos del diccionario recopilado

        Args:
            data (dict): Diccionario de datos recopilados
        """

        try:
            data["Dia"] = foper(data["Dia"])
            data["Cfr"] = foper(data["Cfr"])
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
        data2 = prefab_space()

        self.data_pack = (
            [data1]
            if self.modification
            else [data2, data1]
        )
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

        data["Lgt"] = self.current_part_length
        data["Chk"] = self.current_chuck_position
        data["Cof"] = self.current_cutoff_tool

        return cutoff_gen(machine, data)

    def modifier(self, data: dict):
        """Modifica la línea de configuración seleccionada

        Args:
            data (dict): Diccionario de datos de configuración
        """

        self.modification = True
        dia, cfr, lgt, chk, cof, blk = data.values()

        self.tbx_dia.setText(str(dia))
        self.tbx_dia.setSelection(0, 100)
        self.tbx_cfr.setText(str(cfr))
        self.btn_save.setText("Actualizar")
        self.show()

    def processor(self, window: QMainWindow, data: dict):
        """Procesa los datos de configuración para cambiar valores de variables

        Args:
            window (QMainWindow): Ventana principal
            data (dict): Diccionario de datos de configuración
        """

        window.save_required = True

        machine = window.current_machine
        tool = cutoff_tools[machine]
        window.current_tool = tool

    def switcher(self, window: QMainWindow, data: dict):
        """Cambia el estado de los botones según los datos de configuración

        Args:
            window (QMainWindow): Ventana principal
            data (dict): Diccionario de datos de configuración
        """

        pass
