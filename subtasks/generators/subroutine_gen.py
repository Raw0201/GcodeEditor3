from tools.formatting import *


def subroutine_gen(machine: str, data: list) -> list:
    """Genera las líneas de tape

    Args:
        machine (str): Tipo de máquina utilizada
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape
    """

    sub, rep, com, blk = data.values()
    iu_space = fspace_ui()

    blk = "/" if blk else ""
    rep = f"L{int(rep)}" if rep > 0 else ""
    com1 = f"G50W{fnum3(com)}" if com  != 0 else ""
    com2 = f"G50W{fnum3(com * -1)}" if com  != 0 else ""

    lines1 = [com1, f"{blk}M98P{sub}{rep}", com2]
    lines2 = [iu_space for _ in lines1] if com != 0 else [iu_space]
    return [lines1, lines2]
