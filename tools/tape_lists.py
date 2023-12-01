import tools

from PySide6.QtWidgets import QMainWindow


def generate_tape_lines(window: QMainWindow, data_list: list):
    """Genera las líneas de tape a partir de la lista de configuración

    Args:
        window (QMainWindow): Ventana principal
        data_list (list): Lista de configuración
    """

    window.tape1_list = []
    window.tape2_list = []
    window.current_config_line = 0

    for line in data_list:
        task = line[0]
        data = line[1]
        if task not in {"Inicio de programa", "Inicio de subrutina"}:
            window.current_config_line += 1

        task_class = tools.sub_tasks.get_task_class(task)
        task_class.processor(window, window, data)
        task_class.switcher(window, window, data)

        parameters = get_parameters(window)
        machine = window.current_machine
        tape_lines = task_class.generator(window, machine, data)

        store_tape_data(window, tape_lines, parameters)


def store_tape_data(window: QMainWindow, tape_lines: list, parameters: dict):
    """Guarda las líneas de tape en las listas respectivas

    Args:
        window (QMainWindow): Ventana principal
        tape_lines (list): Líneas generadas de tape
        parameters (dict): Diccionario de parámetros actuales
    """

    config_line, tool, ttype, diameter, spec, comment = parameters.values()

    for tape_line in tape_lines[0]:
        if tape_line != "":
            window.tape1_list.append(
                (config_line, tape_line, tool, ttype, diameter, spec, comment)
            )
    for tape_line in tape_lines[1]:
        if tape_line != "":
            window.tape2_list.append(
                (config_line, tape_line, tool, ttype, diameter, spec, comment)
            )


def get_parameters(window: QMainWindow) -> dict:
    """Obtiene los parámetros actuales de configuración

    Args:
        window (QMainWindow): Ventana principal

    Returns:
        dict: Diccionario de parámetros
    """

    return {
        "Config_line": window.current_config_line,
        "Current_tool": window.current_tool,
        "Current_type": window.current_tool_type,
        "Current_diameter": window.current_tool_diameter,
        "Current_specification": window.current_tool_specification,
        "Current_comment": window.current_comment,
    }
