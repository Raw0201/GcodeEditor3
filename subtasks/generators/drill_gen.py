from tools.cnc_codes import *
from tools.formatting import *

import math


def drill_gen(machine, data) -> list:
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

    cyl, sde = data["Cyl"], data["Sde"]
    blank_space = fspace()
    mod_s1 = 1

    if sde in {"$2", "$3"}:
        lines = [blank_space, blank_space]
    if cyl == "CICLO DE PERFORADO":
        lines = drilling_cycle_s1(data, mod_s1)
    elif cyl == "CORTES INDIVIDUALES":
        lines = drilling_cuts_s1(data, mod_s1)

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def gen_a16(data: list) -> list:
    """Genera los códigos para torno suizo A16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, cyl, sde = data["Xin"], data["Cyl"], data["Sde"]
    blank_space = fspace()
    mod_s1 = 1
    mod_s3 = 1 if xin > 0 else -1

    if sde == "$2":
        lines = [blank_space, blank_space]
    elif sde == "$3":
        lines = drilling_cuts_s3(data, mod_s3)
    elif cyl == "CICLO DE PERFORADO":
        lines = drilling_cycle_s1(data, mod_s1)
    elif cyl == "CORTES INDIVIDUALES":
        lines = drilling_cuts_s1(data, mod_s1)

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def gen_k16(data: list) -> list:
    """Genera los códigos para torno suizo K16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, cyl, sde = data["Xin"], data["Cyl"], data["Sde"]
    blank_space = fspace()
    mod_s1 = 1
    mod_s3 = 1 if xin > 0 else -1

    if sde == "$3":
        lines = drilling_cuts_s3(data, mod_s3)
    elif cyl == "CICLO DE PERFORADO":
        lines = drilling_cycle_s1(data, mod_s1)
    elif cyl == "CORTES INDIVIDUALES":
        lines = drilling_cuts_s1(data, mod_s1)

    lines1, lines2 = lines[0], lines[1]

    return [lines2, lines1] if sde == "$2" else [lines1, lines2]


def gen_e16(data: list) -> list:
    """Genera los códigos para torno suizo E16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, cyl, sde = data["Xin"], data["Cyl"], data["Sde"]
    blank_space = fspace()
    mod_s1 = 1
    mod_s3 = 1 if xin > 0 else -1

    if sde == "$3":
        lines = drilling_cuts_s3(data, mod_s3)
    elif cyl == "CICLO DE PERFORADO":
        lines = drilling_cycle_s1(data, mod_s1)
    elif cyl == "CORTES INDIVIDUALES":
        lines = drilling_cuts_s1(data, mod_s1)

    lines1, lines2 = lines[0], lines[1]

    return [lines2, lines1] if sde == "$2" else [lines1, lines2]


def gen_omni(data: list) -> list:
    """Genera los códigos para torno OmniTurn

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, cyl, sde = data["Xin"], data["Cyl"], data["Sde"]
    blank_space = fspace()
    mod_s1 = -1
    mod_s3 = 1 if xin > 0 else -1

    if sde == "$2":
        lines = [blank_space, blank_space]
    elif sde == "$3":
        lines = drilling_cuts_s3o(data, mod_s3)
    elif cyl == "CICLO DE PERFORADO":
        lines = drilling_cycle_s1o(data, mod_s1)
    elif cyl == "CORTES INDIVIDUALES":
        lines = drilling_cuts_s1o(data, mod_s1)

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def gen_romi(data: list) -> list:
    """Genera los códigos para torno Romi

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, cyl, sde = data["Xin"], data["Cyl"], data["Sde"]
    blank_space = fspace()
    mod_s1 = -1
    mod_s3 = 1 if xin > 0 else -1

    if sde == "$2":
        lines = [blank_space, blank_space]
    elif sde == "$3":
        lines = drilling_cuts_s3(data, mod_s3)
    if cyl == "CICLO DE PERFORADO":
        lines = drilling_cycle_s1r(data, mod_s1)
    elif cyl == "CORTES INDIVIDUALES":
        lines = drilling_cuts_s1(data, mod_s1)

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def gen_hardinge(data: list) -> list:
    """Genera los códigos para torno Hardinge

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    xin, cyl, sde = data["Xin"], data["Cyl"], data["Sde"]
    blank_space = fspace()
    mod_s1 = -1
    mod_s3 = 1 if xin > 0 else -1

    if sde == "$2":
        lines = [blank_space, blank_space]
    elif sde == "$3":
        lines = drilling_cuts_s3(data, mod_s3)
    elif cyl == "CICLO DE PERFORADO":
        lines = drilling_cycle_s1h(data, mod_s1)
    elif cyl == "CORTES INDIVIDUALES":
        lines = drilling_cuts_s1(data, mod_s1)

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def gen_mazak(data: list) -> list:
    """Genera los códigos para fresadora Mazak

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    cyl, sde = data["Cyl"], data["Sde"]
    blank_space = fspace()
    mod_s1 = -1

    if sde in {"$2", "$3"}:
        lines = [blank_space, blank_space]
    elif cyl == "CICLO DE PERFORADO":
        lines = drilling_cycle_s1m(data, mod_s1)
    elif cyl == "CORTES INDIVIDUALES":
        lines = drilling_cuts_s1(data, mod_s1)

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def drilling_cycle_s1(data: dict, mod: int) -> list:
    """Genera el ciclo de perforado del husillo $1 y $2

    Args:
        data (dict): Lista de datos a procesar
        mod (int): Modificador de dirección en Z

    Returns:
        list: Lista de líneas de tape
    """

    (
        dpt,
        cut,
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
        cyl,
        blk,
    ) = data.values()

    blk = "/" if blk else ""
    blank_space = fspace()

    params = dpt, cut, ang, dia
    point, final_depth, remanent = drilling_params_s1(params)

    dpt = f"Z{fnum3(final_depth)}"
    cut = f"Q{int(cut * 100000)}"
    dwl = f"P{int(dwl * 1000)}"
    fed = f"F{ffed(fed)}"

    first_depth = zin + (point + 0.02) * mod
    fct = f"Z{fnum3(first_depth)}"
    xin = f"X{fnum3(xin)}"
    zin = f"Z{fnum3(zin - (0.02 * mod))}"

    lines1 = [
        f"{blk}G00{xin}{zin}",
        f"{blk}G01{fct}{fed}",
        f"{blk}G83{dpt}{cut}{dwl}{fed}",
        f"{blk}G00{zin}",
    ]
    lines2 = [blank_space for _ in lines1]

    return [lines1, lines2]


def drilling_cycle_s1o(data: dict, mod: int) -> list:
    """Genera el ciclo de perforado del husillo $1 OmniTurn

    Args:
        data (dict): Lista de datos a procesar
        mod (int): Modificador de dirección en Z

    Returns:
        list: Lista de líneas de tape
    """

    (
        dpt,
        cut,
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
        cyl,
        blk,
    ) = data.values()

    blk = "/" if blk else ""
    blank_space = fspace()

    params = dpt, cut, ang, dia
    point, final_depth, remanent = drilling_params_s1(params)

    dpt = f"Z{fnum3(final_depth * mod)}"
    cut = f"K{fnum3(cut)}"
    fed = f"F{ffed(fed)}"

    dwl1 = f"{blk}Z-{fnum3(final_depth - 0.02)}F50." if dwl > 0 else ""
    dwl2 = f"{blk}Z-{fnum3(final_depth)}{fed}" if dwl > 0 else ""
    dwl3 = f"{blk}G04F{ffed(dwl)}" if dwl > 0 else ""

    first_depth = zin + (point + 0.02) * mod
    fct = f"Z{fnum3(first_depth)}"
    xin = f"X{fnum3(xin)}"
    zin = f"Z{fnum3(zin - (0.02 * mod))}"

    lines1 = [
        f"{blk}{xin}{zin}F300.",
        f"{blk}{fct}{fed}",
        f"{blk}G83{dpt}{cut}{fed}",
        dwl1,
        dwl2,
        dwl3,
        f"{blk}{zin}F300.",
    ]
    lines2 = [blank_space for _ in lines1]
    if not dwl:
        del lines2[-3:]

    return [lines1, lines2]


def drilling_cycle_s1r(data: dict, mod: int) -> list:
    """Genera el ciclo de perforado del husillo $1 Romi

    Args:
        data (dict): Lista de datos a procesar
        mod (int): Modificador de dirección en Z

    Returns:
        list: Lista de líneas de tape
    """

    (
        dpt,
        cut,
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
        cyl,
        blk,
    ) = data.values()

    blk = "/" if blk else ""
    blank_space = fspace()

    params = dpt, cut, ang, dia
    point, final_depth, remanent = drilling_params_s1(params)

    dpt = f"{fnum3(final_depth * mod)}"
    cut = f"Q{int(cut * 10000)}"
    fed = f"F{ffed(fed)}"
    dwl1 = f"{blk}G00Z-{fnum3(final_depth - 0.02)}" if dwl > 0 else ""
    dwl2 = f"{blk}G01Z-{fnum3(final_depth)}{fed}" if dwl > 0 else ""
    dwl3 = f"{blk}G04U{ffed(dwl)}" if dwl > 0 else ""

    first_depth = zin + (point + 0.02) * mod
    fct = f"Z{fnum3(first_depth)}"
    rfc = f"R{fnum3(first_depth)}"
    xin = f"X{fnum3(xin)}"
    zin = f"Z{fnum3(zin - (0.02 * mod))}"

    lines1 = [
        f"{blk}G00{xin}{zin}",
        f"{blk}G01{fct}{fed}",
        f"{blk}G74{rfc}",
        f"{blk}G74Z{dpt}{cut}{fed}",
        dwl1,
        dwl2,
        dwl3,
        f"{blk}G00{zin}",
    ]
    lines2 = [blank_space for _ in lines1]
    if not dwl:
        del lines2[-3:]

    return [lines1, lines2]


def drilling_cycle_s1h(data: dict, mod: int) -> list:
    """Genera el ciclo de perforado del husillo $1 Hardinge

    Args:
        data (dict): Lista de datos a procesar
        mod (int): Modificador de dirección en Z

    Returns:
        list: Lista de líneas de tape
    """

    (
        dpt,
        cut,
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
        cyl,
        blk,
    ) = data.values()

    blk = "/" if blk else ""
    blank_space = fspace()

    params = dpt, cut, ang, dia
    point, final_depth, remanent = drilling_params_s1(params)

    dpt = f"K{fnum3(final_depth * mod)}"
    cut = int(cut * 10000)
    fed = f"F{ffed(fed)}"
    dwl1 = f"{blk}G00Z-{fnum3(final_depth - 0.02)}" if dwl > 0 else ""
    dwl2 = f"{blk}G01Z-{fnum3(final_depth)}{fed}" if dwl > 0 else ""
    dwl3 = f"{blk}G04U{ffed(dwl)}" if dwl > 0 else ""

    first_depth = zin + (point + 0.02) * mod
    fct = f"Z{fnum3(first_depth)}"
    xin = f"X{fnum3(xin)}"
    zin = f"Z{fnum3(zin - (0.02 * mod))}"
    bct = "B.02"
    wct = f"W{cut}"
    cct = f"C{cut}"

    lines1 = [
        f"{blk}G00{xin}{zin}",
        f"{blk}G01{fct}{fed}",
        f"{blk}G65P9136{dpt}{bct}{wct}{cct}{fed}",
        dwl1,
        dwl2,
        dwl3,
        f"{blk}G00{zin}",
    ]
    lines2 = [blank_space for _ in lines1]
    if not dwl:
        del lines2[-3:]

    return [lines1, lines2]


def drilling_cycle_s1m(data: dict, mod: int) -> list:
    """Genera el ciclo de perforado del husillo $1 Mazak

    Args:
        data (dict): Lista de datos a procesar
        mod (int): Modificador de dirección en Z

    Returns:
        list: Lista de líneas de tape
    """

    (
        dpt,
        cut,
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
        cyl,
        blk,
    ) = data.values()

    blk = "/" if blk else ""
    blank_space = fspace()

    params = dpt, cut, ang, dia
    point, final_depth, remanent = drilling_params_s1(params)

    zin = zin - (0.02 * mod)
    dpt = (
        f"Z{fnum3(final_depth * mod)}"
        if sys == "ABSOLUTO"
        else f"Z{fnum3((final_depth + zin) * mod)}"
    )
    cut = f"Q{int(cut * 10000)}"
    fed = f"F{ffed(fed)}"
    rtr = f"R{fnum3(rtr)}"
    xin = f"X{fnum3(xin)}"
    yin = f"Y{fnum3(yin)}"
    zin = f"Z{fnum3(zin)}"

    sys = mill_g_codes[f"SISTEMA {sys}"]
    znd = mill_g_codes[znd]

    lines1 = [
        f"{blk}{sys}{znd}G83{dpt}{cut}{rtr}{fed}",
    ]
    lines2 = [blank_space for _ in lines1]

    return [lines1, lines2]


def drilling_cuts_s1(data: dict, mod: int) -> list:
    """Genera las líneas de perforado del husillo $1 y $2

    Args:
        data (dict): Lista de datos a procesar
        mod (int): Modificador de dirección en Z

    Returns:
        list: Lista de líneas de tape
    """

    (
        dpt,
        cut,
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
        cyl,
        blk,
    ) = data.values()

    blk = "/" if blk else ""
    blank_space = fspace()

    params = dpt, cut, ang, dia
    point, final_depth, remanent = drilling_params_s1(params)
    fed = f"F{ffed(fed)}"

    if float(fnum3(remanent)) == 0:
        remanent = ""

    first_depth = zin + (point + 0.02) * mod
    fct = f"Z{fnum3(first_depth)}"
    xin = f"X{fnum3(xin)}"
    zin = f"Z{fnum3(zin - (0.02 * mod))}"
    dwl = f"G04F{ffed(dwl)}" if dwl > 0 else ""

    lines1 = [f"{blk}G00{xin}{zin}", f"{blk}G01{fct}{fed}"]
    current_depth = first_depth

    while abs(current_depth) < final_depth - cut:
        current_depth = current_depth + (cut * mod)
        cdp = f"Z{fnum3(current_depth)}"
        adp = f"Z{fnum3(current_depth - (0.02 * mod))}"

        lines1.append(f"{blk}G01{cdp}")
        lines1.append(f"{blk}G00{fct}")
        lines1.append(f"{blk}{adp}")

    fdp = f"Z{fnum3(final_depth * mod)}"
    lines1.append(f"{blk}G01{fdp}") if remanent else ""
    lines1.append(dwl) if dwl else ""
    lines1.append(f"{blk}G00{zin}")

    lines2 = [blank_space for _ in lines1]

    return [lines1, lines2]


def drilling_cuts_s3(data: dict, mod: int) -> list:
    """Genera las líneas de perforado del husillo $3

    Args:
        data (dict): Lista de datos a procesar
        mod (int): Modificador de dirección en X

    Returns:
        list: Lista de líneas de tape
    """

    (
        dpt,
        cut,
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
        cyl,
        blk,
    ) = data.values()

    blk = "/" if blk else ""
    blank_space = fspace()

    params = xin, dpt, cut, ang, dia
    point, final_depth, remanent = drilling_params_s3(params)
    fed = f"F{ffed(fed)}"
    dwl = f"G04F{ffed(dwl)}" if dwl > 0 else ""

    if float(fnum3(remanent)) == 0:
        remanent = ""

    cut *= 2
    point *= 2
    first_depth = abs(xin) - (point - 0.04) * mod
    fct = f"X{fnum3(first_depth)}"
    xin = f"X{fnum3(xin + (0.04 * mod))}"
    yin = f"Y{fnum3(yin)}"
    zin = f"Z{fnum3(zin)}"

    lines1 = [f"{blk}G00{xin}{yin}{zin}", f"{blk}G01{fct}{fed}"]
    current_depth = abs(first_depth)

    while current_depth > final_depth + cut:
        current_depth = current_depth - cut
        lines1.append(f"{blk}G01X{fnum3(current_depth * mod)}")
        lines1.append(f"{blk}G00{fct}")
        lines1.append(f"{blk}X{fnum3((current_depth + 0.04) * mod)}")
    lines1.append(
        f"{blk}G01X{fnum3(final_depth * 2 * mod)}"
    ) if remanent else ""
    lines1.append(dwl) if dwl else ""
    lines1.append(f"{blk}G00{xin}")

    lines2 = [blank_space for _ in lines1]

    return [lines1, lines2]


def drilling_cuts_s1o(data: dict, mod: int) -> list:
    """Genera las líneas de perforado del husillo $1 OmniTurn

    Args:
        data (dict): Lista de datos a procesar
        mod (int): Modificador de dirección en Z

    Returns:
        list: Lista de líneas de tape
    """

    (
        dpt,
        cut,
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
        cyl,
        blk,
    ) = data.values()

    blk = "/" if blk else ""
    blank_space = fspace()

    params = dpt, cut, ang, dia
    point, final_depth, remanent = drilling_params_s1(params)
    fed = f"F{ffed(fed)}"

    if float(fnum3(remanent)) == 0:
        remanent = ""

    first_depth = zin + (point + 0.02) * mod
    fct = f"Z{fnum3(first_depth)}"
    xin = f"X{fnum3(xin)}"
    zin = f"Z{fnum3(zin - (0.02 * mod))}"
    dwl = f"G04X{ffed(dwl)}" if dwl > 0 else ""

    lines1 = [f"{blk}{xin}{zin}", f"{blk}{fct}{fed}"]
    current_depth = first_depth

    while abs(current_depth) < final_depth - cut:
        current_depth = current_depth + (cut * mod)
        lines1.append(f"{blk}Z{fnum3(current_depth)}{fed}")
        lines1.append(f"{blk}{fct}F300.")
        lines1.append(f"{blk}Z{fnum3(current_depth - (0.02 * mod))}")
    lines1.append(f"{blk}Z{fnum3(final_depth * mod)}{fed}") if remanent else ""
    lines1.append(dwl) if dwl else ""
    lines1.append(f"{blk}{zin}F300.")

    lines2 = [blank_space for _ in lines1]

    return [lines1, lines2]


def drilling_cuts_s3o(data: dict, mod: int) -> list:
    """Genera las líneas de perforado del husillo $3 OmniTurn

    Args:
        data (dict): Lista de datos a procesar
        mod (int): Modificador de dirección en X

    Returns:
        list: Lista de líneas de tape
    """

    (
        dpt,
        cut,
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
        cyl,
        blk,
    ) = data.values()

    blk = "/" if blk else ""
    blank_space = fspace()

    params = xin, dpt, cut, ang, dia
    point, final_depth, remanent = drilling_params_s3o(params)
    fed = f"F{ffed(fed)}"

    if float(fnum3(remanent)) == 0:
        remanent = ""

    first_depth = abs(xin) - (point - 0.02) * mod
    fct = f"X{fnum3(first_depth)}"
    xin = f"X{fnum3(xin + (0.02 * mod))}"
    zin = f"Z{fnum3(zin)}"
    dwl = f"G04F{ffed(dwl)}" if dwl > 0 else ""

    lines1 = [f"{blk}G00{xin}{zin}", f"{blk}G01{fct}{fed}"]
    current_depth = abs(first_depth)

    while current_depth > final_depth + cut:
        current_depth = current_depth - cut
        lines1.append(f"{blk}X{fnum3(current_depth * mod)}{fed}")
        lines1.append(f"{blk}{fct}F300.")
        lines1.append(f"{blk}X{fnum3((current_depth + 0.02) * mod)}")
    lines1.append(f"{blk}X{fnum3(final_depth * mod)}{fed}") if remanent else ""
    lines1.append(dwl) if dwl else ""
    lines1.append(f"{blk}{xin}F300.")

    lines2 = [blank_space for _ in lines1]

    return [lines1, lines2]


def drilling_params_s1(params: list) -> list:
    """Calcula dimensiones para perforado

    Args:
        params (list): Lista de parámetros

    Returns:
        list: Lista de dimensiones calculadas
    """

    dpt, cut, ang, dia = params

    angle = math.radians(ang / 2)
    point = (dia / 2) / math.tan(angle)
    final_depth = dpt + point
    cut_depth = final_depth - point - 0.02
    cuts = round(cut_depth / cut)
    remanent = cut_depth - (cut * cuts)

    return point, final_depth, remanent


def drilling_params_s3(params: list) -> list:
    """Calcula dimensiones para perforado

    Args:
        params (list): Lista de parámetros

    Returns:
        list: Lista de dimensiones calculadas
    """

    xin, dpt, cut, ang, dia = params

    cut *= 2
    angle = math.radians(ang / 2)
    point = (dia / 2) / math.tan(angle)
    final_depth = dpt - point
    cut_depth = ((abs(xin) - final_depth) / 2) - point - 0.02
    cuts = round(cut_depth / cut)
    remanent = cut_depth - (cut * cuts)

    return point, final_depth, remanent


def drilling_params_s3o(params: list) -> list:
    """Calcula dimensiones para perforado

    Args:
        params (list): Lista de parámetros

    Returns:
        list: Lista de dimensiones calculadas
    """

    xin, dpt, cut, ang, dia = params

    angle = math.radians(ang / 2)
    point = (dia / 2) / math.tan(angle)
    final_depth = dpt - point
    cut_depth = ((abs(xin) - final_depth) / 2) - point - 0.02
    cuts = round(cut_depth / cut)
    remanent = cut_depth - (cut * cuts)

    return point, final_depth, remanent
