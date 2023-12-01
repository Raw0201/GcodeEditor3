import tools
from tools.widgets import *
from tools.tape_lists import *
from tools.default_data import *


def collect_data(window: QMainWindow, data_class: str):
    """Crea una sub tarea para recolectar datos de configuración

    Args:
        window (QMainWindow): Ventana principal
        data_class (str): Clase de la sub tarea
    """

    subtask_class = tools.sub_tasks.tasks_list[data_class]["Name"]
    window.subtask1 = subtask_class(window)

    if data_class not in {
        "Free",
        "End",
        "Tool_close",
        "Turn_ini",
        "Mill_ini",
        "Mill_end",
        "Drill_ini",
        "Drill_end",
        "Rough_turn_cycle_end",
        "Flatten_sub",
        "Lineal_rgh_x_sub",
        "Lineal_rgh_y_sub",
    }:
        window.subtask1.show()
    else:
        window.subtask1.collector()


def store_config_data(window: QMainWindow, data_pack: list, modif: bool):
    """Almacena los datos recolectados en la lista de configuración

    Args:
        window (QMainWindow): Ventana principal
        data_pack (list): Lista de datos recolectados
        modif (bool): Indicador de datos modificados
    """

    if modif:
        update_modified_data(window, data_pack)
    elif not window.current_selection:
        append_new_data(window, data_pack)
    else:
        insert_new_data(window, data_pack)

    load_default_variables(window)
    generate_tape_lines(window, window.config_list)
    update_data_widgets(window)


def update_modified_data(window: QMainWindow, data_pack: list):
    """Actualiza los datos modificados en la lista de configuración

    Args:
        window (QMainWindow): Ventana principal
        data_pack (list): Paquete de datos modificados
    """

    task = data_pack[0][0]
    data = data_pack[0][1]
    index = window.current_selection[0]
    window.config_list[index] = [task, data]
    tools.main_window.update_data(window)


def append_new_data(window: QMainWindow, data_pack: list):
    """Agrega los datos recolectados al final de la lista

    Args:
        window (QMainWindow): Ventana principal
        data_pack (list): Paquete de datos recolectados
    """

    for pack in data_pack:
        task = pack[0]
        data = pack[1]
        window.config_list.append([task, data])

        end_line = len(window.config_list) - 1
        window.current_selection = [end_line]


def insert_new_data(window: QMainWindow, data_pack: list):
    """Inserta los datos recolectados en una posición de la lista

    Args:
        data_pack (list): Paquete de datos recolectados
    """

    for pack in data_pack:
        task = pack[0]
        data = pack[1]
        current_index = window.current_selection[0] + 1
        window.config_list.insert(current_index, [task, data])
        window.current_selection = [current_index]
