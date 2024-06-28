from tools.formatting import *
from tools.cnc_codes import *


def radial_mill_gen(machine, data) -> list:
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

    xin, yin, zin, fed, xcn, ycn, zcn, mov, sys, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    xin = "" if xin == "" else f"X{fnum4(xin)}"
    yin = "" if yin == "" else f"Y{fnum4(yin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    mov = "" if mov == "" else swiss_g_codes[f"GIRO {mov}"]
    sys = "" if sys == "" else swiss_g_codes[f"SISTEMA {sys}"]

    if xcn != "" and ycn == "" and zcn == "":
        rad = "" if xcn == "" else f"R{fnum4(xcn)}"
    else:
        xcn = "" if xcn == "" else f"I{fnum4(xcn)}"
        ycn = "" if ycn == "" else f"J{fnum4(ycn)}"
        zcn = "" if zcn == "" else f"K{fnum4(zcn)}"
        rad = f"{xcn}{ycn}{zcn}"

    lines1 = [f"{blk}{mov}{xin}{yin}{zin}{rad}{fed}"]
    lines2 = [iu_space]

    return [lines1, lines2]


def gen_k16(data: list) -> list:
    """Genera los códigos para torno suizo K16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, yin, zin, fed, xcn, ycn, zcn, mov, sys, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    xin = "" if xin == "" else f"X{fnum4(xin)}"
    yin = "" if yin == "" else f"Y{fnum4(yin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    mov = "" if mov == "" else swiss_g_codes[f"GIRO {mov}"]
    sys = "" if sys == "" else swiss_g_codes[f"SISTEMA {sys}"]

    if xcn != "" and ycn == "" and zcn == "":
        rad = "" if xcn == "" else f"R{fnum4(xcn)}"
    else:
        xcn = "" if xcn == "" else f"I{fnum4(xcn)}"
        ycn = "" if ycn == "" else f"J{fnum4(ycn)}"
        zcn = "" if zcn == "" else f"K{fnum4(zcn)}"
        rad = f"{xcn}{ycn}{zcn}"

    lines1 = [f"{blk}{mov}{xin}{yin}{zin}{rad}{fed}"]
    lines2 = [iu_space]

    return [lines1, lines2]


def gen_e16(data: list) -> list:
    """Genera los códigos para torno suizo E16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, yin, zin, fed, xcn, ycn, zcn, mov, sys, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    xin = "" if xin == "" else f"X{fnum4(xin)}"
    yin = "" if yin == "" else f"Y{fnum4(yin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    mov = "" if mov == "" else swiss_g_codes[f"GIRO {mov}"]
    sys = "" if sys == "" else swiss_g_codes[f"SISTEMA {sys}"]

    if xcn != "" and ycn == "" and zcn == "":
        rad = "" if xcn == "" else f"R{fnum4(xcn)}"
    else:
        xcn = "" if xcn == "" else f"I{fnum4(xcn)}"
        ycn = "" if ycn == "" else f"J{fnum4(ycn)}"
        zcn = "" if zcn == "" else f"K{fnum4(zcn)}"
        rad = f"{xcn}{ycn}{zcn}"

    lines1 = [f"{blk}{mov}{xin}{yin}{zin}{rad}{fed}"]
    lines2 = [iu_space]

    return [lines1, lines2]


def gen_omni(data: list) -> list:
    """Genera los códigos para torno OmniTurn

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, yin, zin, fed, xcn, ycn, zcn, mov, sys, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    xin = yin if yin != "" else xin
    xin = "" if xin == "" else f"X{fnum4(xin)}"
    yin = "" if yin == "" else f"Y{fnum4(yin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    mov = "" if mov == "" else lathe_g_codes[f"GIRO {mov}"]
    sys = "" if sys == "" else lathe_g_codes[f"SISTEMA {sys}"]

    if xcn != "" and zcn == "":
        rad = "" if xcn == "" else f"R{fnum4(xcn)}"
    else:
        xcn = "" if xcn == "" else f"I{fnum4(xcn)}"
        zcn = "" if zcn == "" else f"K{fnum4(zcn)}"
        rad = f"{xcn}{zcn}"

    lines1 = [f"{blk}{mov}{xin}{zin}{rad}{fed}"]
    lines2 = [iu_space]

    return [lines1, lines2]


def gen_romi(data: list) -> list:
    """Genera los códigos para torno Romi

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, yin, zin, fed, xcn, ycn, zcn, mov, sys, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    xin = yin if yin != "" else xin
    xin = "" if xin == "" else f"X{fnum4(xin)}"
    yin = "" if yin == "" else f"Y{fnum4(yin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    mov = "" if mov == "" else lathe_g_codes[f"GIRO {mov}"]
    sys = "" if sys == "" else lathe_g_codes[f"SISTEMA {sys}"]

    if xcn != "" and zcn == "":
        rad = "" if xcn == "" else f"R{fnum4(xcn)}"
    else:
        xcn = "" if xcn == "" else f"I{fnum4(xcn)}"
        zcn = "" if zcn == "" else f"K{fnum4(zcn)}"
        rad = f"{xcn}{zcn}"

    lines1 = [f"{blk}{mov}{xin}{zin}{rad}{fed}"]
    lines2 = [iu_space]

    return [lines1, lines2]


def gen_hardinge(data: list) -> list:
    """Genera los códigos para torno Hardinge

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, yin, zin, fed, xcn, ycn, zcn, mov, sys, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    xin = yin if yin != "" else xin
    xin = "" if xin == "" else f"X{fnum4(xin)}"
    yin = "" if yin == "" else f"Y{fnum4(yin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    mov = "" if mov == "" else lathe_g_codes[f"GIRO {mov}"]
    sys = "" if sys == "" else lathe_g_codes[f"SISTEMA {sys}"]

    if xcn != "" and zcn == "":
        rad = "" if xcn == "" else f"R{fnum4(xcn)}"
    else:
        xcn = "" if xcn == "" else f"I{fnum4(xcn)}"
        zcn = "" if zcn == "" else f"K{fnum4(zcn)}"
        rad = f"{xcn}{zcn}"

    lines1 = [f"{blk}{mov}{xin}{zin}{rad}{fed}"]
    lines2 = [iu_space]

    return [lines1, lines2]


def gen_mazak(data: list) -> list:
    """Genera los códigos para fresadora Mazak

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, yin, zin, fed, xcn, ycn, zcn, mov, sys, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    xin = "" if xin == "" else f"X{fnum4(xin)}"
    yin = "" if yin == "" else f"Y{fnum4(yin)}"
    zin = "" if zin == "" else f"Z{fnum4(zin)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    mov = "" if mov == "" else mill_g_codes[f"GIRO {mov}"]
    sys = "" if sys == "" else mill_g_codes[f"SISTEMA {sys}"]

    if xcn != "" and ycn == "" and zcn == "":
        rad = "" if xcn == "" else f"R{fnum4(xcn)}"
    else:
        xcn = "" if xcn == "" else f"I{fnum4(xcn)}"
        ycn = "" if ycn == "" else f"J{fnum4(ycn)}"
        zcn = "" if zcn == "" else f"K{fnum4(zcn)}"
        rad = f"{xcn}{ycn}{zcn}"

    lines1 = [f"{blk}{sys}{mov}{xin}{yin}{zin}{rad}{fed}"]
    lines2 = [iu_space]

    return [lines1, lines2]
