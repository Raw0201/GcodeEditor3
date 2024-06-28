from tools.cnc_codes import *
from tools.formatting import *

import math


def face_mill_gen(machine, data) -> list:
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
        lines = face_mill_alt(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA ADENTRO":
        lines = face_mill_inn(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA AFUERA":
        lines = face_mill_out(data, tmd, lmd, tdn, ldn)

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
        lines = face_mill_alt(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA ADENTRO":
        lines = face_mill_inn(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA AFUERA":
        lines = face_mill_out(data, tmd, lmd, tdn, ldn)

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
        lines = face_mill_alt(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA ADENTRO":
        lines = face_mill_inn(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA AFUERA":
        lines = face_mill_out(data, tmd, lmd, tdn, ldn)

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
        lines = face_mill_alto(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA ADENTRO":
        lines = face_mill_inno(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA AFUERA":
        lines = face_mill_outo(data, tmd, lmd, tdn, ldn)

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
        lines = face_mill_alt(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA ADENTRO":
        lines = face_mill_inn(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA AFUERA":
        lines = face_mill_out(data, tmd, lmd, tdn, ldn)

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
        lines = face_mill_alt(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA ADENTRO":
        lines = face_mill_inn(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA AFUERA":
        lines = face_mill_out(data, tmd, lmd, tdn, ldn)

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
        lines = face_mill_altm(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA ADENTRO":
        lines = face_mill_innm(data, tmd, lmd, tdn, ldn)
    elif dyr == "HACIA AFUERA":
        lines = face_mill_outm(data, tmd, lmd, tdn, ldn)

    lines1, lines2 = lines[0], lines[1]

    return [lines1, lines2]


def face_mill_alt(data: list, tmd: int, lmd: int, tdn: str, ldn: str) -> list:
    """Genera las líneas de fresado de cara con corte alternado

    Args:
        data (list): Lista de datos a procesar
        tmd (int): Modificador de movimiento transversal
        lmd (int): Modificador de movimiento longitudinal
        tdn (str): Denominación del eje transversal
        ldn (str): Denominación del eje longitudinal

    Returns:
        list: Lista de líneas de tape
    """
    
    wdt, lgt, ang, mat, fed, cut, dyr, pos, tcm, lcm, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    ang = math.radians(ang)
    cuts = math.ceil((((mat - wdt) / 2) * math.cos(ang)) / cut)
    cuts = cuts if cuts % 2 == 0 else cuts + 1

    params = lgt, tmd, lmd, wdt, ang, dia, cuts, cut
    tin, tnd, tds, lsc, lin, lnd, lds = face_milling_params(params)

    tst = tin - (tds)
    lines1 = [
        f"{blk}G00{tdn}{fnum3(tst * tmd + tcm)}{ldn}{fnum3(lsc + lcm)}",
        f"{blk}G01{ldn}{fnum3(lin + lcm)}F{ffed(fed)}",
    ]

    cyls = int(cuts / 2)
    lnd -= (lds * cuts)
    lnd *= lmd

    for cyl in range(cyls):
        tin -= tds
        tcr = "" if cyl == 0 else f"{blk}{tdn}{fnum3(tin * tmd + tcm)}"
        cfd = f"F{ffed(fed * 0.5)}" if cyl + 1 == cyls else ""
        lines1.append(tcr)
        lnd += lds * lmd
        crl = f"{blk}{tdn}{fnum3(tnd * tmd + tcm)}{ldn}{fnum3(lnd + lcm)}"
        lines1.append(crl)
        lnd += lds * lmd
        crl = f"{blk}{ldn}{fnum3(lnd + lcm)}"
        lines1.append(crl)
        tin -= tds
        crl = f"{blk}{tdn}{fnum3(tin * tmd + tcm)}{ldn}{fnum3(lin + lcm)}{cfd}"
        lines1.append(crl)

    lines2 = [iu_space for _ in lines1]
    del lines2[-1]

    return [lines1, lines2]


def face_mill_inn(data: list, tmd: int, lmd: int, tdn: str, ldn: str) -> list:
    """Genera las líneas de fresado de cara con corte hacia adentro

    Args:
        data (list): Lista de datos a procesar
        tmd (int): Modificador de movimiento transversal
        lmd (int): Modificador de movimiento longitudinal
        tdn (str): Denominación del eje transversal
        ldn (str): Denominación del eje longitudinal

    Returns:
        list: Lista de líneas de tape
    """

    wdt, lgt, ang, mat, fed, cut, dyr, pos, tcm, lcm, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    ang = math.radians(ang)
    cuts = math.ceil((((mat - wdt) / 2) * math.cos(ang)) / cut)
    cuts = cuts if cuts % 2 == 0 else cuts + 1

    params = lgt, tmd, lmd, wdt, ang, dia, cuts, cut
    tin, tnd, tds, lsc, lin, lnd, lds = face_milling_params(params)

    tst = tin - (tds)
    lines1 = [
        f"{blk}G00{tdn}{fnum3(tst * tmd + tcm)}{ldn}{fnum3(lsc + lcm)}",
        f"{blk}G01{ldn}{fnum3(lin + lcm)}F{ffed(fed)}",
    ]

    cyls = cuts
    lnd -= (lds * cuts)
    lnd *= lmd

    for cyl in range(cyls):
        tin -= tds
        tcr = "" if cyl == 0 else f"{blk}G01{tdn}{fnum3(tin * tmd + tcm)}"
        cfd = f"F{ffed(fed * 0.5)}" if cyl + 1 == cyls else ""
        lines1.append(tcr)
        lnd += lds * lmd
        crl = f"{blk}{tdn}{fnum3(tnd * tmd + tcm)}{ldn}{fnum3(lnd + lcm)}{cfd}"
        lines1.append(crl)
        crl = f"{blk}G00{ldn}{fnum3(lin + lcm)}"
        lines1.append(crl)
        crl = f"{blk}{tdn}{fnum3(tin * tmd + tcm)}"
        lines1.append(crl) if cyl != cuts - 1 else ""

    lines2 = [iu_space for _ in lines1]
    del lines2[-1]

    return [lines1, lines2]


def face_mill_out(data: list, tmd: int, lmd: int, tdn: str, ldn: str) -> list:
    """Genera las líneas de fresado de cara con corte hacia afuera

    Args:
        data (list): Lista de datos a procesar
        tmd (int): Modificador de movimiento transversal
        lmd (int): Modificador de movimiento longitudinal
        tdn (str): Denominación del eje transversal
        ldn (str): Denominación del eje longitudinal

    Returns:
        list: Lista de líneas de tape
    """

    wdt, lgt, ang, mat, fed, cut, dyr, pos, tcm, lcm, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    ang = math.radians(ang)
    cuts = math.ceil((((mat - wdt) / 2) * math.cos(ang)) / cut)
    cuts = cuts if cuts % 2 == 0 else cuts + 1

    params = lgt, tmd, lmd, wdt, ang, dia, cuts, cut
    tin, tnd, tds, lsc, lin, lnd, lds = face_milling_params(params)

    cyls = cuts
    lnd -= (lds * cuts)
    lnd *= lmd
    lnd += lds * lmd

    lines1 = [
        f"{blk}G00{tdn}{fnum3(tnd * tmd + tcm)}{ldn}{fnum3(lsc + lcm)}",
        f"{blk}G01{ldn}{fnum3(lnd + lcm)}F{ffed(fed)}",
    ]

    for cyl in range(cyls):
        tin -= tds
        tcr = "" if cyl == 0 else f"{blk}G01{ldn}{fnum3(lnd + lcm)}"
        cfd = f"F{ffed(fed * 0.5)}" if cyl + 1 == cyls else ""
        lines1.append(tcr)
        crl = f"{blk}{tdn}{fnum3(tin * tmd + tcm)}{ldn}{fnum3(lin + lcm)}{cfd}"
        lines1.append(crl)
        crl = f"{blk}G00{tdn}{fnum3(tnd * tmd + tcm)}"
        lines1.append(crl) if cyl != cuts - 1 else ""
        crl = f"{blk}{ldn}{fnum3(lnd + lcm)}"
        lines1.append(crl) if cyl != cuts - 1 else ""
        lnd += lds * lmd

    lines2 = [iu_space for _ in lines1]
    del lines2[-1]

    return [lines1, lines2]


def face_mill_alto(data: list, tmd: int, lmd: int, tdn: str, ldn: str) -> list:
    """Genera las líneas de fresado de cara con corte alternado para omni

    Args:
        data (list): Lista de datos a procesar
        tmd (int): Modificador de movimiento transversal
        lmd (int): Modificador de movimiento longitudinal
        tdn (str): Denominación del eje transversal
        ldn (str): Denominación del eje longitudinal

    Returns:
        list: Lista de líneas de tape
    """

    wdt, lgt, ang, mat, fed, cut, dyr, pos, tcm, lcm, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    ang = math.radians(ang)
    cuts = math.ceil((((mat - wdt) / 2) * math.cos(ang)) / cut)
    cuts = cuts if cuts % 2 == 0 else cuts + 1

    params = lgt, tmd, lmd, wdt, ang, dia, cuts, cut
    tin, tnd, tds, lsc, lin, lnd, lds = face_milling_params(params)

    tst = tin - (tds)
    lines1 = [
        f"{blk}{tdn}{fnum3(tst * tmd + tcm)}{ldn}{fnum3(lsc + lcm)}",
        f"{blk}{ldn}{fnum3(lin + lcm)}F{ffed(fed)}",
    ]

    cyls = int(cuts / 2)
    lnd -= (lds * cuts)
    lnd *= lmd

    for cyl in range(cyls):
        tin -= tds
        tcr = "" if cyl == 0 else f"{blk}{tdn}{fnum3(tin * tmd + tcm)}"
        cfd = f"F{ffed(fed * 0.5)}" if cyl + 1 == cyls else ""
        lines1.append(tcr)
        lnd += lds * lmd
        crl = f"{blk}{tdn}{fnum3(tnd * tmd + tcm)}{ldn}{fnum3(lnd + lcm)}"
        lines1.append(crl)
        lnd += lds * lmd
        crl = f"{blk}{ldn}{fnum3(lnd + lcm)}"
        lines1.append(crl)
        tin -= tds
        crl = f"{blk}{tdn}{fnum3(tin * tmd + tcm)}{ldn}{fnum3(lin + lcm)}{cfd}"
        lines1.append(crl)

    lines2 = [iu_space for _ in lines1]
    del lines2[-1]

    return [lines1, lines2]


def face_mill_inno(data: list, tmd: int, lmd: int, tdn: str, ldn: str) -> list:
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

    wdt, lgt, ang, mat, fed, cut, dyr, pos, tcm, lcm, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    ang = math.radians(ang)
    cuts = math.ceil((((mat - wdt) / 2) * math.cos(ang)) / cut)
    cuts = cuts if cuts % 2 == 0 else cuts + 1

    params = lgt, tmd, lmd, wdt, ang, dia, cuts, cut
    tin, tnd, tds, lsc, lin, lnd, lds = face_milling_params(params)

    tst = tin - (tds * tmd)
    lines1 = [
        f"{blk}{tdn}{fnum3(tst * tmd + tcm)}{ldn}{fnum3(lsc + lcm)}",
        f"{blk}{ldn}{fnum3(lin + lcm)}F{ffed(fed)}",
    ]

    cyls = cuts
    lnd -= (lds * cuts)
    lnd *= lmd

    for cyl in range(cyls):
        tin -= tds * tmd
        tcr = "" if cyl == 0 else f"{blk}{tdn}{fnum3(tin * tmd + tcm)}F{ffed(fed)}"
        cfd = f"F{ffed(fed * 0.5)}" if cyl + 1 == cyls else ""
        lines1.append(tcr)
        lnd += lds * lmd
        crl = f"{blk}{tdn}{fnum3(tnd * tmd + tcm)}{ldn}{fnum3(lnd + lcm)}{cfd}"
        lines1.append(crl)
        crl = f"{blk}{ldn}{fnum3(lin + lcm)}F300"
        lines1.append(crl)
        crl = f"{blk}{tdn}{fnum3(tin * tmd + tcm)}"
        lines1.append(crl) if cyl != cuts - 1 else ""

    lines2 = [iu_space for _ in lines1]
    del lines2[-1]

    return [lines1, lines2]


def face_mill_outo(data: list, tmd: int, lmd: int, tdn: str, ldn: str) -> list:
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

    wdt, lgt, ang, mat, fed, cut, dyr, pos, tcm, lcm, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    ang = math.radians(ang)
    cuts = math.ceil((((mat - wdt) / 2) * math.cos(ang)) / cut)
    cuts = cuts if cuts % 2 == 0 else cuts + 1

    params = lgt, tmd, lmd, wdt, ang, dia, cuts, cut
    tin, tnd, tds, lsc, lin, lnd, lds = face_milling_params(params)

    cyls = cuts
    lnd -= (lds * cuts)
    lnd *= lmd
    lnd += lds * lmd

    lines1 = [
        f"{blk}{tdn}{fnum3(tnd * tmd)}{ldn}{fnum3(lsc)}",
        f"{blk}{ldn}{fnum3(lnd + lcm)}F{ffed(fed)}",
    ]

    for cyl in range(cyls):
        tin -= tds * tmd
        tcr = "" if cyl == 0 else f"{blk}{ldn}{fnum3(lnd + lcm)}F{ffed(fed)}"
        cfd = f"F{ffed(fed * 0.5)}" if cyl + 1 == cyls else ""
        lines1.append(tcr)
        crl = f"{blk}{tdn}{fnum3(tin * tmd + tcm)}{ldn}{fnum3(lin + lcm)}{cfd}"
        lines1.append(crl)
        crl = f"{blk}{tdn}{fnum3(tnd * tmd + tcm)}F300"
        lines1.append(crl) if cyl != cuts - 1 else ""
        crl = f"{blk}{ldn}{fnum3(lnd + lcm)}"
        lines1.append(crl) if cyl != cuts - 1 else ""
        lnd += lds * lmd

    lines2 = [iu_space for _ in lines1]
    del lines2[-1]

    return [lines1, lines2]


def face_mill_altm(data: list, tmd: int, lmd: int, tdn: str, ldn: str) -> list:
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

    wdt, lgt, ang, mat, fed, cut, dyr, pos, tcm, lcm, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    ang = math.radians(ang)
    cuts = math.ceil((((mat - wdt) / 2) * math.cos(ang)) / cut)
    cuts = cuts if cuts % 2 == 0 else cuts + 1

    params = lgt, tmd, lmd, wdt, ang, dia, cuts, cut
    tin, tnd, tds, lsc, lin, lnd, lds = face_milling_params(params)

    tst = tin - (tds)
    lines1 = [
        f"{blk}G90G00{ldn}{fnum3(lsc + lcm)}{tdn}{fnum3(tst * tmd + tcm)}",
        f"{blk}G91G01{ldn}{fnum3((lsc - lin)*-1)}F{ffed(fed)}",
    ]

    cyls = int(cuts / 2)
    lnd -= (lds * cuts)
    lnd *= lmd
    tps = tnd - tst

    for cyl in range(cyls):
        # tin -= tds * tmd
        tcr = "" if cyl == 0 else f"{blk}{tdn}{fnum3(tds * tmd * -1)}"
        cfd = f"F{ffed(fed * 0.5)}" if cyl + 1 == cyls else ""
        lines1.append(tcr)
        lnd += lds * lmd
        lps = lnd - lin

        crl = f"{blk}{ldn}{fnum3(lps)}{tdn}{fnum3(tps * tmd)}"
        tps += tds

        lines1.append(crl)
        lnd += lds * lmd
        crl = f"{blk}{ldn}{fnum3(lds)}"
        lines1.append(crl)
        tin -= tds
        lps += lds
        lps *= -1

        crl = f"{blk}{ldn}{fnum3(lps)}{tdn}{fnum3(tps * tmd * -1)}{cfd}"
        tps += tds
        
        lines1.append(crl)

    lines2 = [iu_space for _ in lines1]
    del lines2[-1]

    return [lines1, lines2]


def face_mill_innm(data: list, tmd: int, lmd: int, tdn: str, ldn: str) -> list:
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

    wdt, lgt, ang, mat, fed, cut, dyr, pos, tcm, lcm, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    ang = math.radians(ang)
    cuts = math.ceil((((mat - wdt) / 2) * math.cos(ang)) / cut)
    cuts = cuts if cuts % 2 == 0 else cuts + 1

    params = lgt, tmd, lmd, wdt, ang, dia, cuts, cut
    tin, tnd, tds, lsc, lin, lnd, lds = face_milling_params(params)

    tst = tin - (tds)
    lines1 = [
        f"{blk}G90G00{ldn}{fnum3(lsc + lcm)}{tdn}{fnum3(tst * tmd + tcm)}",
        f"{blk}G91G01{ldn}{fnum3((lsc - lin)*-1)}F{ffed(fed)}",
    ]

    cyls = cuts
    lnd -= (lds * cuts)
    lnd *= lmd
    tps = tnd - tst

    for cyl in range(cyls):
        tcr = "" if cyl == 0 else f"{blk}G01{tdn}{fnum3(tds * tmd * -1)}"
        cfd = f"F{ffed(fed * 0.5)}" if cyl + 1 == cyls else ""
        lines1.append(tcr)

        lnd += lds * lmd
        lps = lnd - lin
        crl = f"{blk}{ldn}{fnum3(lps)}{tdn}{fnum3(tps * tmd)}{cfd}"
        
        lines1.append(crl)

        crl = f"{blk}G00{ldn}{fnum3(lps * -1)}"
        lines1.append(crl)
        crl = f"{blk}{tdn}{fnum3(tps * tmd * -1)}"
        tps += tds
        lines1.append(crl) if cyl != cuts - 1 else ""

    lines2 = [iu_space for _ in lines1]
    del lines2[-1]

    return [lines1, lines2]


def face_mill_outm(data: list, tmd: int, lmd: int, tdn: str, ldn: str) -> list:
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

    wdt, lgt, ang, mat, fed, cut, dyr, pos, tcm, lcm, dia, blk = data.values()
    iu_space = fspace_ui()
    blk = "/" if blk else ""

    ang = math.radians(ang)
    cuts = math.ceil((((mat - wdt) / 2) * math.cos(ang)) / cut)
    cuts = cuts if cuts % 2 == 0 else cuts + 1

    params = lgt, tmd, lmd, wdt, ang, dia, cuts, cut
    tin, tnd, tds, lsc, lin, lnd, lds = face_milling_params(params)

    cyls = cuts
    lnd -= (lds * cuts)
    lnd *= lmd
    lnd += lds * lmd
    lps = (lsc - lnd) * -1

    lines1 = [
        f"{blk}G90G00{ldn}{fnum3(lsc + lcm)}{tdn}{fnum3(tnd * tmd + tcm)}",
        f"{blk}G91G01{ldn}{fnum3(lps)}F{ffed(fed)}",
    ]

    for cyl in range(cyls):
        tin -= tds
        tcr = "" if cyl == 0 else f"{blk}G01{ldn}{fnum3(lds)}"
        cfd = f"F{ffed(fed * 0.5)}" if cyl + 1 == cyls else ""
        lines1.append(tcr)

        lps = (lnd - lin) * -1
        tps = tnd - tin
        crl = f"{blk}{ldn}{fnum3(lps)}{tdn}{fnum3(tps * tmd * -1)}{cfd}"
        lines1.append(crl)

        crl = f"{blk}G00{tdn}{fnum3(tps * tmd)}"
        lines1.append(crl) if cyl != cuts - 1 else ""
        crl = f"{blk}{ldn}{fnum3(lps * -1)}"
        lines1.append(crl) if cyl != cuts - 1 else ""
        lnd += lds * lmd

    lines2 = [iu_space for _ in lines1]
    del lines2[-1] 

    return [lines1, lines2]


def face_milling_params(params: list) -> list:
    """Calcula dimensiones para fresado de cara plana

    Args:
        params (list): Lista de datos a procesar

    Returns:
        list: Lista de dimensiones calculadas
    """

    lgt, tmd, lmd, wdt, ang, dia, cuts, cut = params

    tds = (cut / math.cos(ang))
    lds = cut / math.sin(ang)
    tin = (((dia / 2) * math.tan((1.5708 - ang) / 2)) + (wdt / 2))
    lnd = (lgt - ((dia / 2) * math.sin(ang)))
    tnd = tin + (((lnd + (dia / 2)) * math.tan(ang)))
    tin = tin + (tds * cuts)
    lsc = (((dia / 2) + 0.025) * lmd * -1)
    lin = ((dia / 2) * lmd * -1)

    return tin, tnd, tds, lsc, lin, lnd, lds
