from tools.cnc_codes import *
from tools.formatting import *


def lineal_mill_gen(machine, data) -> list:
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

    xin, yin, zin, fed, rep, mov, sys, com, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    xin = "" if xin == "" else f"X{fnum4(xin)}"
    yin = "" if yin == "" else f"Y{fnum4(yin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    mov = "" if mov == "" else swiss_g_codes[f"MOVIMIENTO {mov}"]
    sys = "" if sys == "" else swiss_g_codes[f"SISTEMA {sys}"]
    com = "" if com == "" else swiss_g_codes[f"COMPENSACION {com}"]

    lines1 = [f"{blk}{com}{mov}{xin}{yin}{zin}{fed}"]
    lines2 = [blank_space]

    return [lines1, lines2]


def gen_k16(data: list) -> list:
    """Genera los códigos para torno suizo K16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, yin, zin, fed, rep, mov, sys, com, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    xin = "" if xin == "" else f"X{fnum4(xin)}"
    yin = "" if yin == "" else f"Y{fnum4(yin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    mov = "" if mov == "" else swiss_g_codes[f"MOVIMIENTO {mov}"]
    sys = "" if sys == "" else swiss_g_codes[f"SISTEMA {sys}"]
    com = "" if com == "" else swiss_g_codes[f"COMPENSACION {com}"]

    lines1 = [f"{blk}{com}{mov}{xin}{yin}{zin}{fed}"]
    lines2 = [blank_space]

    return [lines1, lines2]


def gen_e16(data: list) -> list:
    """Genera los códigos para torno suizo E16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, yin, zin, fed, rep, mov, sys, com, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    xin = "" if xin == "" else f"X{fnum4(xin)}"
    yin = "" if yin == "" else f"Y{fnum4(yin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    mov = "" if mov == "" else swiss_g_codes[f"MOVIMIENTO {mov}"]
    sys = "" if sys == "" else swiss_g_codes[f"SISTEMA {sys}"]
    com = "" if com == "" else swiss_g_codes[f"COMPENSACION {com}"]

    lines1 = [f"{blk}{com}{mov}{xin}{yin}{zin}{fed}"]
    lines2 = [blank_space]

    return [lines1, lines2]


def gen_omni(data: list) -> list:
    """Genera los códigos para torno OmniTurn

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, yin, zin, fed, rep, mov, sys, com, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    xin = yin if yin != "" else xin
    xin = "" if xin == "" else f"X{fnum4(xin)}"
    yin = "" if yin == "" else f"Y{fnum4(yin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    mov = "" if mov == "" else lathe_g_codes[f"MOVIMIENTO {mov}"]
    sys = "" if sys == "" else lathe_g_codes[f"SISTEMA {sys}"]
    com = "" if com == "" else lathe_g_codes[f"COMPENSACION {com}"]

    lines1 = [f"{blk}{com}{mov}{xin}{zin}{fed}"]
    lines2 = [blank_space]

    return [lines1, lines2]


def gen_romi(data: list) -> list:
    """Genera los códigos para torno Romi

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, yin, zin, fed, rep, mov, sys, com, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    xin = yin if yin != "" else xin
    xin = "" if xin == "" else f"X{fnum4(xin)}"
    yin = "" if yin == "" else f"Y{fnum4(yin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    mov = "" if mov == "" else lathe_g_codes[f"MOVIMIENTO {mov}"]
    sys = "" if sys == "" else lathe_g_codes[f"SISTEMA {sys}"]
    com = "" if com == "" else lathe_g_codes[f"COMPENSACION {com}"]

    lines1 = [f"{blk}{com}{mov}{xin}{zin}{fed}"]
    lines2 = [blank_space]

    return [lines1, lines2]


def gen_hardinge(data: list) -> list:
    """Genera los códigos para torno Hardinge

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, yin, zin, fed, rep, mov, sys, com, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    xin = yin if yin != "" else xin
    xin = "" if xin == "" else f"X{fnum4(xin)}"
    yin = "" if yin == "" else f"Y{fnum4(yin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    mov = "" if mov == "" else lathe_g_codes[f"MOVIMIENTO {mov}"]
    sys = "" if sys == "" else lathe_g_codes[f"SISTEMA {sys}"]
    com = "" if com == "" else lathe_g_codes[f"COMPENSACION {com}"]

    lines1 = [f"{blk}{com}{mov}{xin}{zin}{fed}"]
    lines2 = [blank_space]

    return [lines1, lines2]


def gen_mazak(data: list) -> list:
    """Genera los códigos para fresadora Mazak

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, yin, zin, fed, rep, mov, sys, com, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    xin = "" if xin == "" else f"X{fnum4(xin)}"
    yin = "" if yin == "" else f"Y{fnum4(yin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    mov = "" if mov == "" else mill_g_codes[f"MOVIMIENTO {mov}"]
    sys = "" if sys == "" else mill_g_codes[f"SISTEMA {sys}"]
    com = "" if com == "" else mill_g_codes[f"COMPENSACION {com}"]
    rep = 0 if rep == "" else rep
    rep = "" if rep < 1 else f"L{int(rep)}"

    lines1 = [f"{blk}{sys}{com}{mov}{xin}{yin}{zin}{rep}{fed}"]
    lines2 = [blank_space]

    return [lines1, lines2]
