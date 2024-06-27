from operator import sub
from subtasks import version, graph, gcodes, mcodes, drill_data, mill_data, thread_data

from tools.main_window import *


def load_menu_actions(window):
    """Cargar acciones del menú

    Args:
        window (QMainWindow): Ventana principal
    """

    window.actionNew.triggered.connect(lambda: new_tape(window))
    window.actionOpen.triggered.connect(lambda: open_file(window))
    window.actionSave.triggered.connect(lambda: save_config(window))
    window.actionClose.triggered.connect(lambda: close_action(window))

    window.actionDelete.triggered.connect(lambda: delete_lines(window))
    window.actionDuplicate.triggered.connect(lambda: duplicate_lines(window))
    window.actionBlock.triggered.connect(lambda: block_lines(window))
    window.actionMove_up.triggered.connect(lambda: movement(window, "up"))
    window.actionMove_down.triggered.connect(lambda: movement(window, "down"))

    window.actionGraph.triggered.connect(lambda: graph_window(window, window.config_list))
    window.actionVersion.triggered.connect(lambda: version_window(window))
    window.actionGCodes.triggered.connect(lambda: gcodes_window(window))
    window.actionMCodes.triggered.connect(lambda: mcodes_window(window))
    window.actionDrillTable.triggered.connect(lambda: drill_window(window))
    window.actionMillTable.triggered.connect(lambda: mill_window(window))
    window.actionThreadTable.triggered.connect(lambda: thread_window(window))

    window.actionGo_to.triggered.connect(lambda: subroutine_prep(window))
    window.actionReturn_to.triggered.connect(lambda: return_to(window))

    window.actionShow_functions.triggered.connect(
        lambda: component_view(window, window.functions_dock)
    )
    window.actionShow_tape1_widget.triggered.connect(
        lambda: component_view(window, window.tape1_widget)
    )
    window.actionShow_tape2_widget.triggered.connect(
        lambda: component_view(window, window.tape2_widget)
    )
    window.actionShow_config_widget.triggered.connect(
        lambda: component_view(window, window.config_widget)
    )
    window.actionG_invert.triggered.connect(
        lambda: gcode_mod(window, "Mov")
    )
    window.actionSubrut_up.triggered.connect(
        lambda: param_mod(window, "Sub", 1.0)
    )
    window.actionSubrut_down.triggered.connect(
        lambda: param_mod(window, "Sub", -1.0)
    )
    window.actionLoop_up.triggered.connect(
        lambda: param_mod(window, "Rep", 1.0)
    )
    window.actionLoop_down.triggered.connect(
        lambda: param_mod(window, "Rep", -1.0)
    )
    window.actionX_invert.triggered.connect(
        lambda: param_invert(window, "Xin")
    )
    window.actionY_invert.triggered.connect(
        lambda: param_invert(window, "Yin")
    )
    window.actionZ_invert.triggered.connect(
        lambda: param_invert(window, "Zin")
    )
    window.actionI_invert.triggered.connect(
        lambda: param_invert(window, "Xcn")
    )
    window.actionJ_invert.triggered.connect(
        lambda: param_invert(window, "Ycn")
    )
    window.actionK_invert.triggered.connect(
        lambda: param_invert(window, "Zcn")
    )
    window.actionS1_move.triggered.connect(
        lambda: side_changer(window, "$1")
    )
    window.actionS2_move.triggered.connect(
        lambda: side_changer(window, "$2")
    )
    window.actionS3_move.triggered.connect(
        lambda: side_changer(window, "$3")
    )
    window.actionX_up.triggered.connect(
        lambda: param_mod(window, "Xin", 0.001)
    )
    window.actionX_down.triggered.connect(
        lambda: param_mod(window, "Xin", -0.001)
    )
    window.actionY_up.triggered.connect(
        lambda: param_mod(window, "Yin", 0.001)
    )
    window.actionY_down.triggered.connect(
        lambda: param_mod(window, "Yin", -0.001)
    )
    window.actionZ_up.triggered.connect(
        lambda: param_mod(window, "Zin", 0.001)
    )
    window.actionZ_down.triggered.connect(
        lambda: param_mod(window, "Zin", -0.001)
    )
    window.actionI_up.triggered.connect(
        lambda: param_mod(window, "Xcn", 0.001)
    )
    window.actionI_down.triggered.connect(
        lambda: param_mod(window, "Xcn", -0.001)
    )
    window.actionJ_up.triggered.connect(
        lambda: param_mod(window, "Ycn", 0.001)
    )
    window.actionJ_down.triggered.connect(
        lambda: param_mod(window, "Ycn", -0.001)
    )
    window.actionK_up.triggered.connect(
        lambda: param_mod(window, "Zcn", 0.001)
    )
    window.actionK_down.triggered.connect(
        lambda: param_mod(window, "Zcn", -0.001)
    )
    window.actionFeed_up.triggered.connect(
        lambda: param_mod(window, "Fed", 0.001)
    )
    window.actionFeed_down.triggered.connect(
        lambda: param_mod(window, "Fed", -0.001)
    )
    window.actionSpeed_up.triggered.connect(
        lambda: param_mod(window, "Spd", 100.0)
    )
    window.actionSpeed_down.triggered.connect(
        lambda: param_mod(window, "Spd", -100.0)
    )


def graph_window(window: QMainWindow, config_list):
    """Crea la ventana de gráfico de tape

    Args:
        window (QMainWindow): Ventana principal
    """

    window.sub_window = graph.Graph(config_list)
    window.sub_window.show()


def version_window(window: QMainWindow):
    """Crea la ventana de info de versión

    Args:
        window (QMainWindow): Ventana principal
    """

    window.sub_window = version.Version()
    window.sub_window.show()

def gcodes_window(window: QMainWindow):
    """Crea la ventana de códigos G
    Args:
        window (QMainWindow): Ventana principal
    """

    window.sub_window = gcodes.Gcodes(window)
    window.sub_window.show()

def mcodes_window(window: QMainWindow):
    """Crea la ventana de códigos M

    Args:
        window (QMainWindow): Ventana principal
    """

    window.sub_window = mcodes.Mcodes(window)
    window.sub_window.show()

def drill_window(window: QMainWindow):
    """Crea la ventana de datos de brocas

    Args:
        window (QMainWindow): Ventana principal
    """

    window.sub_window = drill_data.Drill_data(window)
    window.sub_window.show()

def mill_window(window: QMainWindow):
    """Crea la ventana de datos de fresas

    Args:
        window (QMainWindow): Ventana principal
    """

    window.sub_window = mill_data.Mill_data(window)
    window.sub_window.show()

def thread_window(window: QMainWindow):
    """Crea la ventana de datos de brocas

    Args:
        window (QMainWindow): Ventana principal
    """

    window.sub_window = thread_data.Thread_data(window)
    window.sub_window.show()
