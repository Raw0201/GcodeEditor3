from tools.formatting import *


def end_gen(machine: str, data: list) -> list:
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

    mta, bar, lgt, chk, cof, tol, typ, dia, spc, xps, yps, zps = data.values()
    blank_space = fspace()

    if mta:
        zin = "Z0" if cof == "DERECHA" else "Z.315"
        lines1 = [
            f"G00X-.1{zin}T00",
            "M56",
            "M02",
            "M99",
            "%",
        ]
    else:
        lines1 = [
            "M99",
            "%",
        ]
    lines2 = [blank_space for _ in lines1]

    return [lines1, lines2]


def gen_a16(data: list) -> list:
    """Genera los códigos para torno suizo A16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    mta, bar, lgt, chk, cof, tol, typ, dia, spc, xps, yps, zps = data.values()
    blank_space = fspace()

    if mta:
        zin = "Z0" if cof == "DERECHA" else "Z.315"
        lines1 = [
            "M08",
            "M08",
            "/M109Q8999",
            "M09",
            "  ",
            f"G00X-.1{zin}T00",
            "M56",
            "M02",
            "M99",
            "%",
        ]
    else:
        lines1 = [
            "M99",
            "%",
        ]
    lines2 = [blank_space for _ in lines1]

    return [lines1, lines2]


def gen_k16(data: list) -> list:
    """Genera los códigos para torno suizo K16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    mta, bar, lgt, chk, cof, tol, typ, dia, spc, xps, yps, zps = data.values()
    blank_space = fspace()

    if mta:
        zin = "Z0" if cof == "DERECHA" else "Z.44"
        bar_dia = fparam(bar)
        mch_lgt = fparam(lgt + 0.2)
        rem_mat = fparam(lgt - chk) if chk > 0 else fparam(0)
        bck_typ = fparam(143) if chk > 0 else fparam(141)

        lines1 = [
            "M08",
            "M08",
            "/M109Q8999",
            "M09",
            "  ",
            f"G00X-.1{zin}T00",
            "  ",
            "G600",
            "G999",
            "N999",
            "M56",
            "M02",
            "M99",
            "  ",
            blank_space,
            blank_space,
            blank_space,
            blank_space,
        ]
        lines2 = [
            "$0",
            "D",
            f"#016={bar_dia}",
            "#020=0000000200",
            f"#024={mch_lgt}",
            "#028=0000001000",
            "#032=0000001000",
            "#036=0003000000",
            "#040=0000000050",
            "#044=-000001000",
            f"#048={rem_mat}",
            "#052=0000008000",
            "#056=0000101000",
            "#060=0000121000",
            f"#064={bck_typ}",
            "#068=0000000000",
            "#072=0000000000",
            "%",
        ]
    else:
        lines1 = [
            "M99",
            "%",
        ]
        lines2 = [blank_space for _ in lines1]

    return [lines1, lines2]


def gen_e16(data: list) -> list:
    """Genera los códigos para torno suizo E16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    mta, bar, lgt, chk, cof, tol, typ, dia, spc, xps, yps, zps = data.values()
    blank_space = fspace()

    if mta:
        zin = "Z0" if cof == "DERECHA" else "Z.44"
        bar_dia = fparam(bar)
        mch_lgt = fparam(lgt + 0.2)
        rem_mat = fparam(lgt - chk) if chk > 0 else fparam(0)
        bck_typ = fparam(421) if chk > 0 else fparam(422)

        lines1 = [
            "M08",
            "M08",
            "/M109Q8999",
            "M09",
            "  ",
            f"G00X-.1{zin}T00",
            "  ",
            "G600",
            "G999",
            "N999",
            "M56",
            "M02",
            "M99",
            "  ",
            blank_space,
            blank_space,
            blank_space,
            blank_space,
            blank_space,
            blank_space,
        ]
        lines2 = [
            "$0",
            "A2-KE-1-16-7-P-M",
            f"#814={bar_dia}",
            "#815=0000000200",
            "#816=0000001000",
            "#817=0003000000",
            "#822=0000000050",
            "#824=-000001000",
            f"#818={mch_lgt}",
            "#819=0000001000",
            "#820=0000000000",
            f"#821={rem_mat}",
            "#990=0015728643",
            "#991=0000400000",
            f"#992={bck_typ}",
            "#893=0000001000",
            "#25119=0000000000",
            "#26029=0000020000",
            "#25115=0000000000",
            "%",
        ]
    else:
        lines1 = [
            "M99",
            "%",
        ]
        lines2 = [blank_space for _ in lines1]

    return [lines1, lines2]


def gen_omni(data: list) -> list:
    """Genera los códigos para torno OmniTurn

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    mta, bar, lgt, chk, cof, tol, typ, dia, spc, xps, yps, zps = data.values()
    blank_space = fspace()

    if mta:
        tol = f"T{tol}"
        dia = "" if dia == 0 else f" {fdia(dia)}"
        spc = "" if spc == "-" else f" {spc}"
        xin = f"X{fnum3(xps)}"
        zin = f"Z{fnum3(zps)}"

        lines1 = lines1 = [f"{tol}({typ}{dia}{spc})", f"{xin}{zin}", "M30"]
    else:
        lines1 = ["M99"]

    lines2 = [blank_space for _ in lines1]

    return [lines1, lines2]


def gen_romi(data: list) -> list:
    """Genera los códigos para torno Romi

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    mta, bar, lgt, chk, cof, tol, typ, dia, spc, xps, yps, zps = data.values()
    blank_space = fspace()

    if mta:
        tol = f"0{tol}" if tol < 10 else f"{tol}"
        dia = "" if dia == 0 else f" {fdia(dia)}"
        spc = "" if spc == "-" else f" {spc}"
        xin = f"X{fnum3(xps)}"
        zin = f"Z{fnum3(zps)}"

        lines1 = [
            f"T{tol}{tol}G54({typ}{dia}{spc})",
            f"G00{xin}{zin}",
            "M76",
            "M24",
            "M30",
            "%",
        ]
    else:
        lines1 = [
            "M99",
            "%",
        ]

    lines2 = [blank_space for _ in lines1]

    return [lines1, lines2]


def gen_hardinge(data: list) -> list:
    """Genera los códigos para torno Hardinge

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    mta, bar, lgt, chk, cof, tol, typ, dia, spc, xps, yps, zps = data.values()
    blank_space = fspace()

    if mta:
        tol = f"0{tol}" if tol < 10 else f"{tol}"
        dia = "" if dia == 0 else f" {fdia(dia)}"
        spc = "" if spc == "-" else f" {spc}"
        xin = f"X{fnum3(xps)}"
        zin = f"Z{fnum3(zps)}"

        lines1 = [
            f"T{tol}({typ}{dia}{spc})",
            f"G00{xin}{zin}M08",
            "G10P08U.00001W.00001",
            "M21",
            "M30",
            "%",
        ]
    else:
        lines1 = [
            "M99",
            "%",
        ]

    lines2 = [blank_space for _ in lines1]

    return [lines1, lines2]


def gen_mazak(data: list) -> list:
    """Genera los códigos para fresadora Mazak

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    mta, bar, lgt, chk, cof, tol, typ, dia, spc, xps, yps, zps = data.values()
    blank_space = fspace()

    if mta:

        tol = f"T0{tol}" if tol < 10 else f"T{tol}"
        dia = "" if dia == 0 else f" {fdia(dia)}"
        spc = "" if spc == "-" else f" {spc}"

        lines1 = [
            f"{tol}T00M06({typ}{dia}{spc})",
            "M30",
            "%",
        ]
    else:
        lines1 = [
            "M99",
            "%",
        ]

    lines2 = [blank_space for _ in lines1]

    return [lines1, lines2]
