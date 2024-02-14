import json


def save_config_file(name: str, source: list) -> None:
    """Guarda la configuración en un archivo .json

    Args:
        name (str): _description_
        source (list): _description_
    """

    if not source:
        return

    file = f"{name}.json"
    with open(file, "w") as file:
        json.dump(source, file)


def update_file_name(window) -> None:
    """Actualiza el nombre del archivo

    Args:
        window (QMainWindow): Ventana principal
    """

    back = " (H)" if window.swiss_back_machining else ""
    machine = window.current_machine
    file_extension = ""
    file_name = ""

    if machine in ("B12", "A16", "K16", "E16"):
        file_name = f"({window.current_machine}) {window.part_name}{back}"
        file_extension = ".CNC"
    elif machine == "OMNITURN":
        file_name = window.main_tape_number
    elif machine == "ROMI":
        file_name = f"R{window.main_tape_number}"
    elif machine == "HARDINGE":
        file_name = f"H{window.main_tape_number}"
    elif machine == "MAZAK":
        file_name = f"{window.main_tape_number}"
        file_extension = ".EIA"

    window.config_file_name = file_name
    window.file_extension = file_extension
