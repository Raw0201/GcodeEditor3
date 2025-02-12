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
from subtasks.generators.sub_matrix_gen import sub_matrix_gen
from subtasks.generators.sub_matrix_gen import matrix_gen
from interfaces.ui_sub_matrix import Ui_frm_sub_matrix


class Sub_matrix(Subtask, Ui_frm_sub_matrix):
    def __init__(self, main_window):
        super().__init__()
        self.window = main_window
        self.task = sub_tasks.tasks_list["Sub_matrix"]["Description"]
        self.image = "comment.png"

        self.tbx_sub.setText(str(self.window.last_subroutine_number + 1))
        self.tbx_sub.setSelection(0, 100)

        self.cbx_sec.addItems(yes_no_list)
        self.cbx_sec.setCurrentText("NO")
        self.cbx_axis.addItems(axis_list)
        self.cbx_axis.setCurrentText("COLUMNAS")

    def collector(self):
        """Recolecta los datos de la sub tarea ingresados por el usuario"""

        data = {
            "Sub": self.tbx_sub.text(),
            "Qty": self.tbx_qty.text(),
            "Spc": self.tbx_spacing.text(),
            "Axs": self.cbx_axis.currentText(),
            "Xin": self.tbx_x_ini.text(),
            "Yin": self.tbx_y_ini.text(),
            "Zin": self.tbx_z_ini.text(),
            "Rep": self.tbx_rep.text(),
            "Ubk": self.tbx_unblk.text(),
            "Cnt": self.tbx_cnt.text(),
            "Sec": self.cbx_sec.currentText(),
            "Mtx": None,
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
            data["Sub"] = int(data["Sub"])
            data["Qty"] = int(data["Qty"])
            data["Xin"] = foper(data["Xin"])
            data["Yin"] = foper(data["Yin"])
            data["Zin"] = foper(data["Zin"])
            data["Rep"] = int(foper(data["Rep"]))
            data["Spc"] = foper(data["Spc"])
            data["Ubk"] = int(data["Ubk"])
            data["Cnt"] = int(foper(data["Cnt"]))

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

        matrix = matrix_gen(data)

        data["Mtx"] = matrix[0] if data["Axs"] == "COLUMNAS" else matrix[1]

        return sub_matrix_gen(machine, data)

    def modifier(self, data: dict):
        """Modifica la línea de configuración seleccionada

        Args:
            data (dict): Diccionario de datos de configuración
        """

        self.modification = True
        sub, qty, spc, axs, xin, yin, zin, rep, ubk, cnt, sec, mtx, blk = data.values()

        self.tbx_sub.setText(str(sub))
        self.tbx_sub.setSelection(0, 100)
        self.tbx_qty.setText(str(qty))
        self.tbx_spacing.setText(str(spc))
        self.cbx_axis.setCurrentText(str(axs))
        self.tbx_x_ini.setText(str(xin))
        self.tbx_y_ini.setText(str(yin))
        self.tbx_z_ini.setText(str(zin))
        self.tbx_rep.setText(str(rep))
        self.tbx_unblk.setText(str(ubk))
        self.tbx_cnt.setText(str(cnt))
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
        window.current_side = "$1"
        window.last_subroutine_number = data["Sub"]

    def switcher(self, window: QMainWindow, data: dict):
        """Cambia el estado de los botones según los datos de configuración

        Args:
            window (QMainWindow): Ventana principal
            data (dict): Diccionario de datos de configuración
        """

        pass
