from tools.formatting import *


def free_gen(machine: str, data: list) -> list:
    """Genera las líneas de tape

    Args:
        machine (str): Tipo de máquina utilizada
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape
    """
    fre, sde = data.values()
    iu_space = fspace_ui()

    if sde == "$1":
        lines1 = [fre]
        lines2 = [iu_space]
    elif sde == "$2":
        lines1 = [iu_space]
        lines2 = [fre]
    else:
        if machine == "B12":
            lines1 = [""]
            lines2 = [""]
        else:
            lines1 = [fre]
            lines2 = [iu_space]

    return [lines1, lines2]
