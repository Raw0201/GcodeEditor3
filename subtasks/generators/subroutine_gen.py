from tools.formatting import *


def subroutine_gen(machine: str, data: list) -> list:
    """Genera las líneas de tape

    Args:
        machine (str): Tipo de máquina utilizada
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape
    """

    sub, rep, blk = data.values()
    blank_space = fspace()

    blk = "/" if blk else ""
    rep = f"L{int(rep)}" if rep > 0 else ""

    lines1 = [f"{blk}M98P{sub}{rep}"]
    lines2 = [blank_space]
    return [lines1, lines2]
