from tools.formatting import *
from tools.compensations import *

def tool_close_gen(machine: str, data: list) -> list:
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

    tol, sde, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    if sde != "$3":
        return ["", ""]

    xin = f"X{fnum3(dia + .02)}"
    sft = fcom(tol, swiss_compensations)
    sft = f"{blk}G50W{fnum3(sft)}" if sft else ""

    if tol in range(21, 34):
        lines1 = [f"{blk}G00Z-.05T00", sft]
    else:
        lines1 = [f"{blk}G00{xin}T00", sft]

    lines2 = [iu_space for _ in lines1]
    if not sft:
        del lines2[-1]
    return [lines1, lines2]


def gen_a16(data: list) -> list:
    """Genera los códigos para torno suizo A16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    tol, sde, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[iu_space], [iu_space]]

    xin = f"X{fnum3(dia + .02)}"
    sft = fcom(tol, swiss_compensations)
    sft = f"{blk}G50W{fnum3(sft)}" if sft else ""

    if tol in range(21, 34):
        lines1 = [f"{blk}G00Z-.05T00", sft]
    else:
        lines1 = [f"{blk}G00{xin}T00", sft]

    lines2 = [iu_space for _ in lines1]
    if not sft:
        del lines2[-1]

    return [lines1, lines2]


def gen_k16(data: list) -> list:
    """Genera los códigos para torno suizo K16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    tol, sde, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    blk = "/" if blk else ""
    xin = f"X{fnum3(dia + .02)}"
    sft = fcom(tol, kswiss_compensations)
    sft = f"{blk}G50W{fnum3(sft)}" if sft else ""

    if tol in range(21, 34):
        lines1 = [f"{blk}G00Z-.05T00", sft]
    else:
        lines1 = [f"{blk}G00{xin}T00", sft]

    lines2 = [iu_space for _ in lines1]
    if not sft:
        del lines2[-1]

    return [lines2, lines1] if sde == "$2" else [lines1, lines2]


def gen_e16(data: list) -> list:
    """Genera los códigos para torno suizo E16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    tol, sde, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    blk = "/" if blk else ""
    xin = f"X{fnum3(dia + .02)}"
    sft = fcom(tol, kswiss_compensations)
    sft = f"{blk}G50W{fnum3(sft)}" if sft else ""

    if tol in range(21, 34):
        lines1 = [f"{blk}G00Z-.05T00", sft]
    else:
        lines1 = [f"{blk}G00{xin}T00", sft]

    lines2 = [iu_space for _ in lines1]
    if not sft:
        del lines2[-1]

    return [lines2, lines1] if sde == "$2" else [lines1, lines2]


def gen_omni(data: list) -> list:
    """Genera los códigos para torno OmniTurn

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    tol, sde, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[iu_space], [iu_space]]

    lines1 = [f"{blk}Z.5F300."]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]


def gen_romi(data: list) -> list:
    """Genera los códigos para torno Romi

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    tol, sde, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[iu_space], [iu_space]]

    lines1 = [f"{blk}G00Z.5"]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]


def gen_hardinge(data: list) -> list:
    """Genera los códigos para torno Hardinge

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    tol, sde, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[iu_space], [iu_space]]

    lines1 = [f"{blk}G00Z.5"]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]


def gen_mazak(data: list) -> list:
    """Genera los códigos para fresadora Mazak

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    tol, sde, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[iu_space], [iu_space]]

    lines1 = [f"{blk}G90G00Z4.0M05M09"]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]
