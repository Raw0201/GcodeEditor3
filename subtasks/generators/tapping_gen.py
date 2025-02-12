from tools.cnc_codes import *
from tools.formatting import *
from tools.thread_tables import *


def tapping_gen(machine, data) -> list:
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

    sde = data["Sde"]
    iu_space = fspace_ui()

    if sde == "$1":
        mod_s1 = 1
        lines = tapping_cycle_s1(data, mod_s1)
    elif sde in {"$2", "$3"}:
        lines = [iu_space, iu_space]

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def gen_a16(data: list) -> list:
    """Genera los códigos para torno suizo A16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, sde = data["Xin"], data["Sde"]
    iu_space = fspace_ui()

    if sde == "$1":
        mod_s1 = 1
        lines = tapping_cycle_s1(data, mod_s1)
    elif sde == "$2":
        lines = [iu_space, iu_space]
    elif sde == "$3":
        mod_s3 = 1 if xin > 0 else -1
        lines = tapping_cycle_s3(data, mod_s3)

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def gen_k16(data: list) -> list:
    """Genera los códigos para torno suizo K16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, sde = data["Xin"], data["Sde"]
    iu_space = fspace_ui()

    if sde in {"$1", "$2"}:
        mod_s1 = 1
        lines = tapping_cycle_s1(data, mod_s1)
    elif sde == "$3":
        mod_s3 = 1 if xin > 0 else -1
        lines = tapping_cycle_s3(data, mod_s3)

    lines1, lines2 = lines[0], lines[1]

    return [lines2, lines1] if sde == "$2" else [lines1, lines2]


def gen_e16(data: list) -> list:
    """Genera los códigos para torno suizo E16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, sde = data["Xin"], data["Sde"]
    iu_space = fspace_ui()

    if sde in {"$1", "$2"}:
        mod_s1 = 1
        lines = tapping_cycle_s1(data, mod_s1)
    elif sde == "$3":
        mod_s3 = 1 if xin > 0 else -1
        lines = tapping_cycle_s3(data, mod_s3)

    lines1, lines2 = lines[0], lines[1]

    return [lines2, lines1] if sde == "$2" else [lines1, lines2]


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

    xin, sde = data["Xin"], data["Sde"]
    iu_space = fspace_ui()

    if sde in {"$1", "$3"}:
        mod_s1 = -1
        lines = tapping_cycle_s1m(data, mod_s1)
    elif sde == "$2":
        lines = [iu_space, iu_space]

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def tapping_cycle_s1(data: list, mod: str) -> list:
    """Genera el ciclo de roscado en husillo $1

    Args:
        data (list): Lista de datos a procesar
        mod (str): Modificador de dirección en Z

    Returns:
        list: Lista de líneas de tape
    """

    dpt, thd, xin, yin, zin, rtr, sde, sys, znd, blk = data.values()
    blk = "/" if blk else ""
    iu_space = fspace_ui()

    dpt = f"Z{fnum3(dpt)}"
    pch = f"F{ffed(thread_table[thd][2])}"

    xin = f"X{fnum3(xin)}"
    zin = f"Z{fnum3(zin - (0.03 * mod))}"

    lines1 = [
        f"{blk}(-- ROSCA {thd} --)",
        f"{blk}G00{xin}{zin}",
        f"{blk}G84{dpt}{pch}D1",
        f"{blk}G80",
    ]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]


def tapping_cycle_s3(data: list, mod: str) -> list:
    """Genera el ciclo de roscado en husillo $3

    Args:
        data (list): Lista de datos a procesar
        mod (str): Modificador de dirección en Z

    Returns:
        list: Lista de líneas de tape
    """

    dpt, thd, xin, yin, zin, rtr, sde, sys, znd, blk = data.values()
    blk = "/" if blk else ""
    iu_space = fspace_ui()

    dpt = f"Z{fnum3(dpt)}"
    pch = f"F{ffed(thread_table[thd][2])}"

    xin = f"X{fnum3(xin + (0.06 * mod))}"
    yin = f"Y{fnum3(yin)}"
    zin = f"Z{fnum3(zin)}"

    lines1 = [
        f"{blk}(-- ROSCA {thd} --)",
        f"{blk}G00{xin}{yin}{zin}",
        f"{blk}G88{dpt}R.03{pch}D3S500",
        f"{blk}G80",
    ]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]


def tapping_cycle_s1m(data: list, mod: str) -> list:
    """Genera el ciclo de roscado en Mazak

    Args:
        data (list): Lista de datos a procesar
        mod (str): Modificador de dirección en Z

    Returns:
        list: Lista de líneas de tape
    """

    dpt, thd, xin, yin, zin, rtr, sde, sys, znd, blk = data.values()
    blk = "/" if blk else ""
    iu_space = fspace_ui()

    zin = zin - (0.03 * mod)
    dpt = (
        f"Z{fnum3(dpt * mod)}" if sys == "ABSOLUTO" else f"Z{fnum3((dpt + zin) * mod)}"
    )
    pch = f"F{ffed(thread_table[thd][2])}"

    xin = f"X{fnum3(xin)}"
    yin = f"Y{fnum3(yin)}"
    zin = f"Z{fnum3(zin)}"
    rtr = f"R{fnum3(rtr)}"

    sys = mill_g_codes[f"SISTEMA {sys}"]
    znd = mill_g_codes[znd]

    lines1 = [
        f"{blk}{sys}{znd}G84{dpt}{rtr}{pch}",
    ]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]
