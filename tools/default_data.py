from tools.constants import *
from PySide6.QtWidgets import QMainWindow


def load_persistent_data(window: QMainWindow):
    """Carga datos persistentes

    Args:
        window (QMainWindow): Ventana principal
    """

    window.current_machine = ""
    window.current_folder = ROOT_DIR


def load_default_data_lists(window: QMainWindow):
    """Carga los valores por defecto de las listas

    Args:
        window (QMainWindow): Ventana principal
    """

    window.config_list = []
    window.tape1_list = []
    window.tape2_list = []
    window.current_selection = []
    window.platter_data = []
    window.graph_list = []


def load_default_variables(window: QMainWindow):
    """Carga los valores por defecto de las variables principales

    Args:
        window (QMainWindow): Ventana principal
    """

    window.subtask1 = None
    window.current_widget = None
    window.config_file_name = ""
    window.file_extension = ""
    window.current_config_line = 0
    window.current_tool = 0
    window.current_comment = ""


def load_default_tape_conditions(window: QMainWindow):
    """Cargar condiciones del tape

    Args:
        window (QMainWindow): Ventana principal
    """

    window.modified_task = False
    window.save_required = False


def load_default_machining_data(window: QMainWindow):
    """Carga los valores por defecto de datos de mecanizado

    Args:
        window (QMainWindow): Ventana principal
    """

    window.current_side = ""
    window.current_work_offset = ""
    window.part_name = ""
    window.main_tape_number = ""
    window.last_config_name = ""
    window.tape_description = ""

    window.current_sequence_number = 0
    window.current_bar_diameter = 0
    window.current_part_length = 0
    window.current_chuck_position = 0
    window.current_cutoff_tool = ""
    window.current_tool = 0
    window.current_tool_type = ""
    window.current_tool_diameter = 0
    window.current_tool_specification = ""
    window.swiss_back_machining = False
    window.main_tape_active = False

    window.first_tool_number = None
    window.first_tool_type = None
    window.first_tool_diameter = None
    window.first_tool_spec = None
    window.first_xps = None
    window.first_yps = None
    window.first_zps = None


def load_default_subroutine_data(window: QMainWindow):
    """Carga los valores por defecto de datos de subrutina

    Args:
        window (QMainWindow): Ventana principal
    """

    window.current_subroutine = 0
    window.last_subroutine_number = 3999
    window.subroutine_tool = 0
    window.subroutine_tool_diameter = 0
    window.subroutine_tool_type = ""
    window.subroutine_tool_specification = ""
    window.current_main_program = ""
    window.subroutine_comment = ""
    window.subroutine_machine = ""
    window.subroutine_folder = ""
    window.platter_data = []
    window.current_cut_dpt = 0


def load_default_plate_data(window: QMainWindow):
    """Carga los valores por defecto de datos de la platina

    Args:
        window (QMainWindow): Ventana principal
    """

    window.material_lgt = 0
    window.material_wdt = 0
    window.column_qty = 0
    window.row_qty = 0
    window.column_spc = 0
    window.row_spc = 0
    window.x_space = 0
    window.y_space = 0
    window.x_compensation = 0
    window.y_compensation = 0
    window.lineal_matrix_x = []
    window.lineal_matrix_y = []
    window.square_matrix_xy = []
    window.square_matrix_yx = []
    window.sub_matrix_x = []
    window.sub_matrix_y = []
    window.plate_matrix_xy = PLATE_XY
    window.plate_matrix_yx = PLATE_YX


def load_default_window_components(window: QMainWindow):
    """Carga el estado por defecto de componentes de la ventana principal

    Args:
        window (QMainWindow): Ventana principal
    """

    window.window_components = {
        window.functions_dock: True,
        window.tape1_widget: True,
        window.tape2_widget: True,
        window.config_widget: True,
    }
