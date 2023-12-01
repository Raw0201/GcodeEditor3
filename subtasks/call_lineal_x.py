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
from subtasks.generators.call_lineal_x_gen import call_lineal_x_gen
from interfaces.ui_call_lineal import Ui_frm_call_lineal


class Call_lineal_x(Subtask, Ui_frm_call_lineal):
    def __init__(self, main_window):
        super().__init__()
        self.window = main_window
        self.task = sub_tasks.tasks_list["Call_lineal_x"]["Description"]
        self.image = "comment.png"

        self.tbx_sub.setText(str(self.window.last_subroutine_number + 1))
        self.tbx_sub.setSelection(0, 100)

        self.cbx_sec.addItems(yes_no_list)
        self.cbx_sec.setCurrentText("NO")

    def collector(self):
        """Recolecta los datos de la sub tarea ingresados por el usuario"""

        data = {
            "Sub": self.tbx_sub.text(),
            "Dpt": self.tbx_dpt.text(),
            "Cut": self.tbx_cut.text(),
            "Ubk": self.tbx_ubk.text(),
            "Sec": self.cbx_sec.currentText(),
            "Mtx": self.window.lineal_matrix_x,
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
        tools.main_window.subroutine_prep(self.window)
        collect_data(self.window, "Lineal_rgh_x_sub")
        collect_data(self.window, "End"),

    def converter(self, data: dict):
        """Formatea los datos del diccionario recopilado

        Args:
            data (dict): Diccionario de datos recopilados
        """

        try:
            data["Sub"] = int(data["Sub"])
            data["Dpt"] = foper(data["Dpt"])
            data["Cut"] = foper(data["Cut"])
            data["Ubk"] = int(data["Ubk"])

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

    def generator(self, machine: str, data: dict) -> list:
        """Genera la lista de líneas de tape

        Args:
            machine (str): Máquina actual
            data (dict): Diccionario de datos de configuración

        Returns:
            list: Lista de líneas de tape
        """

        data["Mtx"] = self.lineal_matrix_x

        return call_lineal_x_gen(machine, data)

    def modifier(self, data: dict):
        """Modifica la línea de configuración seleccionada

        Args:
            data (dict): Diccionario de datos de configuración
        """

        self.modification = True
        sub, dpt, cut, ubk, sec, mtx, blk = data.values()

        self.tbx_sub.setText(str(sub))
        self.tbx_sub.setSelection(0, 100)
        self.tbx_dpt.setText(str(dpt))
        self.tbx_cut.setText(str(cut))
        self.tbx_ubk.setText(str(ubk))
        self.cbx_sec.setCurrentText(str(sec))
        self.btn_save.setText("Actualizar")
        self.show()

    def processor(self, window: QMainWindow, data: dict):
        """Procesa los datos de configuración para cambiar valores de variables

        Args:
            window (QMainWindow): Ventana principal
            data (dict): Diccionario de datos de configuración
        """
        
        window.save_required = True
        window.current_cut_dpt = data["Cut"]
        window.current_side = "$1"
        window.last_subroutine_number = data["Sub"]

    def switcher(self, window: QMainWindow, data: dict):
        """Cambia el estado de los botones según los datos de configuración

        Args:
            window (QMainWindow): Ventana principal
            data (dict): Diccionario de datos de configuración
        """

        pass
