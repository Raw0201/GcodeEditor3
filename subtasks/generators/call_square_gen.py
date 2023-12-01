from tools.formatting import *
import math


def call_square_gen(machine: str, data: list) -> list:
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
    sub, dpt, cut, ubk, sec, dyr, mtx, blk = data.values()
    blank_space = fspace()

    rep = 0 if cut == 0 else math.ceil(dpt / cut)
    zps = dpt if cut == 0 else (dpt - (rep * cut)) * -1

    if zps == -.0:
        zps = cut
        rep += 1

    zsc = fnum3(zps + 0.05)
    zps = fnum3(zps)
    rep = f"L{rep}" if rep > 1 else ""

    lines1 = []
    for cnt, point in enumerate(mtx):
        xpn, ypn = fnum4(point[0]), fnum4(point[1])
        pcn = cnt + 1
        if cnt >= ubk or blk:
            blk = "/"
        else:
            blk = ""
        lines1.append(f"{blk}G90G00X{xpn}Y{ypn}Z{zsc}({pcn})")
        lines1.append(f"{blk}G01Z{zps}F.02")
        lines1.append(f"{blk}M98P{sub}{rep}")
        lines1.append(f"{blk}G90G00Z{zsc}") if sec == "SÍ" else ""

    lines2 = [blank_space for _ in lines1]

    return [lines1, lines2]
