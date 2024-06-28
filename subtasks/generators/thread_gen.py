from tools.formatting import *
from tools.compensations import *
from tools.thread_tables import *


def thread_gen(machine, data) -> list:
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

    zin, znd, thd, typ, pos, rgh, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    xnd, zin, znd, dia, xsc, xc1, xc2, pch = thread_data(data)

    rg1 = f"{blk}G01X{fnum3(xnd)}F.003" if rgh == "SÍ" else ""
    rg2 = f"{blk}G00X{fnum3(xsc)}" if rgh == "SÍ" else ""
    rg1 = rg1 if typ == "EXTERNA" else ""
    rg2 = rg2 if typ == "EXTERNA" else ""

    lines1 = [
        f"(-- ROSCA {thd} --)",
        f"{blk}G00X{fnum3(xsc)}",
        rg1,
        rg2,
        f"{blk}G92X{fnum3(xc1)}Z{fnum3(znd)}F{fnum3(pch)}",
        f"{blk}X{fnum3(xc2)}",
        f"{blk}X{fnum3(xnd)}",
    ]
    lines2 = [iu_space for _ in lines1]
    if rg1 == "":
        del lines2[-2:]
    return [lines1, lines2]


def gen_a16(data: list) -> list:
    """Genera los códigos para torno suizo A16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    zin, znd, thd, typ, pos, rgh, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    xnd, zin, znd, dia, xsc, xc1, xc2, pch = thread_data(data)

    rg1 = f"{blk}G01X{fnum3(xnd)}F.003" if rgh == "SÍ" else ""
    rg2 = f"{blk}G00X{fnum3(xsc)}" if rgh == "SÍ" else ""
    rg1 = rg1 if typ == "EXTERNA" else ""
    rg2 = rg2 if typ == "EXTERNA" else ""

    lines1 = [
        f"(-- ROSCA {thd} --)",
        f"{blk}G00X{fnum3(xsc)}",
        rg1,
        rg2,
        f"{blk}G92X{fnum3(xc1)}Z{fnum3(znd)}F{fnum3(pch)}",
        f"{blk}X{fnum3(xc2)}",
        f"{blk}X{fnum3(xnd)}",
    ]
    lines2 = [iu_space for _ in lines1]
    if rg1 == "":
        del lines2[-2:]
    return [lines1, lines2]


def gen_k16(data: list) -> list:
    """Genera los códigos para torno suizo K16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    zin, znd, thd, typ, pos, rgh, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    xnd, zin, znd, dia, xsc, xc1, xc2, pch = thread_data(data)

    rg1 = f"{blk}G01X{fnum3(xnd)}F.003" if rgh == "SÍ" else ""
    rg2 = f"{blk}G00X{fnum3(xsc)}" if rgh == "SÍ" else ""
    rg1 = rg1 if typ == "EXTERNA" else ""
    rg2 = rg2 if typ == "EXTERNA" else ""

    lines1 = [
        f"(-- ROSCA {thd} --)",
        f"{blk}G00X{fnum3(xsc)}",
        rg1,
        rg2,
        f"{blk}G92X{fnum3(xc1)}Z{fnum3(znd)}F{fnum3(pch)}",
        f"{blk}X{fnum3(xc2)}",
        f"{blk}X{fnum3(xnd)}",
    ]
    lines2 = [iu_space for _ in lines1]
    if rg1 == "":
        del lines2[-2:]
    return [lines1, lines2]


def gen_e16(data: list) -> list:
    """Genera los códigos para torno suizo E16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    zin, znd, thd, typ, pos, rgh, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    xnd, zin, znd, dia, xsc, xc1, xc2, pch = thread_data(data)

    rg1 = f"{blk}G01X{fnum3(xnd)}F.003" if rgh == "SÍ" else ""
    rg2 = f"{blk}G00X{fnum3(xsc)}" if rgh == "SÍ" else ""
    rg1 = rg1 if typ == "EXTERNA" else ""
    rg2 = rg2 if typ == "EXTERNA" else ""

    lines1 = [
        f"{blk}G00X{fnum3(xsc)}",
        rg1,
        rg2,
        f"{blk}G92X{fnum3(xc1)}Z{fnum3(znd)}F{fnum3(pch)}",
        f"{blk}X{fnum3(xc2)}",
        f"{blk}X{fnum3(xnd)}",
    ]
    lines2 = [iu_space for _ in lines1]
    if rg1 == "":
        del lines2[-2:]
    return [lines1, lines2]


def gen_omni(data: list) -> list:
    """Genera los códigos para torno OmniTurn

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    zin, znd, thd, typ, pos, rgh, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""
    mod = 0.5 if pos == "POSITIVA" else -0.5

    xnd, zin, znd, dia, xsc, xc1, xc2, pch = thread_data(data)

    rg1 = f"{blk}G01X{fnum3(xnd * mod)}F2" if rgh == "SÍ" else ""
    rg2 = f"{blk}G00X{fnum3(xsc * mod)}" if rgh == "SÍ" else ""
    rg1 = rg1 if typ == "EXTERNA" else ""
    rg2 = rg2 if typ == "EXTERNA" else ""
    fsh = thread_table[thd][3]

    lines1 = [
        f"(-- ROSCA {thd} --)",
        f"{blk}G00X{fnum3(xsc * mod)}",
        rg1,
        rg2,
        f"{blk}G33X{fnum3(xnd * mod)}Z{fnum3(znd)}I{fnum3(fsh)}F{fnum3(pch)}",
    ]
    lines2 = [iu_space for _ in lines1]
    if rg1 == "":
        del lines2[-2:]
    return [lines1, lines2]


def gen_romi(data: list) -> list:
    """Genera los códigos para torno Romi

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    zin, znd, thd, typ, pos, rgh, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""
    mod = 1 if pos == "POSITIVA" else -1

    xnd, zin, znd, dia, xsc, xc1, xc2, pch = thread_data(data)

    rg1 = f"{blk}G01X{fnum3(xnd * mod)}F2" if rgh == "SÍ" else ""
    rg2 = f"{blk}G00X{fnum3(xsc * mod)}" if rgh == "SÍ" else ""
    rg1 = rg1 if typ == "EXTERNA" else ""
    rg2 = rg2 if typ == "EXTERNA" else ""
    hgt = (thread_table[thd][0] - thread_table[thd][1]) / 2
    fsh = thread_table[thd][3]

    xnd = fnum3(xnd * mod)
    znd = fnum3(znd)
    hgt = fnum3(hgt)
    fsh = fnum3(fsh)
    pch = fnum3(pch)

    lines1 = [
        f"(-- ROSCA {thd} --)",
        f"{blk}G00X{fnum3(xsc * mod)}",
        rg1,
        rg2,
        "G76P020000Q00200R.002",
        f"{blk}G76X{xnd}Z{znd}R0P{hgt}Q{fsh}F{pch}",
    ]
    lines2 = [iu_space for _ in lines1]
    if rg1 == "":
        del lines2[-2:]
    return [lines1, lines2]


def gen_hardinge(data: list) -> list:
    """Genera los códigos para torno Hardinge

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    zin, znd, thd, typ, pos, rgh, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""
    mod = 1 if pos == "POSITIVA" else -1

    xnd, zin, znd, dia, xsc, xc1, xc2, pch = thread_data(data)

    rg1 = f"{blk}G01X{fnum3(xnd * mod)}F2" if rgh == "SÍ" else ""
    rg2 = f"{blk}G00X{fnum3(xsc * mod)}" if rgh == "SÍ" else ""
    rg1 = rg1 if typ == "EXTERNA" else ""
    rg2 = rg2 if typ == "EXTERNA" else ""
    hgt = (thread_table[thd][0] - thread_table[thd][1]) / 2
    fsh = thread_table[thd][3]

    xnd = fnum3(xnd * mod)
    znd = fnum3(znd)
    hgt = fnum3(hgt)
    fsh = fnum3(fsh)
    pch = fnum3(pch)

    lines1 = [
        f"(-- ROSCA {thd} --)",
        f"{blk}G00X{fnum3(xsc * mod)}",
        rg1,
        rg2,
        "G76P020000Q00200R.002",
        f"{blk}G76X{xnd}Z{znd}R0P{hgt}Q{fsh}F{pch}",
    ]
    lines2 = [iu_space for _ in lines1]
    if rg1 == "":
        del lines2[-2:]
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


def thread_data(data):
    """Genera los datos de dimensiones de la rosca

    Args:
        data (list): Lista de datos a procesar

    Returns:
        str: Datos procesados
    """

    zin, znd, thd, typ, pos, rgh, dia, blk = data.values()
    blk = "/" if blk else ""

    xin = thread_table[thd][0] if typ == "EXTERNA" else thread_table[thd][1]
    xnd = thread_table[thd][1] if typ == "EXTERNA" else thread_table[thd][0]

    xs1 = 0.01 if typ == "EXTERNA" else -0.01
    xs2 = 0.005 if typ == "EXTERNA" else -0.005
    xsc = xin + xs1
    xc1 = xnd + xs1
    xc2 = xnd + xs2

    pch = thread_table[thd][2]

    return xnd, zin, znd, dia, xsc, xc1, xc2, pch
