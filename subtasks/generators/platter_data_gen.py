from tools.formatting import *
import math


def platter_data_gen(machine: str, data: list) -> list:
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

    lines1, lines2 = [""], [""]

    return [lines1, lines2]


def gen_e16(data: list) -> list:
    """Genera los códigos para torno suizo E16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    lines1, lines2 = [""], [""]

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
    cqt, csp, rqt, rsp, xsp, ysp, xdm, ydm, xcm, ycm, blk = data.values()
    iu_space = fspace_ui()

    lines1 = [f"(DIST CENTROS: X{fnum3(csp)} Y{fnum3(rsp)})"]
    lines2 = [iu_space]

    return [lines1, lines2]


def matrix_gen(data: list) -> list:
    """Genera cuadrícula de piezas de platina

    Args:
        data (dict): Datos suministrados

    Returns:
        list: Lista de puntos XY para cada pieza
    """
    cqt, csp, rqt, rsp, xsp, ysp, xdm, ydm, xcm, ycm, blk = data.values()

    # cqt = Column quantity        csp = Column center distance
    # rqt = Row quantity           rsp = Row center distance
    # xsp = X space                ysp = Y space
    # xdm = X material dimension   ydm = Y material dimension
    # xcm = X compensation         ycm = Y compensation

    pcx = csp - xsp  # Piece lenght
    pcy = rsp - ysp  # Piece width
    wlx = (cqt - 1) * csp  # Work lenght X
    wly = (rqt - 1) * rsp  # Work lenght Y

    msx = (wlx - xdm) / 2  # Matrix start X
    msy = (wly - ydm) / 2 - wly  # Matrix start Y
    ssx = msx if xcm == 0 else (xcm + (pcx / 2)) * -1  # Square start X
    ssy = msy if ycm == 0 else (ycm + (pcy / 2) + wly) * -1  # Square start Y

    lsx = msx + ((pcx + xsp) / 2)  # Lineal start X
    lsy = msy - ((pcy + ysp) / 2)  # Lineal start Y

    lin_prm = [
        rqt,
        cqt,
        csp,
        rsp,
        xsp,
        ysp,
        lsx,
        lsy,
        pcx,
        pcy,
        xdm,
        ydm,
    ]  # Lineal parameters
    sqr_prm = [rqt, cqt, csp, rsp, ssx, ssy]  # Square parameters

    lin_x = lineal_x_gen(lin_prm)  # Lineal matrix X
    lin_y = lineal_y_gen(lin_prm)  # Lineal matrix Y
    sqr_xy = square_xy_gen(sqr_prm)  # Square matrix XY
    sqr_yx = square_yx_gen(sqr_prm)  # Square matrix YX

    return [lin_x, lin_y, sqr_xy, sqr_yx]


def lineal_x_gen(lin_prm: list) -> list:
    """Genera lista de puntos de líneas en eje X

    Args:
        lin_prm (list): Lista de parámetros para líneas

    Returns:
        list: Lista de puntos de líneas
    """
    rqt, cqt, csp, rsp, xsp, ysp, lsx, lsy, pcx, pcy, xdm, ydm = lin_prm
    xps = (ysp / 2) + 0.05  # Initial position X
    yps = lsy  # Initial position Y
    fdx = xps - lsx + pcx + xsp  # First displacement X
    ldx = (xps * 2) + xdm - fdx  # Last displacement X

    lin_x = [[xps, yps, fdx, ldx]]  # Line data X

    for _ in range(rqt):
        yps += rsp
        lin_x.append([xps, yps, fdx, ldx])

    return lin_x


def lineal_y_gen(lin_prm: list) -> list:
    """Genera lista de puntos de líneas en eje Y

    Args:
        lin_prm (list): Lista de parámetros para líneas

    Returns:
        list: Lista de puntos de líneas
    """
    rqt, cqt, csp, rsp, xsp, ysp, lsx, lsy, pcx, pcy, xdm, ydm = lin_prm

    xps = lsx  # Position X
    yps = lsy  # Position Y
    fdx = rsp  # First displacement X
    ldx = rsp * (rqt - 1)  # Last displacement

    lin_y = [[xps, yps, fdx, ldx]]  # Line data Y

    for _ in range(cqt):
        xps -= csp
        lin_y.append([xps, yps, fdx, ldx])

    return lin_y


def square_xy_gen(sqr_prm: list) -> list:
    """Genera lista de puntos en dirección X-Y

    Args:
        matrix_params (list): Lista de parámetros para cuadrícula

    Returns:
        list: Lista de puntos de cuadrícula
    """
    rqt, cqt, csp, rsp, xsp, ysp = sqr_prm

    sqr_xy = []  # Square data X-Y
    xps = xsp  # Initial position X
    yps = ysp  # Initial position Y
    xdr = "NEG"  # Displacement direction X
    cnt = 1  # Piece counter

    for _ in range(rqt):
        for _ in range(cqt - 1):
            sqr_xy.append([xps, yps])
            if xdr == "NEG":
                cnt += 1
                xps -= csp
                if cnt == cqt:
                    sqr_xy.append([xps, yps])
                    xdr = "POS"
                    yps += rsp
            else:
                cnt -= 1
                xps += csp
                if cnt == 1:
                    sqr_xy.append([xps, yps])
                    xdr = "NEG"
                    yps += rsp
    return sqr_xy


def square_yx_gen(sqr_prm: list) -> list:
    """Genera lista de puntos en dirección Y-X

    Args:
        matrix_params (list): Lista de parámetros para cuadrícula

    Returns:
        list: Lista de puntos de cuadrícula
    """
    rqt, cqt, csp, rsp, xsp, ysp = sqr_prm

    sqr_yx = []  # Square data Y-X
    xps = xsp  # Initial position X
    yps = ysp  # Initial position Y
    ydr = "POS"  # Displacement direction Y
    cnt = rqt  # Piece counter

    for _ in range(cqt):
        for _ in range(rqt - 1):
            sqr_yx.append([xps, yps])
            if ydr == "POS":
                cnt -= 1
                yps += rsp
                if cnt == 1:
                    sqr_yx.append([xps, yps])
                    ydr = "NEG"
                    xps -= csp
            else:
                cnt += 1
                yps -= rsp
                if cnt == rqt:
                    sqr_yx.append([xps, yps])
                    ydr = "POS"
                    xps -= csp
    return sqr_yx
