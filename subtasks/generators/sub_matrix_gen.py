from tools.formatting import *
import math


def sub_matrix_gen(machine: str, data: list) -> list:
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
    sub, qty, spc, axs, xin, yin, zin, rep, ubk, cnt, sec, mtx, blk = data.values()
    iu_space = fspace_ui()

    rep = f"L{rep}" if rep > 1 else ""
    znd = fnum3(zin)

    lines1 = []
    ubk_len = len(mtx) + ubk

    for pts, point in enumerate(mtx):
        zsc = fnum3(zin)
        xpn, ypn = fnum4(point[0]), fnum4(point[1])
        pcn = int(cnt + pts)

        if ubk >= 0:
            if pts >= ubk or blk:
                blk = "/"
            else:
                blk = ""
        else:
            if pts < ubk_len:
                blk = "/"
            else:
                blk = ""

        lines1.append(f"{blk}G90G00X{xpn}Y{ypn}Z{zsc}({pcn})")
        lines1.append(f"{blk}M98P{sub}{rep}")
        lines1.append(f"{blk}G90G00Z{zsc}") if sec == "SÍ" else ""

    lines2 = [iu_space for _ in lines1]

    return [lines1, lines2]


def matrix_gen(data: list) -> list:
    """Genera cuadrícula de piezas de platina

    Args:
        data (dict): Datos suministrados

    Returns:
        list: Lista de puntos XY para cada pieza
    """
    sub, qty, spc, axs, xin, yin, zin, rep, ubk, cnt, sec, mtx, blk = data.values()

    lin_prm = [qty, spc, xin, yin]  # Lineal parameters

    lin_x = lineal_x_gen(lin_prm)  # Lineal matrix X
    lin_y = lineal_y_gen(lin_prm)  # Lineal matrix Y

    return [lin_x, lin_y]


def lineal_x_gen(lin_prm: list) -> list:
    """Genera lista de puntos de matriz de columnas

    Args:
        lin_prm (list): Lista de parámetros para líneas

    Returns:
        list: Lista de puntos de líneas
    """
    qty, spc, xin, yin = lin_prm

    lin_x = [[xin, yin]]  # Line data Y

    for _ in range(qty - 1):
        xin += spc
        lin_x.append([xin, yin])

    return lin_x


def lineal_y_gen(lin_prm: list) -> list:
    """Genera lista de puntos de matriz de filas

    Args:
        lin_prm (list): Lista de parámetros para líneas

    Returns:
        list: Lista de puntos de líneas
    """
    qty, spc, xin, yin = lin_prm

    lin_y = [[xin, yin]]  # Line data X

    for _ in range(qty - 1):
        yin += spc
        lin_y.append([xin, yin])

    return lin_y
