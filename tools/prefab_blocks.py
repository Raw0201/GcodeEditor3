from PySide6.QtWidgets import QMainWindow

from tools.formatting import fnum3


def prefab_space() -> list:
    """Bloque prefabricado de espacio

    Returns:
        list: Bloque prefabricado
    """

    return [
        " ",
        {
            "Fre": " ",
        },
    ]


def prefab_comment(comment: str, side: str) -> list:
    """Bloque prefabricado de comentario


    Args:
        comment (str): Comentario a agregar
        side (str): Lado del programa

    Returns:
        list: Bloque prefabricado
    """

    return [
        "        Comentario",
        {
            "Com": comment,
            "Sde": side,
            "Blk": False,
        },
    ]


def prefab_thread_tool_call(tool: int, xin: float, zin: float) -> list:
    """Bloque prefabricado de llamada de herramienta

    Args:
        tool (int): Número de herramienta
        xin (float): Posición inicial eje X
        zin (float): Posición inicial eje Z

    Returns:
        list: Bloque prefabricado
    """

    return [
        "    Llamar herramienta",
        {
            "Tol": tool,
            "Typ": "CUCHILLA",
            "Dia": 0.0,
            "Spc": "ROSCAR",
            "Sde": "$1",
            "Xin": xin,
            "Yin": 0.0,
            "Zin": zin,
            "Mcd": "NO",
            "Com": "-",
            "Blk": False,
        },
    ]


def prefab_cutoff_tool_call(tool: int, xin: float, zin: float) -> list:
    """Bloque prefabricado de llamada de herramienta de tronzado

    Args:
        tool (int): Número de herramienta
        xin (float): Posición inicial eje X
        zin (float): Posición inicial eje Z

    Returns:
        list: Bloque prefabricado
    """

    return [
        "    Llamar herramienta",
        {
            "Tol": tool,
            "Typ": "CUCHILLA",
            "Dia": 0.0,
            "Spc": "TRONZAR",
            "Sde": "$1",
            "Xin": xin,
            "Yin": 0,
            "Zin": zin,
            "Mcd": "NO",
            "Com": "-",
            "Blk": False,
        },
    ]


def prefab_center_drill_tool_call(
    tool: int, xin: float, yin: float, zin: float, side: str
) -> list:
    """Bloque prefabricado de llamada de herramienta de perforado

    Args:
        tool (int): Número de herramienta
        xin (float): Posición inicial eje X
        yin (float): Posición inicial eje Y
        zin (float): Posición inicial eje Z
        side (str): Lado del programa

    Returns:
        list: Bloque prefabricado
    """

    return [
        "    Llamar herramienta",
        {
            "Tol": tool,
            "Typ": "SPOT",
            "Dia": 0.25,
            "Spc": "90 GRD",
            "Sde": side,
            "Xin": xin,
            "Yin": yin,
            "Zin": zin,
            "Mcd": "INICIO PERFORADO",
            "Com": "-",
            "Blk": False,
        },
    ]


def prefab_drill_tool_call(
    tool: int, xin: float, yin: float, zin: float, side: str
) -> list:
    """Bloque prefabricado de llamada de herramienta de perforado

    Args:
        tool (int): Número de herramienta
        xin (float): Posición inicial eje X
        yin (float): Posición inicial eje Y
        zin (float): Posición inicial eje Z
        side (str): Lado del programa

    Returns:
        list: Bloque prefabricado
    """

    return [
        "    Llamar herramienta",
        {
            "Tol": tool,
            "Typ": "BROCA",
            "Dia": 0.0,
            "Spc": "-",
            "Sde": side,
            "Xin": xin,
            "Yin": yin,
            "Zin": zin,
            "Mcd": "NO",
            "Com": "-",
            "Blk": False,
        },
    ]


def prefab_tapping_tool_call(
    tool: int, xin: float, yin: float, zin: float, side: str
) -> list:
    """Bloque prefabricado de llamada de herramienta de roscado

    Args:
        tool (int): Número de herramienta
        xin (float): Posición inicial eje X
        yin (float): Posición inicial eje Y
        zin (float): Posición inicial eje Z
        side (str): Lado del programa

    Returns:
        list: Bloque prefabricado
    """

    return [
        "    Llamar herramienta",
        {
            "Tol": tool,
            "Typ": "MACHO ROSCAR",
            "Dia": 0.0,
            "Spc": "-",
            "Sde": side,
            "Xin": xin,
            "Yin": yin,
            "Zin": zin,
            "Mcd": "NO",
            "Com": "-",
            "Blk": False,
        },
    ]


def prefab_csink_tool_call(
    tool: int, angle: float, xin: float, yin: float, zin: float, side: str
) -> list:
    """Bloque prefabricado de llamada de herramienta de perforado

    Args:
        tool (int): Número de herramienta
        angle (float): Ángulo de la punta de la herramienta
        xin (float): Posición inicial eje X
        yin (float): Posición inicial eje Y
        zin (float): Posición inicial eje Z
        side (str): Lado del programa

    Returns:
        list: Bloque prefabricado
    """

    return [
        "    Llamar herramienta",
        {
            "Tol": tool,
            "Typ": "SPOT",
            "Dia": 0.25,
            "Spc": f"{fnum3(angle)} GRD",
            "Sde": side,
            "Xin": xin,
            "Yin": yin,
            "Zin": zin,
            "Mcd": "NO",
            "Com": "-",
            "Blk": False,
        },
    ]


def prefab_tool_close(tool: int, side: str, bar: float) -> list:
    """Bloque prefabricado de cierre de herramienta

    Args:
        tool (int): Número de herramienta
        side (str): Lado del programa
        bar (float): Diámetro de la barra utilizada

    Returns:
        list: Bloque prefabricado
    """

    return [
        "    Cerrar herramienta",
        {
            "Tol": tool,
            "Sde": side,
            "Dia": bar,
            "Blk": False,
        },
    ]


def prefab_spindle(speed: int, rotation: str, side: str) -> list:
    """Bloque prefabricado de activación de husillo

    Args:
        speed (int): Velocidad de giro
        rotation (str): Dirección de rotación
        side (str): Lado del programa

    Returns:
        list: Bloque prefabricado
    """

    return [
        "        Giro del husillo",
        {"Spd": speed, "Rot": rotation, "Sde": side, "Blk": False},
    ]


def prefab_sub_header(window: QMainWindow, description: str) -> list:
    """Bloque prefabricado de encabezado de subrutina

    Args:
        window (QMainWindow): Ventana principal
        description (str): Descripción de la subrutina

    Returns:
        list: Bloque prefabricado
    """

    return [
        "Inicio de subrutina",
        {
            "Pgr": window.current_subroutine,
            "Mnp": window.current_main_program,
            "Dsc": description,
            "Plt": window.platter_data,
            "Tol": window.subroutine_tool,
            "Typ": window.subroutine_tool_type,
            "Dia": window.subroutine_tool_diameter,
            "Spc": window.subroutine_tool_specification,
            "Mch": window.subroutine_machine,
            "Lgt": window.current_part_length,
        },
    ]


def prefab_mill_end() -> list:
    """Bloque prefabricado de cierre de fresados

    Returns:
        list: Bloque prefabricado
    """

    return [
        "    * Finalizar fresados",
        {
            "Blk": False,
        },
    ]


def prefab_drill_end() -> list:
    """Bloque prefabricado de cierre de perforados

    Returns:
        list: Bloque prefabricado
    """

    return [
        "    * Finalizar perforados",
        {
            "Blk": False,
        },
    ]


def prefab_center_drill(depth: float, feed: float) -> list:
    """Bloque prefabricado de cierre de perforados

    Args:
        depth (float): Profundidad del perforado
        feed (float): Avance de corte

    Returns:
        list: Bloque prefabricado
    """

    return [
        "        Agujero centro",
        {
            "Dpt": depth,
            "Fed": feed,
            "Xin": 0.0,
            "Yin": 0.0,
            "Zin": -0.02,
            "Rtr": 0.0,
            "Dwl": 0.0,
            "Sde": "$1",
            "Sys": "ABSOLUTO",
            "Znd": "Z INICIAL",
            "Blk": False,
        },
    ]
