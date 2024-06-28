from tools.formatting import *


def header_sub_gen(machine: str, data: list) -> list:
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

    prg, mnp, dsc, plt, tol, typ, dia, spc, mch, lgt = data.values()
    iu_space = fspace_ui()

    num = ftape(mch, prg)
    dsc = "" if dsc == "-" else f" {dsc}"

    lines1 = ["%", f"O{num}(SUB{dsc})"]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]


def gen_a16(data: list) -> list:
    """Genera los códigos para torno suizo A16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    prg, mnp, dsc, plt, tol, typ, dia, spc, mch, lgt = data.values()
    iu_space = fspace_ui()

    num = ftape(mch, prg)
    dsc = "" if dsc == "-" else f" {dsc}"

    lines1 = ["%", f"O{num}(SUB{dsc})"]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]


def gen_k16(data: list) -> list:
    """Genera los códigos para torno suizo K16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    prg, mnp, dsc, plt, tol, typ, dia, spc, mch, lgt = data.values()
    iu_space = fspace_ui()

    num = ftape(mch, prg)
    dsc = "" if dsc == "-" else f" {dsc}"

    lines1 = ["%", f"O{num}(SUB{dsc})"]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]


def gen_e16(data: list) -> list:
    """Genera los códigos para torno suizo E16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    prg, mnp, dsc, plt, tol, typ, dia, spc, mch, lgt = data.values()
    iu_space = fspace_ui()

    num = ftape(mch, prg)
    dsc = "" if dsc == "-" else f" {dsc}"

    lines1 = ["%", f"O{num}(SUB{dsc})"]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]


def gen_omni(data: list) -> list:
    """Genera los códigos para torno OmniTurn

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    prg, mnp, dsc, plt, tol, typ, dia, spc, mch, lgt = data.values()
    iu_space = fspace_ui()

    num = ftape(mch, prg)
    dsc = "" if dsc == "-" else f" {dsc}"

    lines1 = [f"O{num}(SUB{dsc})"]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]


def gen_romi(data: list) -> list:
    """Genera los códigos para torno Romi

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    prg, mnp, dsc, plt, tol, typ, dia, spc, mch, lgt = data.values()
    iu_space = fspace_ui()

    num = ftape(mch, prg)
    dsc = "" if dsc == "-" else f" {dsc}"

    lines1 = ["%", f"O{num}(SUB{dsc})"]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]


def gen_hardinge(data: list) -> list:
    """Genera los códigos para torno Hardinge

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    prg, mnp, dsc, plt, tol, typ, dia, spc, mch, lgt = data.values()
    iu_space = fspace_ui()

    num = ftape(mch, prg)
    dsc = "" if dsc == "-" else f" {dsc}"

    lines1 = ["%", f"O{num}(SUB{dsc})"]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]


def gen_mazak(data: list) -> list:
    """Genera los códigos para fresadora Mazak

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    prg, mnp, dsc, plt, tol, typ, dia, spc, mch, lgt = data.values()
    iu_space = fspace_ui()

    num = ftape(mch, prg)
    dia = fdia(dia)
    spc = "" if spc == "-" else f" {spc}"

    lines1 = [
        "%",
        f"O{num}({typ} {dia}{spc})",
    ]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]
