from tools.formatting import *


def header_gen(machine: str, data: list) -> list:
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

    prt, prg, dsc, mch, dia, lgt, chk, cof, wrk = data.values()
    iu_space = fspace_ui()
    version = fversion()

    num = ftape(mch, prg)
    xin = f"X{fnum3(dia + 0.02)}"
    zin = "Z0" if cof == "DERECHA" else "Z.315"

    lines1 = [
        "%",
        f"O{num}({prt})",
        f"G50{zin}({mch} - {version})",
        "M06",
        "G99M03S7000",
        f"G00{xin}Z-.02M52",
    ]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]


def gen_a16(data: list) -> list:
    """Genera los códigos para torno suizo A16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    prt, prg, dsc, mch, dia, lgt, chk, cof, wrk = data.values()
    iu_space = fspace_ui()
    version = fversion()

    num = ftape(mch, prg)
    xin = f"X{fnum3(dia + 0.02)}"
    zin = "Z0" if cof == "DERECHA" else "Z.315"

    lines1 = [
        "%",
        f"O{num}({prt})",
        f"G50{zin}({mch} - {version})",
        "M06",
        "M09",
        "G99M03S7000",
        f"G00{xin}Z-.02M52",
    ]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]


def gen_k16(data: list) -> list:
    """Genera los códigos para torno suizo K16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    prt, prg, dsc, mch, dia, lgt, chk, cof, wrk = data.values()
    iu_space = fspace_ui()
    version = fversion()

    num = ftape(mch, prg)
    xin = f"X{fnum3(dia + 0.02)}"
    zin = "Z0" if cof == "DERECHA" else "Z.44"

    lines1 = [
        "%",
        f"O{num}({prt})",
        "$1",
        f"G50{zin}({mch} - {version})",
        "M06",
        "M09",
        "G99M03S1=7000",
        f"G00{xin}Z-.02M52",
        "G600",
    ]
    lines2 = [
        iu_space,
        iu_space,
        "$2",
        "G50Z0",
        "M89",
        iu_space,
        iu_space,
        iu_space,
        "G600",
    ]
    return [lines1, lines2]


def gen_e16(data: list) -> list:
    """Genera los códigos para torno suizo E16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    prt, prg, dsc, mch, dia, lgt, chk, cof, wrk = data.values()
    iu_space = fspace_ui()
    version = fversion()

    num = ftape(mch, prg)
    xin = f"X{fnum3(dia + 0.02)}"
    zin = "Z0" if cof == "DERECHA" else "Z.44"

    lines1 = [
        "%",
        f"O{num}({prt})",
        "$1",
        f"G50{zin}({mch} - {version})",
        "M06",
        "M09",
        "G99M03S1=7000",
        f"G00{xin}Z-.02M52",
        "G600",
    ]
    lines2 = [
        iu_space,
        iu_space,
        "$2",
        "G50Z0",
        "M89",
        iu_space,
        iu_space,
        iu_space,
        "G600",
    ]
    return [lines1, lines2]


def gen_omni(data: list) -> list:
    """Genera los códigos para torno OmniTurn

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    prt, prg, dsc, mch, dia, lgt, chk, cof, wrk = data.values()
    iu_space = fspace_ui()
    version = fversion()

    lines1 = [f"G90G94F300({prg}  {prt})", f"({mch} - {dsc} - {version})"]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]


def gen_romi(data: list) -> list:
    """Genera los códigos para torno Romi

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    prt, prg, dsc, mch, dia, lgt, chk, cof, wrk = data.values()
    iu_space = fspace_ui()
    version = fversion()

    num = ftape(mch, prg)

    lines1 = [
        "%",
        f"O{num}({prt})",
        f"({mch} - {dsc} - {version})",
        "G20G40G90G95",
    ]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]


def gen_hardinge(data: list) -> list:
    """Genera los códigos para torno Hardinge

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    prt, prg, dsc, mch, dia, lgt, chk, cof, wrk = data.values()
    iu_space = fspace_ui()
    version = fversion()

    num = ftape(mch, prg)

    lines1 = [
        "%",
        f"O{num}({prt})",
        f"({mch} - {dsc} - {version})",
        "G65P9150H1.5",
    ]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]


def gen_mazak(data: list) -> list:
    """Genera los códigos para fresadora Mazak

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    prt, prg, dsc, mch, dia, lgt, chk, cof, wrk = data.values()
    iu_space = fspace_ui()
    version = fversion()

    num = ftape(mch, prg)

    lines1 = [
        "%",
        f"O{num}({prt})",
        f"({mch} - {dsc} - {version})",
        "G17G20G40G49G80G90G95",
        wrk,
    ]
    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]
