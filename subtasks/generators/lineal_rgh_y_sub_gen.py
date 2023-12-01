from tools.formatting import *
from tools.compensations import *


def lineal_rgh_y_sub_gen(machine: str, data: list) -> list:
    """Genera las líneas de tape

    Args:
        machine (str): Tipo de máquina utilizada
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape
    """

    if machine == "B12":
        return gen_b12(data)
    elif machine == "A16":
        return gen_a16(data)
    elif machine == "K16":
        return gen_k16(data)
    elif machine == "E16":
        return gen_e16(data)
    elif machine == "OMNITURN":
        return gen_omni(data)
    elif machine == "ROMI":
        return gen_romi(data)
    elif machine == "HARDINGE":
        return gen_hardinge(data)
    elif machine == "MAZAK":
        return gen_mazak(data)


def gen_b12(data: list) -> list:
    """Genera los códigos para torno suizo B12

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    lines1, lines2 = [""], [""]

    return [lines1, lines2]


def gen_a16(data: list) -> list:
    """Genera los códigos para torno suizo A16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    lines1, lines2 = [""], [""]

    return [lines1, lines2]


def gen_k16(data: list) -> list:
    """Genera los códigos para torno suizo K16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    lines1, lines2 = [""], [""]

    return [lines1, lines2]


def gen_e16(data: list) -> list:
    """Genera los códigos para torno suizo E16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    lines1, lines2 = [""], [""]

    return [lines1, lines2]


def gen_omni(data: list) -> list:
    """Genera los códigos para torno OmniTurn

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    lines1, lines2 = [""], [""]

    return [lines1, lines2]


def gen_romi(data: list) -> list:
    """Genera los códigos para torno Romi

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    lines1, lines2 = [""], [""]

    return [lines1, lines2]


def gen_hardinge(data: list) -> list:
    """Genera los códigos para torno Hardinge

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    lines1, lines2 = [""], [""]

    return [lines1, lines2]


def gen_mazak(data: list) -> list:
    """Genera los códigos para fresadora Mazak

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    mtx, cut, blk = data.values()
    blk = "/" if blk else ""
    blank_space = fspace()

    yin = fnum4(mtx[0][2])
    ynd = fnum4(mtx[0][3])

    lines1 = [
        f"{blk}G91G01Z-{fnum3(cut)}F.002",
        f"{blk}Y{fnum4(yin)}F.015",
        f"/Y{fnum4(ynd)}",
        f"{blk}Z-{fnum3(cut)}F.002",
        f"/Y-{fnum4(ynd)}F.015",
        f"{blk}Y-{fnum4(yin)}F.015",
    ]
    
    lines2 = [blank_space for _ in lines1]

    return [lines1, lines2]
