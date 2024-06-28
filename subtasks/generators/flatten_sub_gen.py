from tools.formatting import *
from tools.compensations import *
import math

def flatten_sub_gen(machine: str, data: list) -> list:
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

    gen = flatten_gen(data)
    fed, xin, xnd, cut, res, cts, yin, cys, yct, yru, yrb = gen
    iu_space = fspace_ui()

    lines1 = [f"G91G01Z-{fnum3(cut)}F.002"]
    for cyc in range(int(cys)):
        if cyc < yct:
            fed = fed if cyc == 0 else ""
            lines1.append(yin)
            lines1.append(f"X-{fnum3(xin)}{fed}")
            lines1.append(f"/X-{fnum3(xnd)}")
            yds = res / cts
            yru += yds
            yin = f"Y{fnum3(yds)}"
            lines1.append(f"Y{fnum3(yds)}")
            lines1.append(f"/X{fnum3(xnd)}")
            lines1.append(f"X{fnum3(xin)}")
        else:
            yds = res / cts
            lines1.append(f"/Y{fnum3(yds)}")
            yrb += yds
            lines1.append(f"/X-{fnum3(xin + xnd)}")
            lines1.append(f"/Y{fnum3(yds)}")
            yrb += yds
            lines1.append(f"/X{fnum3(xnd + xin)}")
    lines1.append(f"/G00Y-{fnum3(yrb)}")
    lines1.append(f"G00Y-{fnum3(yru)}")

    lines2 = [iu_space for _ in lines1]
    del lines2[-1]

    return [lines1, lines2]

def flatten_gen(data: list) -> list:
    """Efectúa los cálculos para refrentado de platina

    Args:
        data (list): Lista de datos de platina

    Returns:
        list: Lista de puntos de refrentado
    """
    tol, dia, cut, xdm, ydm, ypc, xpc, xnd, blk = data.values()

    xps = (float(dia) / 2) + 0.05
    xin = xps - xpc
    xnd = xps - xnd

    cut = fnum3(cut)
    fed = "F.015"
    amn = dia - 0.1
    res = ydm - amn
    cts = math.ceil(res / amn)
    cts = cts + 1 if cts % 2 == 0 else cts
    yds = ""
    yin = yds
    cys = (cts + 1) / 2

    yps = ydm + ypc
    yct = math.ceil((yps / amn) / 2)

    yru = 0
    yrb = 0
    return fed, xin, xnd, cut, res, cts, yin, cys, yct, yru, yrb
