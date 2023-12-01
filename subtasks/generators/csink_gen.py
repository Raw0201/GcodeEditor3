from tools.cnc_codes import *
from tools.formatting import *

import math


def csink_gen(machine, data) -> list:
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
    blank_space = fspace()

    if sde == "$1":
        mod_s1 = 1
        lines = csink_s1(data, mod_s1)
    elif sde in {"$2", "$3"}:
        lines = [blank_space, blank_space]

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
    blank_space = fspace()

    if sde == "$1":
        mod_s1 = 1
        lines = csink_s1(data, mod_s1)
    elif sde == "$2":
        lines = [blank_space, blank_space]
    elif sde == "$3":
        mod_s3 = 1 if xin > 0 else -1
        lines = csink_s3(data, mod_s3)

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
    blank_space = fspace()

    if sde in {"$1", "$2"}:
        mod_s1 = 1
        lines = csink_s1(data, mod_s1)
    elif sde == "$3":
        mod_s3 = 1 if xin > 0 else -1
        lines = csink_s3(data, mod_s3)

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
    blank_space = fspace()

    if sde in {"$1", "$2"}:
        mod_s1 = 1
        lines = csink_s1(data, mod_s1)
    elif sde == "$3":
        mod_s3 = 1 if xin > 0 else -1
        lines = csink_s3(data, mod_s3)

    lines1, lines2 = lines[0], lines[1]

    return [lines2, lines1] if sde == "$2" else [lines1, lines2]


def gen_omni(data: list) -> list:
    """Genera los códigos para torno OmniTurn

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, sde = data["Xin"], data["Sde"]
    blank_space = fspace()

    if sde == "$1":
        mod_s1 = -1
        lines = csink_s1o(data, mod_s1)
    elif sde == "$2":
        lines = [blank_space, blank_space]
    elif sde == "$3":
        mod_s3 = 1 if xin > 0 else -1
        lines = csink_s3o(data, mod_s3)

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def gen_romi(data: list) -> list:
    """Genera los códigos para torno Romi

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, sde = data["Xin"], data["Sde"]
    blank_space = fspace()

    if sde == "$1":
        mod_s1 = -1
        lines = csink_s1(data, mod_s1)
    elif sde == "$2":
        lines = [blank_space, blank_space]
    elif sde == "$3":
        mod_s3 = 1 if xin > 0 else -1
        lines = csink_s3(data, mod_s3)

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def gen_hardinge(data: list) -> list:
    """Genera los códigos para torno Hardinge

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, sde = data["Xin"], data["Sde"]
    blank_space = fspace()

    if sde == "$1":
        mod_s1 = -1
        lines = csink_s1(data, mod_s1)
    elif sde == "$2":
        lines = [blank_space, blank_space]
    elif sde == "$3":
        mod_s3 = 1 if xin > 0 else -1
        lines = csink_s3(data, mod_s3)

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def gen_mazak(data: list) -> list:
    """Genera los códigos para fresadora Mazak

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    sde = data["Sde"]
    blank_space = fspace()

    if sde == "$1":
        mod_s1 = -1
        lines = csink_s1m(data, mod_s1)
    elif sde in {"$2", "$3"}:
        lines = [blank_space, blank_space]

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def csink_s1(data: list, mod: str) -> list:
    (
        lgt,
        dim,
        ang,
        dia,
        fed,
        dwl,
        xin,
        yin,
        zin,
        rtr,
        sde,
        sys,
        znd,
        blk,
    ) = data.values()

    blk = "/" if blk else ""
    blank_space = fspace()

    angle = math.radians(ang / 2)
    xan = lgt * math.tan(angle)
    total_dia = dim + (xan * 2)
    point = (total_dia / 2) / math.tan(angle)

    znd = point if point < (dia / 2) else (dia / 2) - 0.02
    xnd = znd * math.tan(angle)
    xds = 0 if point < (dia / 2) else total_dia - (xnd * 2)

    fed = f"F{ffed(fed)}"
    dwl = f"G04F{ffed(dwl)}" if dwl > 0 else ""
    zcm = zin

    xin = f"X{fnum3(xin)}"
    zin = f"Z{fnum3(zin - (0.02 * mod))}"
    xds = f"X{fnum3(xds)}" if xds > 0 else ""
    zds = f"Z{fnum3(((znd - lgt - 0.02) * mod + zcm))}"
    znd = f"Z{fnum3(znd * mod + zcm)}"

    lines1 = [
        f"{blk}G00{xin}{zin}",
        f"{blk}G01{xds}{zds}F.03",
        f"{blk}G01{znd}{fed}",
        dwl,
        f"{blk}G00{zin}",
    ]
    lines2 = [blank_space for _ in lines1]
    if not dwl:
        del lines2[-1]

    return [lines1, lines2]


def csink_s1m(data: list, mod: str) -> list:
    (
        lgt,
        dim,
        ang,
        dia,
        fed,
        dwl,
        xin,
        yin,
        zin,
        rtr,
        sde,
        sys,
        znd,
        blk,
    ) = data.values()

    blk = "/" if blk else ""
    blank_space = fspace()

    angle = math.radians(ang / 2)
    xan = lgt * math.tan(angle)
    total_dia = dim + (xan * 2)
    point = (total_dia / 2) / math.tan(angle)

    fed = f"F{ffed(fed)}"
    dwl = f"E{int(dwl * 1000)}" if dwl > 0 else ""

    zin = zin - (0.02 * mod)
    zdp = (
        f"Z{fnum3(point * mod)}"
        if sys == "ABSOLUTO"
        else f"Z{fnum3((point + zin) * mod)}"
    )
    xin = f"X{fnum3(xin)}"
    yin = f"Y{fnum3(yin)}"
    zin = f"Z{fnum3(zin)}"
    rtr = f"R{fnum3(rtr)}"

    sys = mill_g_codes[f"SISTEMA {sys}"]
    znd = mill_g_codes[znd]

    lines1 = [
        f"{blk}G00{xin}{yin}{zin}",
        f"{blk}{sys}{znd}G82{zdp}{rtr}{dwl}{fed}",
    ]
    lines2 = [blank_space for _ in lines1]

    return [lines1, lines2]


def csink_s3(data: list, mod: str) -> list:
    (
        lgt,
        dim,
        ang,
        dia,
        fed,
        dwl,
        xin,
        yin,
        zin,
        rtr,
        sde,
        sys,
        znd,
        blk,
    ) = data.values()

    blk = "/" if blk else ""
    blank_space = fspace()

    angle = math.radians(ang / 2)
    xan = lgt * math.tan(angle)
    total_dia = dim + (xan * 2)
    point = (total_dia / 2) / math.tan(angle)

    fed = f"F{ffed(fed)}"
    dwl = f"G04F{ffed(dwl)}" if dwl > 0 else ""

    xds = f"X{fnum3(xin - ((point - lgt - .02) * 2 * mod))}"
    xnd = f"X{fnum3(xin - (point * 2 * mod))}"
    xin = f"X{fnum3(xin + (0.04 * mod))}"
    yin = f"Y{fnum3(yin)}"
    zin = f"Z{fnum3(zin)}"

    lines1 = [
        f"{blk}G00{xin}{yin}{zin}",
        f"{blk}G01{xds}F.03",
        f"{blk}G01{xnd}{fed}",
        dwl,
        f"{blk}G00{xin}",
    ]
    lines2 = [blank_space for _ in lines1]
    if not dwl:
        del lines2[-1]

    return [lines1, lines2]


def csink_s1o(data: list, mod: str) -> list:
    (
        lgt,
        dim,
        ang,
        dia,
        fed,
        dwl,
        xin,
        yin,
        zin,
        rtr,
        sde,
        sys,
        znd,
        blk,
    ) = data.values()

    blk = "/" if blk else ""
    blank_space = fspace()

    angle = math.radians(ang / 2)
    xan = lgt * math.tan(angle)
    total_dia = dim + (xan * 2)
    point = (total_dia / 2) / math.tan(angle)

    znd = point if point < (dia / 2) else (dia / 2) - 0.02
    xnd = znd * math.tan(angle)
    xds = 0 if point < (dia / 2) else total_dia - (xnd * 2)

    fed = f"F{ffed(fed)}"
    dwl = f"G04F{ffed(dwl)}" if dwl > 0 else ""

    xin = f"X{fnum3(xin)}"
    zin = f"Z{fnum3(zin - (0.02 * mod))}"
    xds = f"X{fnum3(xds / 2)}" if xds > 0 else ""
    zds = f"Z{fnum3((znd - lgt - 0.02) * mod)}"
    znd = f"Z{fnum3(znd * mod)}"

    lines1 = [
        f"{blk}{xin}{zin}F300.",
        f"{blk}{xds}{zds}F20.",
        f"{blk}{znd}{fed}",
        dwl,
        f"{blk}{zin}F300.",
    ]
    lines2 = [blank_space for _ in lines1]
    if not dwl:
        del lines2[-1]

    return [lines1, lines2]


def csink_s3o(data: list, mod: str) -> list:
    (
        lgt,
        dim,
        ang,
        dia,
        fed,
        dwl,
        xin,
        yin,
        zin,
        rtr,
        sde,
        sys,
        znd,
        blk,
    ) = data.values()

    blk = "/" if blk else ""
    blank_space = fspace()

    angle = math.radians(ang / 2)
    xan = lgt * math.tan(angle)
    total_dia = dim + (xan * 2)
    point = (total_dia / 2) / math.tan(angle)

    fed = f"F{ffed(fed)}"
    dwl = f"G04F{ffed(dwl)}" if dwl > 0 else ""

    xds = f"X{fnum3(xin - ((point - lgt - .02) * 2 * mod))}"
    xnd = f"X{fnum3(xin - (point * 2 * mod))}"
    xin = f"X{fnum3(xin + (0.04 * mod))}"
    yin = f"Y{fnum3(yin)}"
    zin = f"Z{fnum3(zin)}"

    lines1 = [
        f"{blk}{xin}{zin}F300.",
        f"{blk}{xds}F20.",
        f"{blk}{xnd}{fed}",
        dwl,
        f"{blk}{xin}F300.",
    ]
    lines2 = [blank_space for _ in lines1]
    if not dwl:
        del lines2[-1]

    return [lines1, lines2]
