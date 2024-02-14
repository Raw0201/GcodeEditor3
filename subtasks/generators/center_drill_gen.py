from tools.cnc_codes import *
from tools.formatting import *


def center_drill_gen(machine, data) -> list:
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

    dpt, fed, xin, yin, zin, rtr, dwl, sde, sys, znd, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    if sde != "$1":
        return [[blank_space], [blank_space]]

    dpt = "" if dpt == "" else f"Z{fnum3(dpt)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    xin = "" if xin == "" else f"X{fnum3(xin)}"
    zin = "" if zin == "" else f"Z{fnum3(zin)}"
    dwl = "" if dwl == 0 else f"{blk}G04U{ffed(dwl)}"
    apx = "" if (xin == "" and zin == "") else f"{blk}G00{xin}{zin}"

    lines1 = [apx, f"{blk}G01{dpt}{fed}", dwl]
    lines2 = [blank_space for _ in lines1]

    if not apx:
        del lines2[-1]
    if not dwl:
        del lines2[-1]

    return [lines1, lines2]


def gen_a16(data: list) -> list:
    """Genera los códigos para torno suizo A16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dpt, fed, xin, yin, zin, rtr, dwl, sde, sys, znd, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[blank_space], [blank_space]]

    dpt = "" if dpt == "" else f"{fnum3(dpt)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    xin = "" if xin == "" else f"X{fnum3(xin)}"
    yin = "" if yin == "" else f"Y{fnum3(yin)}"
    zin = "" if zin == "" else f"Z{fnum3(zin)}"
    axs = "X" if sde == "$3" else "Z"

    dwl = "" if dwl == 0 else f"{blk}G04U{ffed(dwl)}"
    apx = (
        ""
        if (xin == "" and yin == "" and zin == "")
        else f"{blk}G00{xin}{yin}{zin}"
    )

    lines1 = [apx, f"{blk}G01{axs}{dpt}{fed}", dwl]
    lines2 = [blank_space for _ in lines1]

    if not apx:
        del lines2[-1]
    if not dwl:
        del lines2[-1]

    return [lines1, lines2]


def gen_k16(data: list) -> list:
    """Genera los códigos para torno suizo K16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dpt, fed, xin, yin, zin, rtr, dwl, sde, sys, znd, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    dpt = "" if dpt == "" else f"{fnum3(dpt)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    xin = "" if xin == "" else f"X{fnum3(xin)}"
    yin = "" if yin == "" else f"Y{fnum3(yin)}"
    zin = "" if zin == "" else f"Z{fnum3(zin)}"
    axs = "X" if sde == "$3" else "Z"

    dwl = "" if dwl == 0 else f"{blk}G04U{ffed(dwl)}"
    apx = (
        ""
        if (xin == "" and yin == "" and zin == "")
        else f"{blk}G00{xin}{yin}{zin}"
    )

    lines1 = [apx, f"{blk}G01{axs}{dpt}{fed}", dwl]
    lines2 = [blank_space for _ in lines1]

    if not apx:
        del lines2[-1]
    if not dwl:
        del lines2[-1]

    return [lines2, lines1] if sde == "$2" else [lines1, lines2]


def gen_e16(data: list) -> list:
    """Genera los códigos para torno suizo E16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dpt, fed, xin, yin, zin, rtr, dwl, sde, sys, znd, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    dpt = "" if dpt == "" else f"{fnum3(dpt)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    xin = "" if xin == "" else f"X{fnum3(xin)}"
    yin = "" if yin == "" else f"Y{fnum3(yin)}"
    zin = "" if zin == "" else f"Z{fnum3(zin)}"
    axs = "X" if sde == "$3" else "Z"

    dwl = "" if dwl == 0 else f"{blk}G04U{ffed(dwl)}"
    apx = (
        ""
        if (xin == "" and yin == "" and zin == "")
        else f"{blk}G00{xin}{yin}{zin}"
    )

    lines1 = [apx, f"{blk}G01{axs}{dpt}{fed}", dwl]
    lines2 = [blank_space for _ in lines1]

    if not apx:
        del lines2[-1]
    if not dwl:
        del lines2[-1]

    return [lines2, lines1] if sde == "$2" else [lines1, lines2]


def gen_omni(data: list) -> list:
    """Genera los códigos para torno OmniTurn

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dpt, fed, xin, yin, zin, rtr, dwl, sde, sys, znd, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[blank_space], [blank_space]]

    dpt = "" if dpt == "" else f"{fnum3(dpt)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    xin = "" if xin == "" else f"X{fnum3(xin)}"
    zin = "" if zin == "" else f"Z{fnum3(zin)}"
    axs = "X" if sde == "$3" else "Z"

    dwl = "" if dwl == 0 else f"{blk}G04F{ffed(dwl)}"
    apx = "" if xin == "" and zin == "" else f"{blk}{xin}{zin}"

    lines1 = [apx, f"{blk}{axs}{dpt}{fed}", dwl]
    lines2 = [blank_space for _ in lines1]

    if not apx:
        del lines2[-1]
    if not dwl:
        del lines2[-1]

    return [lines1, lines2]


def gen_romi(data: list) -> list:
    """Genera los códigos para torno Romi

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dpt, fed, xin, yin, zin, rtr, dwl, sde, sys, znd, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[blank_space], [blank_space]]

    dpt = "" if dpt == "" else f"{fnum3(dpt)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    xin = "" if xin == "" else f"X{fnum3(xin)}"
    zin = "" if zin == "" else f"Z{fnum3(zin)}"
    axs = "X" if sde == "$3" else "Z"

    dwl = "" if dwl == 0 else f"{blk}G04F{ffed(dwl)}"
    apx = "" if xin == "" and zin == "" else f"{blk}G00{xin}{zin}"

    lines1 = [apx, f"{blk}G01{axs}{dpt}{fed}", dwl]
    lines2 = [blank_space for _ in lines1]

    if not apx:
        del lines2[-1]
    if not dwl:
        del lines2[-1]

    return [lines1, lines2]


def gen_hardinge(data: list) -> list:
    """Genera los códigos para torno Hardinge

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dpt, fed, xin, yin, zin, rtr, dwl, sde, sys, znd, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[blank_space], [blank_space]]

    dpt = "" if dpt == "" else f"{fnum3(dpt)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    xin = "" if xin == "" else f"X{fnum3(xin)}"
    zin = "" if zin == "" else f"Z{fnum3(zin)}"
    axs = "X" if sde == "$3" else "Z"

    dwl = "" if dwl == 0 else f"{blk}G04F{ffed(dwl)}"
    apx = "" if xin == "" and zin == "" else f"{blk}G00{xin}{zin}"

    lines1 = [apx, f"{blk}G01{axs}{dpt}{fed}", dwl]
    lines2 = [blank_space for _ in lines1]

    if not apx:
        del lines2[-1]
    if not dwl:
        del lines2[-1]

    return [lines1, lines2]


def gen_mazak(data: list) -> list:
    """Genera los códigos para fresadora Mazak

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dpt, fed, xin, yin, zin, rtr, dwl, sde, sys, znd, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[blank_space], [blank_space]]

    dpt = "" if dpt == "" else f"Z{fnum3(dpt)}"
    fed = "" if fed == "" else f"F{ffed(fed)}"
    # xin = "" if xin == "" else f"X{fnum3(xin)}"
    # yin = "" if yin == "" else f"Y{fnum3(yin)}"
    # zin = "" if zin == "" else f"Z{fnum3(zin)}"
    rtr = "" if rtr == "" else f"R{fnum3(rtr)}"

    dwl = "" if dwl == 0 else f"{blk}G04U{ffed(dwl)}"
    sys = mill_g_codes[f"SISTEMA {sys}"]
    znd = mill_g_codes[znd]

    lines1 = [f"{blk}{sys}{znd}G81{dpt}{rtr}{fed}", dwl]
    lines2 = [blank_space for _ in lines1]

    if not dwl:
        del lines2[-1]

    return [lines1, lines2]
