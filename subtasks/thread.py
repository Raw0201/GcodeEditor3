from PySide6.QtWidgets import QMainWindow

from main import *
from tools import sub_tasks
from tools.formatting import *
from tools.config_list import *
from tools.validations import *
from tools.directories import *
from tools.main_window import *
from tools.default_data import *
from tools.thread_tables import *
from tools.message_boxes import *
from tools.prefab_blocks import *
from tools.combo_box_lists import *
from tools.file_management import *

from subtasks.sub_task import Subtask
from subtasks.generators.thread_gen import thread_gen
from interfaces.ui_thread import Ui_frm_thread


class Thread(Subtask, Ui_frm_thread):
    def __init__(self, main_window):
        super().__init__()
        self.window = main_window
        self.task = sub_tasks.tasks_list["Thread"]["Description"]
        self.image = "thread.png"

        self.cbx_thd.addItems(thread_table)
        self.cbx_typ.addItems(thread_types)
        self.cbx_pos.addItems(positions_list)
        self.cbx_rgh.addItems(yes_no_list)

    def collector(self):
        """Recolecta los datos de la sub tarea ingresados por el usuario"""

        data = {
            "Zin": self.tbx_zin.text(),
            "Znd": self.tbx_znd.text(),
            "Thd": self.cbx_thd.currentText(),
            "Typ": self.cbx_typ.currentText(),
            "Pos": self.cbx_pos.currentText(),
            "Rgh": self.cbx_rgh.currentText(),
            "Dia": self.window.current_bar_diameter,
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
            data["Zin"] = foper(data["Zin"])
            data["Znd"] = foper(data["Znd"])
        except ValueError:
            data_type_error(self)
            return

        self.packer(data)

    def packer(self, data: dict):
        """Agrega datos al paquete de datos a exportar

        Args:
            data (dict): Diccionario de datos recopilados
        """

        machine = self.window.current_machine
        tool = thread_tools[machine]
        xin = thread_table[data["Thd"]][0]
        xin = xin / 2 if machine == "OMNITURN" else xin

        data1 = (self.task, data)
        data2 = prefab_space()
        data3 = prefab_thread_tool_call(
            tool,
            xin,
            data["Zin"],
        )
        data4 = prefab_spindle(
            1500,
            "NORMAL",
            "$1",
        )
        data5 = prefab_tool_close(
            tool,
            "$1",
            self.window.current_bar_diameter,
        )

        self.data_pack = (
            [data1]
            if self.modification
            else [data2, data3, data4, data1, data5]
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

        data["Dia"] = self.current_bar_diameter
        return thread_gen(machine, data)

    def modifier(self, data: dict):
        """Modifica la línea de configuración seleccionada

        Args:
            data (dict): Diccionario de datos de configuración
        """

        self.modification = True
        zin, znd, thd, typ, pos, rgh, dia, blk = data.values()

        self.tbx_zin.setText(str(zin))
        self.tbx_zin.setSelection(0, 100)
        self.tbx_znd.setText(str(znd))
        self.cbx_thd.setCurrentText(str(thd))
        self.cbx_typ.setCurrentText(str(typ))
        self.cbx_pos.setCurrentText(str(pos))
        self.cbx_rgh.setCurrentText(str(rgh))
        self.btn_save.setText("Actualizar")
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
