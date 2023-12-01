import os
import contextlib

from tools.constants import *
from PySide6.QtWidgets import QMainWindow


def create_machine_folders():
    """Crea los folders por defecto para los archivos de configuración"""

    root = ROOT_DIR
    machines = MACHINES

    with contextlib.suppress(FileExistsError):
        os.mkdir(root)
    os.chdir(root)

    with contextlib.suppress(FileExistsError):
        for machine in machines:
            os.mkdir(machine)


def update_file_dir(window: QMainWindow):
    """Actualiza el folder de guardado

    Args:
        window (QMainWindow): Ventana principal
    """

    root = ROOT_DIR
    window.current_folder = f"{root}/{window.current_machine}"
    os.chdir(window.current_folder)
