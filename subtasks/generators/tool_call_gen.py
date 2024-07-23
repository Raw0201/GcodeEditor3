from tools.formatting import *
from tools.compensations import *
from tools.cnc_codes import *


def tool_call_gen(machine, data) -> list:
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

    tol, typ, dia, spc, sde, xin, yin, zin, mcd, com, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    if sde != "$1":
        return ["", ""]

    tol = kswiss_to_swiss(tol, sde)
    data["Tol"] = tol

    sft = fcom(tol, swiss_compensations)
    sft = f"{blk}G50W-{fnum3(sft)}" if sft else ""
    tol = f"T0{tol}" if tol < 10 else f"T{tol}"
    dia = "" if dia == 0 else f" {fdia(dia)}"
    spc = "" if spc == "-" else f" {spc}"
    zin = f"Z{fnum3(zin)}"
    com = "" if com == "-" else f"(- {com} -)"
    mcd = mcd if mcd == "NO" else swiss_m_codes[mcd]
    mcd = "" if mcd in {"NO", "M140"} else f"{blk}{mcd}{com}"

    lines1 = [
        f"{blk}{tol}00({typ}{dia}{spc})",
        mcd,
        sft,
        f"{blk}G00{zin}{tol}",
    ]
    lines2 = [iu_space for _ in lines1]
    if not sft:
        del lines2[-1]
    if not mcd:
        del lines2[-1]

    return [lines1, lines2]


def gen_a16(data: list) -> list:
    """Genera los códigos para torno suizo A16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    tol, typ, dia, spc, sde, xin, yin, zin, mcd, com, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[iu_space], [iu_space]]

    tol = kswiss_to_swiss(tol, sde)
    data["Tol"] = tol

    sft = fcom(tol, swiss_compensations)
    sft = f"{blk}G50W-{fnum3(sft)}" if sft else ""
    tol = f"T0{tol}" if tol < 10 else f"T{tol}"
    dia = "" if dia == 0 else f" {fdia(dia)}"
    spc = "" if spc == "-" else f" {spc}"
    zin = f"Z{fnum3(zin)}"

    com = "" if com == "-" else f"(- {com} -)"
    mcd = mcd if mcd == "NO" else swiss_m_codes[mcd]
    mcd = "" if mcd in {"NO", "M140"} else f"{blk}{mcd}{com}"

    lines1 = [
        f"{blk}{tol}00({typ}{dia}{spc})",
        mcd,
        sft,
        f"{blk}G00{zin}{tol}",
    ]
    lines2 = [iu_space for _ in lines1]
    if not sft:
        del lines2[-1]
    if not mcd:
        del lines2[-1]

    return [lines1, lines2]


def gen_k16(data: list) -> list:
    """Genera los códigos para torno suizo K16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    tol, typ, dia, spc, sde, xin, yin, zin, mcd, com, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    tol = swiss_to_kswiss(tol, sde)
    data["Tol"] = tol

    sft = fcom(tol, kswiss_compensations)
    sft = f"{blk}G50W-{fnum3(sft)}" if sft else ""
    tol = f"T0{tol}" if tol < 10 else f"T{tol}"
    dia = "" if dia == 0 else f" {fdia(dia)}"
    spc = "" if spc == "-" else f" {spc}"
    zin = f"Z{fnum3(zin)}"
    com = "" if com == "-" else f"(- {com} -)"
    mcd = mcd if mcd == "NO" else swiss_k_m_codes[mcd]
    mcd = "" if mcd == "NO" else f"{blk}{mcd}{com}"

    lines1 = [
        f"{blk}{tol}00({typ}{dia}{spc})",
        mcd,
        sft,
        f"{blk}G00{zin}{tol}",
    ]
    lines2 = [iu_space for _ in lines1]
    if not sft:
        del lines2[-1]
    if not mcd:
        del lines2[-1]

    return [lines2, lines1] if sde == "$2" else [lines1, lines2]


def gen_e16(data: list) -> list:
    """Genera los códigos para torno suizo E16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    tol, typ, dia, spc, sde, xin, yin, zin, mcd, com, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    tol = swiss_to_kswiss(tol, sde)
    data["Tol"] = tol

    sft = fcom(tol, kswiss_compensations)
    sft = f"{blk}G50W-{fnum3(sft)}" if sft else ""
    tol = f"T0{tol}" if tol < 10 else f"T{tol}"
    dia = "" if dia == 0 else f" {fdia(dia)}"
    spc = "" if spc == "-" else f" {spc}"
    zin = f"Z{fnum3(zin)}"
    com = "" if com == "-" else f"(- {com} -)"
    mcd = mcd if mcd == "NO" else swiss_k_m_codes[mcd]
    mcd = "" if mcd == "NO" else f"{blk}{mcd}{com}"

    lines1 = [
        f"{blk}{tol}00({typ}{dia}{spc})",
        mcd,
        sft,
        f"{blk}G00{zin}{tol}",
    ]
    lines2 = [iu_space for _ in lines1]
    if not sft:
        del lines2[-1]
    if not mcd:
        del lines2[-1]

    return [lines2, lines1] if sde == "$2" else [lines1, lines2]


def gen_omni(data: list) -> list:
    """Genera los códigos para torno OmniTurn

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    tol, typ, dia, spc, sde, xin, yin, zin, mcd, com, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[iu_space], [iu_space]]

    tol = f"T{tol}"
    dia = "" if dia == 0 else f" {fdia(dia)}"
    spc = "" if spc == "-" else f" {spc}"
    xin = f"X{fnum3(xin)}"
    zin = f"Z{fnum3(zin)}"
    com = "" if com == "-" else f"(- {com} -)"
    mcd = mcd if mcd == "NO" else omni_m_codes[mcd]
    mcd = "" if mcd in {"NO", "M140"} else f"{blk}{mcd}{com}"

    lines1 = [
        f"{blk}{tol}({typ}{dia}{spc})",
        f"{blk}{xin}{zin}",
        mcd,
    ]
    lines2 = [iu_space for _ in lines1]
    if not mcd:
        del lines2[-1]

    return [lines1, lines2]


def gen_romi(data: list) -> list:
    """Genera los códigos para torno Romi

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    tol, typ, dia, spc, sde, xin, yin, zin, mcd, com, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[iu_space], [iu_space]]

    tol = f"0{tol}" if tol < 10 else f"{tol}"
    dia = "" if dia == 0 else f" {fdia(dia)}"
    spc = "" if spc == "-" else f" {spc}"
    xin = f"X{fnum3(xin)}"
    zin = f"Z{fnum3(zin)}"
    com = "" if com == "-" else f"(- {com} -)"
    mcd = mcd if mcd == "NO" else romi_m_codes[mcd]
    mcd = "" if mcd in {"NO", "M140"} else f"{blk}{mcd}{com}"

    lines1 = [
        f"{blk}T{tol}{tol}G54({typ}{dia}{spc})",
        mcd,
        f"{blk}G00{xin}{zin}M08",
    ]
    lines2 = [iu_space for _ in lines1]
    if not mcd:
        del lines2[-1]

    return [lines1, lines2]


def gen_hardinge(data: list) -> list:
    """Genera los códigos para torno Hardinge

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    tol, typ, dia, spc, sde, xin, yin, zin, mcd, com, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""    

    if sde == "$2":
        return [[iu_space], [iu_space]]

    tol = f"0{tol}" if tol < 10 else f"{tol}"
    dia = "" if dia == 0 else f" {fdia(dia)}"
    spc = "" if spc == "-" else f" {spc}"
    xin = f"X{fnum3(xin)}"
    zin = f"Z{fnum3(zin)}"
    com = "" if com == "-" else f"(- {com} -)"
    mcd = mcd if mcd == "NO" else hardinge_m_codes[mcd]
    mcd = "" if mcd in {"NO", "M140"} else f"{blk}{mcd}{com}"

    lines1 = [
        f"{blk}T{tol}({typ}{dia}{spc})",
        mcd,
        f"{blk}G00{xin}{zin}M08",
    ]
    lines2 = [iu_space for _ in lines1]
    if not mcd:
        del lines2[-1]

    return [lines1, lines2]


def gen_mazak(data: list) -> list:
    """Genera los códigos para fresadora Mazak

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    tol, typ, dia, spc, sde, xin, yin, zin, mcd, com, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[iu_space], [iu_space]]

    tol = f"T0{tol}" if tol < 10 else f"T{tol}"
    dia = "" if dia == 0 else f" {fnum4(dia)}"
    spc = "" if spc == "-" else f" {spc}"
    xin = f"X{fnum4(xin)}"
    yin = f"Y{fnum4(yin)}"
    zin = f"Z{fnum3(zin)}"
    com = "" if com == "-" else f"(- {com} -)"
    mcd = mcd if mcd == "NO" else mazak_m_codes[mcd]
    mcd = "" if mcd in {"NO", "M140"} else f"{blk}{mcd}{com}"

    lines1 = [
        f"{blk}{tol}T00M06({typ}{dia}{spc})",
        mcd,
        f"{blk}G90G00{xin}{yin}{zin}M08",
    ]
    lines2 = [iu_space for _ in lines1]
    if not mcd:
        del lines2[-1]

    return [lines1, lines2]
