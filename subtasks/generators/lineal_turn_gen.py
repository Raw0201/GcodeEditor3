from tools.cnc_codes import *
from tools.formatting import *


def lineal_turn_gen(machine, data) -> list:
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

    xin, zin, fed, seq, mov, sde, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    if sde != "$1":
        return [[blank_space], [blank_space]]

    xin = "" if xin == "" else f"X{fnum4(xin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    seq = "" if seq == 0 else f"N{int(seq)}"
    mov = "" if mov == "" else swiss_g_codes[f"MOVIMIENTO {mov}"]

    lines1 = [f"{blk}{seq}{mov}{xin}{zin}{fed}"]
    lines2 = [blank_space]

    return [lines1, lines2]


def gen_a16(data: list) -> list:
    """Genera los códigos para torno suizo A16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, zin, fed, seq, mov, sde, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    if sde != "$1":
        return [[blank_space], [blank_space]]

    xin = "" if xin == "" else f"X{fnum4(xin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    seq = "" if seq == 0 else f"N{int(seq)}"
    mov = "" if mov == "" else swiss_g_codes[f"MOVIMIENTO {mov}"]

    lines1 = [f"{blk}{seq}{mov}{xin}{zin}{fed}"]
    lines2 = [blank_space]

    return [lines1, lines2]


def gen_k16(data: list) -> list:
    """Genera los códigos para torno suizo K16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, zin, fed, seq, mov, sde, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    xin = "" if xin == "" else f"X{fnum4(xin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    seq = "" if seq == 0 else f"N{int(seq)}"
    mov = "" if mov == "" else swiss_g_codes[f"MOVIMIENTO {mov}"]

    lines1 = [f"{blk}{seq}{mov}{xin}{zin}{fed}"]
    lines2 = [blank_space]

    return [lines2, lines1] if sde == "$2" else [lines1, lines2]


def gen_e16(data: list) -> list:
    """Genera los códigos para torno suizo E16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, zin, fed, seq, mov, sde, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    xin = "" if xin == "" else f"X{fnum4(xin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    seq = "" if seq == 0 else f"N{int(seq)}"
    mov = "" if mov == "" else swiss_g_codes[f"MOVIMIENTO {mov}"]

    lines1 = [f"{blk}{seq}{mov}{xin}{zin}{fed}"]
    lines2 = [blank_space]

    return [lines2, lines1] if sde == "$2" else [lines1, lines2]


def gen_omni(data: list) -> list:
    """Genera los códigos para torno OmniTurn

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, zin, fed, seq, mov, sde, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    if sde != "$1":
        return [[blank_space], [blank_space]]

    xin = "" if xin == "" else f"X{fnum4(xin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    seq = "" if seq == 0 else f"N{int(seq)}"

    lines1 = [f"{blk}{seq}{xin}{zin}{fed}"]
    lines2 = [blank_space]

    return [lines1, lines2]


def gen_romi(data: list) -> list:
    """Genera los códigos para torno Romi

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, zin, fed, seq, mov, sde, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    if sde != "$1":
        return [[blank_space], [blank_space]]

    xin = "" if xin == "" else f"X{fnum4(xin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    seq = "" if seq == 0 else f"N{int(seq)}"
    mov = "" if mov == "" else lathe_g_codes[f"MOVIMIENTO {mov}"]

    lines1 = [f"{blk}{seq}{mov}{xin}{zin}{fed}"]
    lines2 = [blank_space]

    return [lines1, lines2]


def gen_hardinge(data: list) -> list:
    """Genera los códigos para torno Hardinge

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, zin, fed, seq, mov, sde, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    if sde != "$1":
        return [[blank_space], [blank_space]]

    xin = "" if xin == "" else f"X{fnum4(xin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    seq = "" if seq == 0 else f"N{int(seq)}"
    mov = "" if mov == "" else lathe_g_codes[f"MOVIMIENTO {mov}"]

    lines1 = [f"{blk}{seq}{mov}{xin}{zin}{fed}"]
    lines2 = [blank_space]

    return [lines1, lines2]


def gen_mazak(data: list) -> list:
    """Genera los códigos para fresadora Mazak

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    lines1, lines2 = [""], [""]

    return [lines1, lines2]
