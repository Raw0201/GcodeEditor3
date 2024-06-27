swiss_compensations = {
    11: 0.06,
    14: 0.1,
    15: 0.03,
    16: 0.295,
    17: 0.295,
    18: 0.295,
}

kswiss_compensations = {
    1: 0.06,
    4: 0.1,
    5: 0.03,
    11: 0.394,
    12: 0.394,
    13: 0.394,
    14: 0.394,
}

swiss_kswiss_tools = {
    11: 1,
    12: 2,
    13: 3,
    14: 4,
    15: 5,
    16: 11,
    17: 12,
    18: 13,
}

kswiss_swiss_tools = {
    1: 11,
    2: 12,
    3: 13,
    4: 14,
    5: 15,
    11: 16,
    12: 17,
    13: 18,
    14: 18,
}


def kswiss_to_swiss(tool: int, side: str) -> int:
    """Convierte números de herramienta desde K

    Args:
        tool (int): Número de herramienta
        side (str): Lado del programa

    Returns:
        int: Número de herramienta convertido
    """

    tools1 = {1: 11, 2: 12, 3: 13, 4: 14, 5: 15}
    tools2 = {11: 16, 12: 17, 13: 18, 14: 18}

    if side == "$1" and tool in tools1:
        tool = tools1[tool]
    elif side == "$3" and tool in tools2:
        tool = tools2[tool]

    return tool


def swiss_to_kswiss(tool: int, side: str) -> int:
    """Convierte números de herramienta hacia K

    Args:
        tool (int): Número de herramienta
        side (str): Lado del programa

    Returns:
        int: Número de herramienta convertido
    """

    tools1 = {11: 1, 12: 2, 13: 3, 14: 4, 15: 5}
    tools2 = {16: 11, 17: 12, 18: 13}

    if side == "$1" and tool in tools1:
        tool = tools1[tool]
    elif side == "$3" and tool in tools2:
        tool = tools2[tool]

    return tool
