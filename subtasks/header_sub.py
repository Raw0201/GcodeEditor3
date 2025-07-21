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
from subtasks.generators.header_sub_gen import header_sub_gen
from interfaces.ui_header_sub import Ui_frm_header_sub


class Header_sub(Subtask, Ui_frm_header_sub):
    def __init__(self, main_window):
        super().__init__()
        self.window = main_window
        self.task = sub_tasks.tasks_list["Header_sub"]["Description"]
        self.image = "header.png"

        self.cbx_mch.addItems(machines_list)

    def collector(self):
        """Recolecta los datos de la sub tarea ingresados por el usuario"""

        data = {
            "Pgr": self.tbx_pgr.text(),
            "Mnp": self.tbx_mnp.text(),
            "Dsc": self.tbx_dsc.text(),
            "Plt": self.window.platter_data,
            "Tol": self.window.subroutine_tool,
            "Typ": self.window.subroutine_tool_type,
            "Dia": self.window.subroutine_tool_diameter,
            "Spc": self.window.subroutine_tool_specification,
            "Mch": self.cbx_mch.currentText(),
            "Lgt": self.tbx_lgt.text(),
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

    def converter(self, data: dict):
        """Formatea los datos del diccionario recopilado

        Args:
            data (dict): Diccionario de datos recopilados
        """

        try:
            data["Pgr"] = ftext(data["Pgr"]) if data["Pgr"] != "" else ""
            data["Mnp"] = ftext(data["Mnp"]) if data["Mnp"] != "" else ""
            data["Dsc"] = ftext(data["Dsc"]) if data["Dsc"] != "" else ""
            data["Lgt"] = foper(data["Lgt"])
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

        return header_sub_gen(machine, data)

    def modifier(self, data: dict):
        """Modifica la línea de configuración seleccionada

        Args:
            data (dict): Diccionario de datos de configuración
        """

        self.modification = True
        pgr, mnp, dsc, plt, tol, typ, dia, spc, mch, lgt = data.values()

        self.tbx_pgr.setText(str(pgr))
        self.tbx_pgr.setSelection(0, 100)
        self.tbx_mnp.setText(str(mnp))
        self.tbx_dsc.setText("-") if dsc == "" else self.tbx_dsc.setText(str(dsc))
        self.cbx_mch.setCurrentText(str(mch))
        self.tbx_lgt.setText(str(lgt))
        self.btn_save.setText("Actualizar")
        self.show()

    def processor(self, window: QMainWindow, data: dict):
        """Procesa los datos de configuración para cambiar valores de variables

        Args:
            window (QMainWindow): Ventana principal
            data (dict): Diccionario de datos de configuración
        """

        window.save_required = True
        window.current_machine = data["Mch"]
        # update_file_dir(window)

        window.main_tape_active = False
        window.current_machine = data["Mch"]
        window.part_name = data["Pgr"]
        window.main_tape_number = data["Pgr"]
        window.current_tool = data["Tol"]
        window.current_tool_type = data["Typ"]
        window.current_tool_diameter = data["Dia"]
        window.current_tool_specification = data["Spc"]

        window.tape_description = "SUBRUTINA"
        window.current_side = "$1"

        update_file_name(window)
        load_main_title(window)

    def switcher(self, window: QMainWindow, data: dict):
        """Cambia el estado de los botones según los datos de configuración

        Args:
            window (QMainWindow): Ventana principal
            data (dict): Diccionario de datos de configuración
        """

        load_default_buttons_status(window)
        load_default_tape_conditions(window)

        for button_list in (
            window.program_buttons_list,
            window.tool_buttons_list,
            window.machine_buttons_list,
            window.turning_buttons_list,
            window.milling_buttons_list,
            window.milling_cycle_buttons_list,
            window.drilling_buttons_list,
        ):
            for button in button_list:
                button.setEnabled(True)

        if window.current_machine != "MAZAK":
            for button in window.plate_buttons_list:
                button.setEnabled(False)
            for button in window.turning_buttons_list:
                button.setEnabled(True)

        if window.current_machine == "MAZAK":
            for button in window.turning_buttons_list:
                button.setEnabled(False)
            for button in window.plate_buttons_list:
                button.setEnabled(True)

        window.btn_header.setEnabled(False)
        window.btn_tool_close.setEnabled(False)
        window.btn_collect.setEnabled(False)
        window.btn_rough_turn_cycle_end.setEnabled(False)

        end_enabled = not window.main_tape_active
        window.btn_end.setEnabled(end_enabled)
