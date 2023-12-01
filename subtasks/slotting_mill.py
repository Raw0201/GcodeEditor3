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
from subtasks.generators.slotting_mill_gen import slotting_mill_gen
from interfaces.ui_slotting_mill import Ui_frm_slotting_mill


class Slotting_mill(Subtask, Ui_frm_slotting_mill):
    def __init__(self, main_window):
        super().__init__()
        self.window = main_window
        self.task = sub_tasks.tasks_list["Slotting_mill"]["Description"]
        self.image = "comment.png"

        self.cbx_pos.addItems(positions_list)
        self.cbx_pos.setCurrentText("POSITIVA")
        self.cbx_dir.addItems(directions_list)
        self.cbx_pos.setCurrentText("ALTERNADOS")

    def collector(self):
        """Recolecta los datos de la sub tarea ingresados por el usuario"""

        data = {
            "Dpt": self.tbx_dpt.text(),
            "Lgt": self.tbx_lgt.text(),
            "Cut": self.tbx_cut.text(),
            "Fed": self.tbx_fed.text(),
            "Ang": self.tbx_ang.text(),
            "Dim": self.tbx_dim.text(),
            "Pos": self.cbx_pos.currentText(),
            "Dyr": self.cbx_dir.currentText(),
            "Lcm": self.tbx_lcm.text(),
            "Tcm": self.tbx_tcm.text(),
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
            data["Dpt"] = foper(data["Dpt"])
            data["Lgt"] = foper(data["Lgt"])
            data["Cut"] = foper(data["Cut"])
            data["Fed"] = foper(data["Fed"])
            data["Ang"] = foper(data["Ang"])
            data["Dim"] = foper(data["Dim"])
            data["Lcm"] = foper(data["Lcm"])
            data["Tcm"] = foper(data["Tcm"])

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

        return slotting_mill_gen(machine, data)

    def modifier(self, data: dict):
        """Modifica la línea de configuración seleccionada

        Args:
            data (dict): Diccionario de datos de configuración
        """

        self.modification = True
        wdt, lgt, cut, fed, ang, dim, pos, dyr, lcm, tcm, blk = data.values()

        self.tbx_dpt.setText(str(wdt))
        self.tbx_dpt.setSelection(0, 100)
        self.tbx_lgt.setText(str(lgt))
        self.tbx_cut.setText(str(cut))
        self.tbx_fed.setText(str(fed))
        self.tbx_ang.setText(str(ang))
        self.tbx_dim.setText(str(dim))
        self.cbx_pos.setCurrentText(str(pos))
        self.cbx_dir.setCurrentText(str(dyr))
        self.tbx_lcm.setText(str(lcm))
        self.tbx_tcm.setText(str(tcm))
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
