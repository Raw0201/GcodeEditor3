from tools.cnc_codes import *
from tools.formatting import *


def spindle_gen(machine: str, data: list) -> list:
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

    spd, rot, sde, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    if sde in ("$2", "$3"):
        return [[iu_space], [iu_space]]

    if spd == 0 and rot != "DETENER":
        return [[f"{blk}G98"], [iu_space]]

    spd = f"S{spd}" if rot in ("NORMAL", "REVERSA") else ""
    rot = swiss_m_codes[f"GIRO {rot}"]

    lines1 = [f"{blk}{rot}{spd}"]
    lines2 = [iu_space]

    return [lines1, lines2]


def gen_a16(data: list) -> list:
    """Genera los códigos para torno suizo A16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    spd, rot, sde, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[iu_space], [iu_space]]

    if spd == 0 and rot != "DETENER":
        return [[f"{blk}G98"], [iu_space]]

    spd = f"S{spd}" if rot in ("NORMAL", "REVERSA") else ""
    rot = f"{rot} {sde}"
    rot = swiss_k_m_codes[f"GIRO {rot}"]

    lines1 = [f"{blk}{rot}{spd}"]
    lines2 = [iu_space]

    return [lines1, lines2]


def gen_k16(data: list) -> list:
    """Genera los códigos para torno suizo K16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    spd, rot, sde, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    if spd == 0 and rot != "DETENER":
        return [[f"{blk}G98"], [iu_space]]
    
    num = sde[-1]
    spd = f"S{num}={spd}" if rot in ("NORMAL", "REVERSA") else ""
    rot = f"{rot} {sde}"
    rot = swiss_k_m_codes[f"GIRO {rot}"]

    lines1 = [f"{blk}{rot}{spd}"]
    lines2 = [iu_space]

    return [lines2, lines1] if sde == "$2" else [lines1, lines2]


def gen_e16(data: list) -> list:
    """Genera los códigos para torno suizo E16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    spd, rot, sde, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    if spd == 0 and rot != "DETENER":
        return [[f"{blk}G98"], [iu_space]]

    num = sde[-1]
    spd = f"S{num}={spd}" if rot in ("NORMAL", "REVERSA") else ""
    rot = f"{rot} {sde}"
    rot = swiss_k_m_codes[f"GIRO {rot}"]

    lines1 = [f"{blk}{rot}{spd}"]
    lines2 = [iu_space]

    return [lines2, lines1] if sde == "$2" else [lines1, lines2]


def gen_omni(data: list) -> list:
    """Genera los códigos para torno OmniTurn

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    spd, rot, sde, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[iu_space], [iu_space]]

    if spd == 0 and rot != "DETENER":
        return [[f"{blk}G94"], [iu_space]]

    spd = f"S{spd}" if rot in ("NORMAL", "REVERSA") else ""

    rot = omni_m_codes[f"GIRO {rot}"]

    lines1 = [f"{blk}{rot}{spd}"]
    lines2 = [iu_space]

    return [lines1, lines2]


def gen_romi(data: list) -> list:
    """Genera los códigos para torno Romi

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    spd, rot, sde, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[iu_space], [iu_space]]

    if spd == 0 and rot != "DETENER":
        return [[f"{blk}G94"], [iu_space]]

    spd = f"S{spd}" if rot in ("NORMAL", "REVERSA") else ""

    rot = romi_m_codes[f"GIRO {rot}"]

    lines1 = [f"{blk}G97{rot}{spd}"]
    lines2 = [iu_space]

    return [lines1, lines2]


def gen_hardinge(data: list) -> list:
    """Genera los códigos para torno Hardinge

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    spd, rot, sde, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[iu_space], [iu_space]]

    if spd == 0 and rot != "DETENER":
        return [[f"{blk}G95"], [iu_space]]

    spd = f"S{spd}" if rot in ("NORMAL", "REVERSA") else ""

    rot = hardinge_m_codes[f"GIRO {rot}"]

    lines1 = [f"{blk}G97{rot}{spd}"]
    lines2 = [iu_space]

    return [lines1, lines2]


def gen_mazak(data: list) -> list:
    """Genera los códigos para fresadora Mazak

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    spd, rot, sde, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[iu_space], [iu_space]]

    if spd == 0 and rot != "DETENER":
        return [[f"{blk}G94"], [iu_space]]

    spd = f"S{spd}" if rot in ("NORMAL", "REVERSA") else ""

    rot = mazak_m_codes[f"GIRO {rot}"]

    lines1 = [f"{blk}{rot}{spd}"]
    lines2 = [iu_space]

    return [lines1, lines2]
