from tools.formatting import *


def collect_gen(machine: str, data: list) -> list:
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

    lines1, lines2 = [""], [""]

    return [lines1, lines2]


def gen_k16(data: list) -> list:
    """Genera los códigos para torno suizo K16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    clt, chk, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    if chk == 0:
        return [[blank_space], [blank_space]]

    lines2 = (
        [
            f"{blk}M25",
            f"{blk}M72",
            f"{blk}M34T0",
            f"{blk}M73",
            f"{blk}T3000",
            f"{blk}GOTO#100",
        ]
        if clt == "AUTOMATICO"
        else [
            f"{blk}M25",
            f"{blk}G00Z-3.0",
            f"{blk}M16",
            f"{blk}G04U4.0",
            f"{blk}M72",
            f"{blk}M34T0",
            f"{blk}M73",
            f"{blk}T3000",
            f"{blk}GOTO#100",
        ]
    )

    lines1 = [blank_space for _ in lines2]
    return [lines1, lines2]


def gen_e16(data: list) -> list:
    """Genera los códigos para torno suizo E16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    clt, chk, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    if chk == 0:
        return [[blank_space], [blank_space]]

    lines2 = (
        [
            f"{blk}M25",
            f"{blk}M72",
            f"{blk}M34T0",
            f"{blk}M73",
            f"{blk}T3000",
            f"{blk}M99",
        ]
        if clt == "AUTOMATICO"
        else [
            f"{blk}M25",
            f"{blk}G00Z-3.0",
            f"{blk}M16",
            f"{blk}G04U4.0",
            f"{blk}M72",
            f"{blk}M34T0",
            f"{blk}M73",
            f"{blk}T3000",
            f"{blk}M99",
        ]
    )

    lines1 = [blank_space for _ in lines2]
    return [lines1, lines2]


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

    lines1, lines2 = [""], [""]

    return [lines1, lines2]
