from tools.cnc_codes import *
from tools.formatting import *

import math


def flat_mill_gen(machine, data) -> list:
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

    dyr, pos = data["Dyr"], data["Pos"]
    tmd = 2 if pos == "POSITIVA" else -2
    lmd = 1
    tdn = "Y"
    ldn = "Z"

    if dyr == "ALTERNADOS":
        lines = flat_mill_alt(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA ADENTRO":
        lines = flat_mill_inn(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA AFUERA":
        lines = flat_mill_out(data, tmd, lmd, tdn, ldn)

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def gen_k16(data: list) -> list:
    """Genera los códigos para torno suizo K16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dyr, pos = data["Dyr"], data["Pos"]
    tmd = 2 if pos == "POSITIVA" else -2
    lmd = 1
    tdn = "Y"
    ldn = "Z"

    if dyr == "ALTERNADOS":
        lines = flat_mill_alt(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA ADENTRO":
        lines = flat_mill_inn(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA AFUERA":
        lines = flat_mill_out(data, tmd, lmd, tdn, ldn)

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def gen_e16(data: list) -> list:
    """Genera los códigos para torno suizo E16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dyr, pos = data["Dyr"], data["Pos"]
    tmd = 2 if pos == "POSITIVA" else -2
    lmd = 1
    tdn = "Y"
    ldn = "Z"

    if dyr == "ALTERNADOS":
        lines = flat_mill_alt(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA ADENTRO":
        lines = flat_mill_inn(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA AFUERA":
        lines = flat_mill_out(data, tmd, lmd, tdn, ldn)

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def gen_omni(data: list) -> list:
    """Genera los códigos para torno OmniTurn

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dyr, pos = data["Dyr"], data["Pos"]
    tmd = 1 if pos == "POSITIVA" else -1
    lmd = -1
    tdn = "X"
    ldn = "Z"

    if dyr == "ALTERNADOS":
        lines = flat_mill_alto(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA ADENTRO":
        lines = flat_mill_inno(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA AFUERA":
        lines = flat_mill_outo(data, tmd, lmd, tdn, ldn)

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def gen_romi(data: list) -> list:
    """Genera los códigos para torno Romi

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dyr, pos = data["Dyr"], data["Pos"]
    tmd = 2 if pos == "POSITIVA" else -2
    lmd = -1
    tdn = "X"
    ldn = "Z"

    if dyr == "ALTERNADOS":
        lines = flat_mill_alt(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA ADENTRO":
        lines = flat_mill_inn(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA AFUERA":
        lines = flat_mill_out(data, tmd, lmd, tdn, ldn)

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def gen_hardinge(data: list) -> list:
    """Genera los códigos para torno Hardinge

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dyr, pos = data["Dyr"], data["Pos"]
    tmd = 2 if pos == "POSITIVA" else -2
    lmd = -1
    tdn = "X"
    ldn = "Z"

    if dyr == "ALTERNADOS":
        lines = flat_mill_alt(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA ADENTRO":
        lines = flat_mill_inn(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA AFUERA":
        lines = flat_mill_out(data, tmd, lmd, tdn, ldn)

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def gen_mazak(data: list) -> list:
    """Genera los códigos para fresadora Mazak

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    dyr, pos = data["Dyr"], data["Pos"]
    tmd = 1 if pos == "POSITIVA" else -1
    lmd = 1
    tdn = "Y"
    ldn = "X"

    if dyr == "ALTERNADOS":
        lines = flat_mill_altm(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA ADENTRO":
        lines = flat_mill_innm(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA AFUERA":
        lines = flat_mill_outm(data, tmd, lmd, tdn, ldn)

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def flat_mill_alt(data: list, tmd: int, lmd: int, tdn: str, ldn: str) -> list:
    """Genera las líneas de fresado de paleta con corte alternado

    Args:
        data (list): Lista de datos a procesar
        tmd (int): Modificador de movimiento transversal
        lmd (int): Modificador de movimiento longitudinal
        tdn (str): Denominación del eje transversal
        ldn (str): Denominación del eje longitudinal

    Returns:
        list: Lista de líneas de tape
    """

    wdt, lgt, mat, fed, cut, dyr, pos, tcm, lcm, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    cuts = math.ceil((mat - wdt) / 2 / cut)
    cuts = cuts if cuts % 2 == 0 else cuts + 1

    params = tmd, lmd, wdt, lgt, fed, cut, tcm, lcm, dia, cuts
    tin, lsc, lin, lnd = flat_milling_params(params)

    tin = tin - (cut * tmd)
    lines1 = [
        f"{blk}G00{tdn}{fnum3(tin)}{ldn}{fnum3(lsc)}",
        f"{blk}G01{ldn}{fnum3(lin)}F{ffed(fed)}",
    ]
    cyls = int(cuts / 2)

    for cyl in range(cyls):
        tcr = "" if cyl == 0 else f"{blk}{tdn}{fnum3(tin)}"
        cfd = fed * 0.5 if cyl + 1 == cyls else fed
        lines1.append(tcr)
        lcr = f"{blk}{ldn}{fnum3(lnd)}"
        lines1.append(lcr)
        tin = tin - (cut * tmd)

        tcr = f"{blk}{tdn}{fnum3(tin)}F{ffed(fed * 0.1)}"
        lines1.append(tcr)
        lcr = f"{blk}{ldn}{fnum3(lin)}F{ffed(cfd)}"
        lines1.append(lcr)
        tin = tin - (cut * tmd)

    lines2 = [iu_space for _ in lines1]
    del lines2[-1]

    return [lines1, lines2]


def flat_mill_inn(data: list, tmd: int, lmd: int, tdn: str, ldn: str) -> list:
    """Genera las líneas de fresado de paleta con corte hacia adentro

    Args:
        data (list): Lista de datos a procesar
        tmd (int): Modificador de movimiento transversal
        lmd (int): Modificador de movimiento longitudinal
        tdn (str): Denominación del eje transversal
        ldn (str): Denominación del eje longitudinal

    Returns:
        list: Lista de líneas de tape
    """

    wdt, lgt, mat, fed, cut, dyr, pos, tcm, lcm, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    cuts = math.ceil((mat - wdt) / 2 / cut)

    params = tmd, lmd, wdt, lgt, fed, cut, tcm, lcm, dia, cuts
    tin, lsc, lin, lnd = flat_milling_params(params)

    tin = tin - (cut * tmd)
    lines1 = [
        f"{blk}G00{tdn}{fnum3(tin)}{ldn}{fnum3(lsc)}",
        f"{blk}G01{ldn}{fnum3(lin)}F{ffed(fed)}",
    ]
    cyls = cuts

    for cyl in range(cyls):
        tcr = "" if cyl == 0 else f"{blk}G01{tdn}{fnum3(tin)}"
        cfd = f"F{ffed(fed * 0.5)}" if cyl + 1 == cyls else ""
        lines1.append(tcr)
        lcr = f"{blk}{ldn}{fnum3(lnd)}{cfd}"
        lines1.append(lcr)
        tsc = f"{blk}{tdn}{fnum3(tin + (cut * tmd))}"
        lines1.append(tsc)
        lcr = f"{blk}G00{ldn}{fnum3(lin)}"
        lines1.append(lcr)
        tin = tin - (cut * tmd)

    lines2 = [iu_space for _ in lines1]
    del lines2[-1]

    return [lines1, lines2]


def flat_mill_out(data: list, tmd: int, lmd: int, tdn: str, ldn: str) -> list:
    """Genera las líneas de fresado de paleta con corte hacia afuera

    Args:
        data (list): Lista de datos a procesar
        tmd (int): Modificador de movimiento transversal
        lmd (int): Modificador de movimiento longitudinal
        tdn (str): Denominación del eje transversal
        ldn (str): Denominación del eje longitudinal

    Returns:
        list: Lista de líneas de tape
    """

    wdt, lgt, mat, fed, cut, dyr, pos, tcm, lcm, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    cuts = math.ceil((mat - wdt) / 2 / cut)

    params = tmd, lmd, wdt, lgt, fed, cut, tcm, lcm, dia, cuts
    tin, lsc, lin, lnd = flat_milling_params(params)

    tin = tin - (cut * tmd)
    lines1 = [
        f"{blk}G00{tdn}{fnum3(tin)}{ldn}{fnum3(lsc)}",
        f"{blk}G01{ldn}{fnum3(lin)}F{ffed(fed)}",
    ]
    cyls = cuts

    for cyl in range(cyls):
        tsc = f"{blk}G00{tdn}{fnum3(tin + (cut * 2 * tmd))}"
        cfd = fed * 0.5 if cyl + 1 == cyls else fed
        lines1.append(tsc)
        lcr = f"{blk}{ldn}{fnum3(lnd)}"
        lines1.append(lcr)
        tcr = f"{blk}G01{tdn}{fnum3(tin)}F{ffed(fed * 0.1)}"
        lines1.append(tcr)
        lcr = f"{blk}{ldn}{fnum3(lin)}F{ffed(cfd)}"
        lines1.append(lcr)
        tin = tin - (cut * tmd)

    lines2 = [iu_space for _ in lines1]
    del lines2[-1]

    return [lines1, lines2]


def flat_mill_alto(data: list, tmd: int, lmd: int, tdn: str, ldn: str) -> list:
    """Genera las líneas de fresado de paleta con corte alternado para omni

    Args:
        data (list): Lista de datos a procesar
        tmd (int): Modificador de movimiento transversal
        lmd (int): Modificador de movimiento longitudinal
        tdn (str): Denominación del eje transversal
        ldn (str): Denominación del eje longitudinal

    Returns:
        list: Lista de líneas de tape
    """

    wdt, lgt, mat, fed, cut, dyr, pos, tcm, lcm, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    cuts = math.ceil((mat - wdt) / 2 / cut)
    cuts = cuts if cuts % 2 == 0 else cuts + 1

    params = tmd, lmd, wdt, lgt, fed, cut, tcm, lcm, dia, cuts
    tin, lsc, lin, lnd = flat_milling_params(params)

    tin = tin - (cut * tmd)
    lines1 = [
        f"{blk}{tdn}{fnum3(tin)}{ldn}{fnum3(lsc)}F300.",
        f"{blk}{ldn}{fnum3(lin)}F{ffed(fed)}",
    ]
    cyls = int(cuts / 2)

    for cyl in range(cyls):
        tcr = "" if cyl == 0 else f"{blk}{tdn}{fnum3(tin)}"
        cfd = fed * 0.5 if cyl + 1 == cyls else fed
        lines1.append(tcr)
        lcr = f"{blk}{ldn}{fnum3(lnd)}"
        lines1.append(lcr)
        tin = tin - (cut * tmd)

        tcr = f"{blk}{tdn}{fnum3(tin)}F{ffed(fed * 0.1)}"
        lines1.append(tcr)
        lcr = f"{blk}{ldn}{fnum3(lin)}F{ffed(cfd)}"
        lines1.append(lcr)
        tin = tin - (cut * tmd)

    lines2 = [iu_space for _ in lines1]
    del lines2[-1]

    return [lines1, lines2]


def flat_mill_inno(data: list, tmd: int, lmd: int, tdn: str, ldn: str) -> list:
    """Genera las líneas de fresado de paleta con corte hacia adentro para omni

    Args:
        data (list): Lista de datos a procesar
        tmd (int): Modificador de movimiento transversal
        lmd (int): Modificador de movimiento longitudinal
        tdn (str): Denominación del eje transversal
        ldn (str): Denominación del eje longitudinal

    Returns:
        list: Lista de líneas de tape
    """

    wdt, lgt, mat, fed, cut, dyr, pos, tcm, lcm, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    cuts = math.ceil((mat - wdt) / 2 / cut)

    params = tmd, lmd, wdt, lgt, fed, cut, tcm, lcm, dia, cuts
    tin, lsc, lin, lnd = flat_milling_params(params)

    tin = tin - (cut * tmd)
    lines1 = [
        f"{blk}{tdn}{fnum3(tin)}{ldn}{fnum3(lsc)}F300.",
        f"{blk}{ldn}{fnum3(lin)}F{ffed(fed)}",
    ]
    cyls = cuts

    for cyl in range(cyls):
        tcr = "" if cyl == 0 else f"{blk}{tdn}{fnum3(tin)}F{ffed(fed)}"
        lines1.append(tcr)
        lcr = f"{blk}{ldn}{fnum3(lnd)}"
        lines1.append(lcr)
        tsc = f"{blk}{tdn}{fnum3(tin + (cut * tmd))}"
        lines1.append(tsc)
        lcr = f"{blk}{ldn}{fnum3(lin)}F300."
        lines1.append(lcr)
        tin = tin - (cut * tmd)

    lines2 = [iu_space for _ in lines1]
    del lines2[-1]

    return [lines1, lines2]


def flat_mill_outo(data: list, tmd: int, lmd: int, tdn: str, ldn: str) -> list:
    """Genera las líneas de fresado de paleta con corte hacia afuera para omni

    Args:
        data (list): Lista de datos a procesar
        tmd (int): Modificador de movimiento transversal
        lmd (int): Modificador de movimiento longitudinal
        tdn (str): Denominación del eje transversal
        ldn (str): Denominación del eje longitudinal

    Returns:
        list: Lista de líneas de tape
    """

    wdt, lgt, mat, fed, cut, dyr, pos, tcm, lcm, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    cuts = math.ceil((mat - wdt) / 2 / cut)

    params = tmd, lmd, wdt, lgt, fed, cut, tcm, lcm, dia, cuts
    tin, lsc, lin, lnd = flat_milling_params(params)

    tin = tin - (cut * tmd)
    lines1 = [
        f"{blk}{tdn}{fnum3(tin)}{ldn}{fnum3(lsc)}F300.",
        f"{blk}{ldn}{fnum3(lin)}F{ffed(fed)}",
    ]
    cyls = cuts

    for cyl in range(cyls):
        tsc = f"{blk}{tdn}{fnum3(tin + (cut * 2 * tmd))}F300."
        cfd = fed * 0.5 if cyl + 1 == cyls else fed
        lines1.append(tsc)
        lcr = f"{blk}{ldn}{fnum3(lnd)}"
        lines1.append(lcr)
        tcr = f"{blk}{tdn}{fnum3(tin)}F{ffed(fed * 0.1)}"
        lines1.append(tcr)
        lcr = f"{blk}{ldn}{fnum3(lin)}F{ffed(cfd)}"
        lines1.append(lcr)
        tin = tin - (cut * tmd)

    lines2 = [iu_space for _ in lines1]
    del lines2[-1]

    return [lines1, lines2]


def flat_mill_altm(data: list, tmd: int, lmd: int, tdn: str, ldn: str) -> list:
    """Genera las líneas de fresado de paleta con corte alternado para mazak

    Args:
        data (list): Lista de datos a procesar
        tmd (int): Modificador de movimiento transversal
        lmd (int): Modificador de movimiento longitudinal
        tdn (str): Denominación del eje transversal
        ldn (str): Denominación del eje longitudinal

    Returns:
        list: Lista de líneas de tape
    """

    wdt, lgt, mat, fed, cut, dyr, pos, tcm, lcm, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    cuts = math.ceil((mat - wdt) / 2 / cut)
    cuts = cuts if cuts % 2 == 0 else cuts + 1

    params = tmd, lmd, wdt, lgt, fed, cut, tcm, lcm, dia, cuts
    tin, lsc, lin, lnd = flat_milling_params(params)

    tin = tin - (cut * tmd)
    lin -= lgt * lmd
    lnd = lin * -1

    lines1 = [
        f"{blk}G00{ldn}{fnum3(lsc)}{tdn}{fnum3(tin)}",
        f"{blk}G91G01{ldn}.025F{ffed(fed)}",
    ]
    cyls = int(cuts / 2)

    for cyl in range(cyls):
        tcr = "" if cyl == 0 else f"{blk}{tdn}{fnum3(tin)}"
        cfd = fed * 0.5 if cyl + 1 == cyls else fed
        tin = cut * tmd * -1
        lines1.append(tcr)
        lcr = f"{blk}{ldn}{fnum3(lnd)}"
        lines1.append(lcr)
        tcr = f"{blk}{tdn}{fnum3(tin)}F{ffed(fed * 0.1)}"
        lines1.append(tcr)
        lcr = f"{blk}{ldn}{fnum3(lin)}F{ffed(cfd)}"
        lines1.append(lcr)

    lines2 = [iu_space for _ in lines1]
    del lines2[-1]

    return [lines1, lines2]


def flat_mill_innm(data: list, tmd: int, lmd: int, tdn: str, ldn: str) -> list:
    """Genera las líneas de fresado de paleta con corte hacia adentro mazak

    Args:
        data (list): Lista de datos a procesar
        tmd (int): Modificador de movimiento transversal
        lmd (int): Modificador de movimiento longitudinal
        tdn (str): Denominación del eje transversal
        ldn (str): Denominación del eje longitudinal

    Returns:
        list: Lista de líneas de tape
    """

    wdt, lgt, mat, fed, cut, dyr, pos, tcm, lcm, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    cuts = math.ceil((mat - wdt) / 2 / cut)

    params = tmd, lmd, wdt, lgt, fed, cut, tcm, lcm, dia, cuts
    tin, lsc, lin, lnd = flat_milling_params(params)

    tin = tin - (cut * tmd)
    lin -= lgt * lmd
    lnd = lin * -1

    lines1 = [
        f"{blk}G90G00{ldn}{fnum3(lsc)}{tdn}{fnum3(tin)}",
        f"{blk}G91G01{ldn}.025F{ffed(fed)}",
    ]
    cyls = cuts

    for cyl in range(cyls):
        tcr = "" if cyl == 0 else f"{blk}G01{tdn}{fnum3(cut * -3 * tmd)}"
        cfd = f"F{ffed(fed * 0.5)}" if cyl + 1 == cyls else ""
        lines1.append(tcr)
        lcr = f"{blk}{ldn}{fnum3(lnd)}{cfd}"
        lines1.append(lcr)
        tsc = f"{blk}{tdn}{fnum3(cut * 2 * tmd)}"
        lines1.append(tsc)
        lcr = f"{blk}G00{ldn}{fnum3(lin)}"
        lines1.append(lcr)

    lines2 = [iu_space for _ in lines1]
    del lines2[-1]

    return [lines1, lines2]


def flat_mill_outm(data: list, tmd: int, lmd: int, tdn: str, ldn: str) -> list:
    """Genera las líneas de fresado de paleta con corte hacia afuera para mazak

    Args:
        data (list): Lista de datos a procesar
        tmd (int): Modificador de movimiento transversal
        lmd (int): Modificador de movimiento longitudinal
        tdn (str): Denominación del eje transversal
        ldn (str): Denominación del eje longitudinal

    Returns:
        list: Lista de líneas de tape
    """

    wdt, lgt, mat, fed, cut, dyr, pos, tcm, lcm, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    cuts = math.ceil((mat - wdt) / 2 / cut)

    params = tmd, lmd, wdt, lgt, fed, cut, tcm, lcm, dia, cuts
    tin, lsc, lin, lnd = flat_milling_params(params)

    fct = cut * tmd
    tin = tin - (cut * tmd)
    lin -= lgt * lmd
    lnd = lin * -1

    lines1 = [
        f"{blk}G90G00{ldn}{fnum3(lsc)}{tdn}{fnum3(tin)}",
        f"{blk}G91G01{ldn}.025{tdn}{fnum3(fct)}F{ffed(fed)}",
    ]
    cyls = cuts

    for cyl in range(cyls):
        tsc = f"{blk}G00{tdn}{fnum3(cut * 2 * tmd)}"
        cfd = fed * 0.5 if cyl + 1 == cyls else fed
        lines1.append(tsc)
        lcr = f"{blk}{ldn}{fnum3(lnd)}"
        lines1.append(lcr)
        ctr = cut * -3 * tmd
        tcr = f"{blk}G01{tdn}{fnum3(fnum3(ctr))}F{ffed(fed * 0.1)}"
        lines1.append(tcr)
        lcr = f"{blk}{ldn}{fnum3(lin)}F{ffed(cfd)}"
        lines1.append(lcr)

    lines2 = [iu_space for _ in lines1]
    del lines2[-1]

    return [lines1, lines2]


def flat_milling_params(params: list) -> list:
    """Calcula dimensiones para fresado de cara plana

    Args:
        params (list): Lista de datos a procesar

    Returns:
        list: Lista de dimensiones calculadas
    """

    tmd, lmd, wdt, lgt, fed, cut, tcm, lcm, dia, cuts = params
    tin = ((wdt / 2) + (dia / 2) + (cut * cuts) + tcm) * tmd
    lsc = (((dia / 2) + 0.025) * lmd * -1) + lcm
    lin = ((dia / 2) * lmd * -1) + lcm
    lnd = (lgt * lmd) + lcm

    return tin, lsc, lin, lnd
