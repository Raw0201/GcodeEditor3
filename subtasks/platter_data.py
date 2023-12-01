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
from subtasks.generators.platter_data_gen import platter_data_gen
from subtasks.generators.platter_data_gen import matrix_gen
from interfaces.ui_platter_data import Ui_frm_platter_data


class Platter_data(Subtask, Ui_frm_platter_data):
    def __init__(self, main_window):
        super().__init__()
        self.window = main_window
        self.task = sub_tasks.tasks_list["Platter_data"]["Description"]
        self.image = "comment.png"

    def collector(self):
        """Recolecta los datos de la sub tarea ingresados por el usuario"""

        data = {
            "Cqt": self.tbx_col_qty.text(),
            "Csp": self.tbx_col_space.text(),
            "Rqt": self.tbx_row_qty.text(),
            "Rsp": self.tbx_row_space.text(),
            "Xsp": self.tbx_x_space.text(),
            "Ysp": self.tbx_y_space.text(),
            "Xdm": self.tbx_x_dim.text(),
            "Ydm": self.tbx_y_dim.text(),
            "Xcm": self.tbx_x_com.text(),
            "Ycm": self.tbx_y_com.text(),
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
            data["Cqt"] = int(data["Cqt"])
            data["Rqt"] = int(data["Rqt"])
            data["Csp"] = foper(data["Csp"])
            data["Rsp"] = foper(data["Rsp"])
            data["Xsp"] = foper(data["Xsp"])
            data["Ysp"] = foper(data["Ysp"])
            data["Xdm"] = foper(data["Xdm"])
            data["Ydm"] = foper(data["Ydm"])
            data["Xcm"] = foper(data["Xcm"])
            data["Ycm"] = foper(data["Ycm"])

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

        return platter_data_gen(machine, data)

    def modifier(self, data: dict):
        """Modifica la línea de configuración seleccionada

        Args:
            data (dict): Diccionario de datos de configuración
        """

        self.modification = True
        cqt, csp, rqt, rsp, xsp, ysp, xdm, ydm, xcm, ycm, blk = data.values()

        self.tbx_col_qty.setText(str(cqt))
        self.tbx_col_qty.setSelection(0, 100)
        self.tbx_col_space.setText(str(csp))
        self.tbx_row_qty.setText(str(rqt))
        self.tbx_row_space.setText(str(rsp))
        self.tbx_x_space.setText(str(xsp))
        self.tbx_y_space.setText(str(ysp))
        self.tbx_x_dim.setText(str(xdm))
        self.tbx_y_dim.setText(str(ydm))
        self.tbx_x_com.setText(str(xcm))
        self.tbx_y_com.setText(str(ycm))

        self.btn_save.setText("Actualizar")
        self.show()

    def processor(self, window: QMainWindow, data: dict):
        """Procesa los datos de configuración para cambiar valores de variables

        Args:
            window (QMainWindow): Ventana principal
            data (dict): Diccionario de datos de configuración
        """

        cqt, csp, rqt, rsp, xsp, ysp, xdm, ydm, xcm, ycm, blk = data.values()

        window.save_required = True
        window.material_lgt = xdm
        window.material_wdt = ydm
        window.column_qty = cqt
        window.row_qty = rqt
        window.column_spc = csp
        window.row_spc = rsp
        window.x_space = xsp
        window.y_space = ysp
        window.x_compensation = xcm
        window.y_compensation = ycm

        matrix = matrix_gen(data)
        window.lineal_matrix_x = matrix[0]
        window.lineal_matrix_y = matrix[1]
        window.square_matrix_xy = matrix[2]
        window.square_matrix_yx = matrix[3]

    def switcher(self, window: QMainWindow, data: dict):
        """Cambia el estado de los botones según los datos de configuración

        Args:
            window (QMainWindow): Ventana principal
            data (dict): Diccionario de datos de configuración
        """

        for button in window.plate_buttons_list:
            button.setEnabled(True)
        window.btn_platter_data.setEnabled(False)
