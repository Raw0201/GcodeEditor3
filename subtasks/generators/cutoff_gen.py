from tools.formatting import *
from tools.compensations import *
from tools.thread_tables import *


def cutoff_gen(machine, data) -> list:
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

    dia, cfr, lgt, chk, cof, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    com = fnum3(0.375) if cof == "IZQUIERDA" else fnum3(0.06)
    xin = f"X{fnum3(dia + 0.01)}"
    zin = f"Z{fnum3(lgt - cfr - 0.005)}"
    xnd = f"X{fnum3(dia - (cfr * 2))}"
    znd = f"Z{fnum3(lgt)}"

    lines1 = [
        f"{blk}T1111(CUCHILLA TRONZAR)",
        f"{blk}M32",
        f"{blk}G50W-{com}",
        f"{blk}G00{zin}",
        f"{blk}{xin}",
        f"{blk}G01{xnd}{znd}F.002",
        f"{blk}X0F.001",
        f"{blk}X-.1F.005",
        f"{blk}M33",
        f"{blk}M7",
        f"{blk}G50W{com}",
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

    dia, cfr, lgt, chk, cof, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    com = fnum3(0.375) if cof == "IZQUIERDA" else fnum3(0.06)
    xin = f"X{fnum3(dia + 0.01)}"
    zin = f"Z{fnum3(lgt - cfr - 0.005)}"
    xnd = f"X{fnum3(dia - (cfr * 2))}"
    znd = f"Z{fnum3(lgt)}"

    lines1 = [
        f"{blk}T1111(CUCHILLA TRONZAR)",
        f"{blk}M32",
        f"{blk}G50W-{com}",
        f"{blk}G00{zin}",
        f"{blk}{xin}",
        f"{blk}G01{xnd}{znd}F.002",
        f"{blk}X0F.001",
        f"{blk}X-.1F.005",
        f"{blk}M33",
        f"{blk}M7",
        f"{blk}G50W{com}",
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

    dia, cfr, lgt, chk, cof, blk = data.values()

    if chk == 0:
        lines1 = cutoff_k16s1_basket(data)
        lines2 = cutoff_k16s2_basket(data)
    else:
        lines1 = cutoff_k16s1_spindle(data)
        lines2 = cutoff_k16s2_spindle(data)

    return [lines1, lines2]


def gen_e16(data: list) -> list:
    """Genera los códigos para torno suizo E16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dia, cfr, lgt, chk, cof, blk = data.values()

    if chk == 0:
        lines1 = cutoff_e16s1_basket(data)
        lines2 = cutoff_e16s2_basket(data)
    else:
        lines1 = cutoff_e16s1_spindle(data)
        lines2 = cutoff_e16s2_spindle(data)

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


def cutoff_k16s1_basket(data: list) -> list:
    """Tronzado en torno K16 $1 con canasta

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dia, cfr, lgt, chk, cof, blk = data.values()
    iu_space = fspace_ui()
    tape_space = fspace_tape()
    blk = "/" if blk else ""

    com = fnum3(0.500) if cof == "IZQUIERDA" else fnum3(0.06)
    xin = f"{fnum3(dia + 0.01)}"
    zin = f"{fnum3(lgt - cfr - 0.005)}"
    xnd = f"{fnum3(dia - (cfr * 2))}"
    znd = f"{fnum3(lgt)}"

    return [
        f"{blk}G650",
        tape_space,
        f"{blk}T0100(CUCHILLA TRONZAR)",
        f"{blk}G50W-{com}",
        f"{blk}G00Z{zin}T01",
        f"{blk}X{xin}",
        f"{blk}G01X{xnd}Z{znd}F.002",
        f"{blk}X0F.001",
        f"{blk}X-.1F.005",
        f"{blk}M07",
        f"{blk}G50W{com}",
        tape_space,
        f"{blk}!2L1",
        iu_space,
        iu_space,
        iu_space,
        iu_space,
        iu_space,
        iu_space,
        iu_space,
        iu_space,
        iu_space,
        iu_space,
    ]


def cutoff_k16s2_basket(data: list) -> list:
    """Tronzado en torno K16 $2 con canasta

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dia, cfr, lgt, chk, cof, blk = data.values()
    iu_space = fspace_ui()
    tape_space = fspace_tape()
    blk = "/" if blk else ""

    return [
        f"{blk}#100=10",
        f"{blk}GOTO100",
        f"{blk}N10",
        tape_space,
        f"{blk}G650",
        f"{blk}M320",
        tape_space,
        f"{blk}!1L1",
        tape_space,
        f"{blk}G999",
        f"{blk}#100=20",
        f"{blk}GOTO100",
        f"{blk}N20",
        f"{blk}M53",
        f"{blk}N999",
        f"{blk}M02",
        f"{blk}M99",
        tape_space,
        f"{blk}N100",
        tape_space,
        f"{blk}M34H8000S8000",
        f"{blk}T3000",
        f"{blk}GOTO#100",
    ]


def cutoff_k16s1_spindle(data: list) -> list:
    """Tronzado en torno K16 $1 con husillo

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dia, cfr, lgt, chk, cof, blk = data.values()
    iu_space = fspace_ui()
    tape_space = fspace_tape()
    blk = "/" if blk else ""

    com = 0.500 if cof == "IZQUIERDA" else 0.06
    xin = f"{fnum3(dia + 0.01)}"
    zin = f"{fnum3(lgt - cfr - 0.005)}"
    xnd = f"{fnum3(dia - (cfr * 2))}"
    znd = f"{fnum3(lgt)}"
    sec = com + 0.06 if com > 0.06 else 0
    zsc = f"{fnum3(float(znd) + sec)}"
    com = fnum3(com)

    return [
        f"{blk}T0100(CUCHILLA TRONZAR)",
        f"{blk}G00Z{zsc}T01",
        tape_space,
        f"{blk}!2L1",
        tape_space,
        f"{blk}S1=3000M03",
        f"{blk}S2=3000M24",
        tape_space,
        f"{blk}G814",
        f"{blk}G650M1",
        tape_space,
        f"{blk}!2L2",
        tape_space,
        f"{blk}G50W-{com}",
        f"{blk}G00Z{zin}",
        f"{blk}X{xin}",
        f"{blk}G01X{xnd}Z{znd}F.002",
        f"{blk}X0F.001",
        f"{blk}X-.1F.005",
        tape_space,
        f"{blk}M7",
        f"{blk}G50W{com}",
        tape_space,
        f"{blk}G813",
        f"{blk}G600",
        iu_space,
        iu_space,
        iu_space,
        iu_space,
        iu_space,
        iu_space,
    ]


def cutoff_k16s2_spindle(data: list) -> list:
    """Tronzado en torno K16 $2 con husillo

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dia, cfr, lgt, chk, cof, blk = data.values()
    iu_space = fspace_ui()
    tape_space = fspace_tape()
    blk = "/" if blk else ""
    chk = f"{fnum3(chk)}"

    return [
        f"{blk}#100=10",
        f"{blk}GOTO100",
        f"{blk}N10",
        tape_space,
        f"{blk}!1L1",
        tape_space,
        f"{blk}G650",
        tape_space,
        f"{blk}M16",
        f"{blk}M72",
        f"{blk}G00Z-.02",
        f"{blk}M77",
        f"{blk}G98G01Z{chk}F200.(SUJETA PIEZA)",
        f"{blk}M15",
        f"{blk}M73",
        f"{blk}G99",
        tape_space,
        f"{blk}!1L2",
        tape_space,
        f"{blk}G600",
        tape_space,
        f"{blk}G999",
        f"{blk}#100=20",
        f"{blk}GOTO100",
        tape_space,
        f"{blk}N20",
        f"{blk}N999",
        f"{blk}M02",
        f"{blk}M99",
        tape_space,
        f"{blk}N100",
    ]


def cutoff_e16s1_basket(data: list) -> list:
    """Tronzado en torno E16 $1 con canasta

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dia, cfr, lgt, chk, cof, blk = data.values()
    iu_space = fspace_ui()
    tape_space = fspace_tape()
    blk = "/" if blk else ""

    com = fnum3(0.500) if cof == "IZQUIERDA" else fnum3(0.06)
    xin = f"{fnum3(dia + 0.01)}"
    zin = f"{fnum3(lgt - cfr - 0.005)}"
    xnd = f"{fnum3(dia - (cfr * 2))}"
    znd = f"{fnum3(lgt)}"

    return [
        f"{blk}T0100(TRONZADO)",
        f"{blk}M320",
        f"{blk}G50W-{com}",
        f"{blk}G00Z{zin}T01",
        f"{blk}X{xin}",
        f"{blk}G01X{xnd}Z{znd}F.002",
        f"{blk}X0F.001",
        f"{blk}X-.1F.005",
        f"{blk}M07",
        f"{blk}G50W{com}",
        tape_space,
        f"{blk}!2L1",
        f"{blk}G600",
    ]


def cutoff_e16s2_basket(data: list) -> list:
    """Tronzado en torno E16 $2 con canasta

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dia, cfr, lgt, chk, cof, blk = data.values()
    iu_space = fspace_ui()
    tape_space = fspace_tape()
    blk = "/" if blk else ""

    return [
        tape_space,
        f"{blk}!1L1",
        tape_space,
        f"{blk}M34",
        tape_space,
        f"{blk}G600",
        f"{blk}G999",
        f"{blk}N999",
        f"{blk}M02",
        f"{blk}M99",
        tape_space,
        iu_space,
        iu_space,
    ]


def cutoff_e16s1_spindle(data: list) -> list:
    """Tronzado en torno E16 $1 con husillo

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dia, cfr, lgt, chk, cof, blk = data.values()
    iu_space = fspace_ui()
    tape_space = fspace_tape()
    blk = "/" if blk else ""

    com = 0.500 if cof == "IZQUIERDA" else 0.06
    xin = f"{fnum3(dia + 0.01)}"
    zin = f"{fnum3(lgt - cfr - 0.005)}"
    xnd = f"{fnum3(dia - (cfr * 2))}"
    znd = f"{fnum3(lgt)}"
    sec = com + 0.06 if com > 0.06 else 0
    zsc = f"{fnum3(float(znd) + sec)}"
    com = fnum3(com)

    return [
        f"{blk}T0100(CUCHILLA TRONZAR)",
        f"{blk}G00Z{zsc}T01",
        tape_space,
        f"{blk}!2L1",
        tape_space,
        f"{blk}S1=3000M03",
        f"{blk}S2=3000M24",
        tape_space,
        f"{blk}G814",
        f"{blk}G650M1",
        tape_space,
        f"{blk}!2L2",
        tape_space,
        f"{blk}G50W-{com}",
        f"{blk}G00Z{zin}",
        f"{blk}X{xin}",
        f"{blk}G01X{xnd}Z{znd}F.002",
        f"{blk}X0F.001",
        f"{blk}X-.1F.005",
        tape_space,
        f"{blk}M7",
        f"{blk}G50W{com}",
        tape_space,
        f"{blk}G813",
        f"{blk}G600",
        iu_space,
        iu_space,
        iu_space,
        iu_space,
        iu_space,
        iu_space,
    ]


def cutoff_e16s2_spindle(data: list) -> list:
    """Tronzado en torno E16 $1 con husillo

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dia, cfr, lgt, chk, cof, blk = data.values()
    iu_space = fspace_ui()
    tape_space = fspace_tape()
    blk = "/" if blk else ""
    chk = f"{fnum3(chk)}"

    return [
        f"{blk}M98H1",
        f"{blk}!1L1",
        tape_space,
        f"{blk}G650",
        tape_space,
        f"{blk}M16",
        f"{blk}M72",
        f"{blk}G00Z-.02",
        f"{blk}M77",
        f"{blk}G98G01Z{chk}F200.(SUJETA PIEZA)",
        f"{blk}M15",
        f"{blk}M73",
        f"{blk}G99",
        tape_space,
        f"{blk}!1L2",
        tape_space,
        f"{blk}G600",
        tape_space,
        f"{blk}G999",
        f"{blk}M98H1",
        tape_space,
        f"{blk}N999",
        f"{blk}M02",
        f"{blk}M99",
        tape_space,
        f"{blk}N1",
        iu_space,
        iu_space,
        iu_space,
        iu_space,
        iu_space,
    ]
