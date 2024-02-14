from PySide6.QtWidgets import QMessageBox


def new_tape_question(self) -> QMessageBox:
    """Mensaje de nuevo programa en blanco

    Returns:
        QMessageBox: Caja de texto
    """

    return QMessageBox.question(
        self,
        "Nuevo programa",
        "¿Desea comenzar un nuevo programa en blanco?",
        buttons=QMessageBox.Yes | QMessageBox.No,
        defaultButton=QMessageBox.No,
    )


def new_subroutine_question(self) -> QMessageBox:
    """Mensaje de creación de nueva subrutina

    Returns:
        QMessageBox: Caja de texto
    """

    return QMessageBox.question(
        self,
        "Subrutina no encontrada",
        "¿Desea crear una nueva subrutina?",
        buttons=QMessageBox.Yes | QMessageBox.No,
        defaultButton=QMessageBox.No,
    )


def data_type_error(self) -> QMessageBox:
    """Mensaje de error en tipo de datos

    Returns:
        QMessageBox: Caja de texto
    """

    return QMessageBox.critical(
        self,
        "Error en tipo de datos",
        "Tipo de datos no válido",
    )


def required_data_error(self) -> QMessageBox:
    """Mensaje de error en datos requeridos

    Returns:
        QMessageBox: Caja de texto
    """

    return QMessageBox.critical(
        self,
        "Datos faltantes",
        "Digite los datos requeridos para la operación",
    )


def movement_error_information(self) -> QMessageBox:
    """Mensaje de error en movimiento de líneas

    Returns:
        QMessageBox: Caja de texto
    """

    return QMessageBox.information(
        self,
        "Movimiento no permitido",
        "El encabezado y fin de programa\nno deben ser movidos",
    )


def delete_header_information(self) -> QMessageBox:
    """Mensaje de error en borrado de información

    Returns:
        QMessageBox: Caja de texto
    """

    return QMessageBox.information(
        self,
        "Borrando encabezado",
        "El encabezado del programa no debe ser borrado",
    )


def delete_lines_warning(self) -> QMessageBox:
    """Mensaje de confirmación de borrado de información

    Returns:
        QMessageBox: Caja de texto
    """

    return QMessageBox.warning(
        self,
        "Borrar líneas",
        "¿Desea borrar las líneas seleccionadas?",
        buttons=QMessageBox.Yes | QMessageBox.No,
        defaultButton=QMessageBox.No,
    )


def duplicate_header_information(self) -> QMessageBox:
    """Mensaje de información de duplicación de información

    Returns:
        QMessageBox: Caja de texto
    """

    return QMessageBox.information(
        self,
        "Duplicando encabezado",
        "El encabezado no debe ser duplicado",
    )


def file_open_error(self) -> QMessageBox:
    """Mensaje de error en apertura de archivo

    Returns:
        QMessageBox: Caja de texto
    """

    return QMessageBox.critical(
        self,
        "Error al abrir archivo",
        "No se puede cargar el programa seleccionado",
    )

def machine_error_information(self) -> QMessageBox:
    """Mensaje de error en selección de máquina

    Returns:
        QMessageBox: Caja de texto
    """

    return QMessageBox.information(
        self,
        "Error en selección de máquina",
        "Seleccione un tipo de máquina para mostrar los comandos",
    )