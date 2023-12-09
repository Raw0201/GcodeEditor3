import tools
import contextlib

from PySide6.QtWidgets import (
    QMainWindow,
    QAbstractItemView,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
)


def load_main_widgets_connections(window: QMainWindow):
    """Carga las conexiones de los widgets de la pantalla principal

    Args:
        window (QMainWindow): Ventana principal
    """

    window.config_widget.clicked.connect(
        lambda: widget_clicked(window, "conf")
    )
    window.tape1_widget.clicked.connect(
        lambda: widget_clicked(window, "tape1")
    )
    window.tape2_widget.clicked.connect(
        lambda: widget_clicked(window, "tape2")
    )

    window.config_widget.itemDoubleClicked.connect(
        lambda: item_modifier(window)
    )
    window.tape1_widget.itemDoubleClicked.connect(
        lambda: item_modifier(window)
    )
    window.tape2_widget.itemDoubleClicked.connect(
        lambda: item_modifier(window)
    )

    window.config_widget.itemSelectionChanged.connect(
        lambda: config_selected(window)
    )
    window.tape1_widget.itemSelectionChanged.connect(
        lambda: tape_selected(window, "tape1")
    )
    window.tape2_widget.itemSelectionChanged.connect(
        lambda: tape_selected(window, "tape2")
    )

    window.tape1_widget.verticalScrollBar().valueChanged.connect(
        lambda: widget_scroll(window, window.tape1_widget.verticalScrollBar().value(), "tape1")
    )
    window.tape2_widget.verticalScrollBar().valueChanged.connect(
        lambda: widget_scroll(window, window.tape2_widget.verticalScrollBar().value(), "tape2")
    )


def update_config_widget(window: QMainWindow):
    """Actualiza los datos en el widget de configuración

    Args:
        window (QMainWindow): Ventana principal
    """

    config_lines = window.config_list
    window.config_widget.setRowCount(len(config_lines))
    for num, line in enumerate(config_lines):
        task_name = line[0]
        window.config_widget.setItem(num, 0, QTableWidgetItem(task_name))


def update_tape_widget(widget: QTableWidget, tape: list):
    """Actualiza los datos en el widget de tape

    Args:
        widget (QTableWidget): Widget de visualización de datos
        tape (list): Lista de líneas de tape
    """

    widget.setRowCount(len(tape))
    for num, line in enumerate(tape):
        widget.setItem(num, 0, QTableWidgetItem(line[1]))


def update_config_widget_selection(window: QMainWindow):
    """Actualiza la selección de items en el widget de configuración

    Args:
        window (QMainWindow): Ventana principal
    """

    all_items = [
        window.config_widget.item(index_number, 0)
        for index_number in range(len(window.config_list))
    ]

    indexes = window.current_selection
    items = [window.config_widget.item(index, 0) for index in indexes]

    items_selector(all_items, items, window.config_widget)

def update_tape_widget_selection(window: QMainWindow, widget: str):
    """Actualiza la selección de items en el widget de tape1

    Args:
        window (QMainWindow): Ventana principal
        widget (str): Widget del item seleccionado
    """

    list = window.tape1_list if widget == "tape1" else window.tape2_list
    widget_obj = window.tape1_widget if widget == "tape1" else window.tape2_widget

    all_items = [
        widget_obj.item(index_number, 0)
        for index_number in range(len(list))
    ]

    config_indexes = window.current_selection
    indexes = [
        num
        for num, index in enumerate(list)
        if index[0] in config_indexes
    ]
    items = [widget_obj.item(index, 0) for index in indexes]

    items_selector(all_items, items, widget_obj)


def items_selector(all_items: list, items: list, widget: QWidget):
    """Selector de items en los widgets

    Args:
        all_items (list): Lista total de items en el widget
        items (list): Lista de items a seleccionar
        widget (QWidget): Widget a seleccionar
    """

    with contextlib.suppress(AttributeError, IndexError):
        for item in all_items:
            item.setSelected(False)
        for item in items:
            item.setSelected(True)
        view = QAbstractItemView
        widget.scrollToItem(items[-1], view.EnsureVisible)


def widget_clicked(window: QMainWindow, widget: str):
    """Recibe la señal de item seleccionado en los widgets

    Args:
        window (QMainWindow): Ventana principal
        widget (str): Widget del item seleccionado
    """

    window.current_widget = widget

    if widget == "conf":
        config_selected(window)
    else:
        tape_selected(window, widget)


def config_selected(window: QMainWindow):
    """Actualiza la lista de índices seleccionados en la configuración

    Args:
        window (QMainWindow): Ventana principal
    """

    if window.current_widget == "conf":
        if selected_items := window.config_widget.selectedItems():
            config_lines = []
            config_lines.extend(
                item.row() for item in selected_items if item.column() == 0
            )
            window.current_selection = sorted(list(set(config_lines)))

            update_tape_widget_selection(window, "tape1")
            update_tape_widget_selection(window, "tape2")


def tape_selected(window: QMainWindow, widget: str):
    """Actualiza la lista de índices seleccionados en el tape1

    Args:
        window (QMainWindow): Ventana principal
        widget (str): Widget del item seleccionado
    """

    widget_obj = window.tape1_widget if widget == "tape1" else window.tape2_widget

    if window.current_widget == widget:
        if selected_items := widget_obj.selectedItems():
            items_selection(window, selected_items)


def items_selection(window: QMainWindow, selected_items: list):
    """Actualiza la lista de índices seleccionados

    Args:
        window (QMainWindow): Ventana principal
        selected_items (list): Lista de items seleccionados
    """

    selected_list = []
    selected_list.extend(
        item.row() for item in selected_items if item.column() == 0
    )

    config_lines = [window.tape1_list[line][0] for line in selected_list]
    window.current_selection = sorted(list(set(config_lines)))

    widget = "tape2" if window.current_widget == "tape1" else "tape1"

    update_config_widget_selection(window)
    update_tape_widget_selection(window, widget)


def item_modifier(window: QMainWindow):
    """Obtiene la línea de configuración a modificar

    Args:
        window (QMainWindow): Ventana principal
    """

    line = window.current_selection
    task = window.config_list[line[0]][0]
    data = window.config_list[line[0]][1]

    task_class = tools.sub_tasks.get_task_class(task)
    window.subtask1 = task_class(window)
    window.subtask1.modifier(data)


def update_data_widgets(window: QMainWindow):
    """Actualiza los datos en los widgets

    Args:
        window (QMainWindow): Ventana principal
    """

    update_config_widget(window)
    update_tape_widget(window.tape1_widget, window.tape1_list)
    update_tape_widget(window.tape2_widget, window.tape2_list)

    update_config_widget_selection(window)
    update_tape_widget_selection(window, "tape1")
    update_tape_widget_selection(window, "tape2")


def widget_scroll(window: QMainWindow, index: int, widget: str):
    """Recibe la señal de desplazamiento de la barra vertical

    Args:
        window (QMainWindow): Ventana principal
        index (int): Posición de la barra de desplazamiento
        widget (str): Widget del item seleccionado
    """
    
    widget_obj = window.tape2_widget if widget == "tape1" else window.tape1_widget
    widget_obj.verticalScrollBar().setValue(index)
