import sys

from PySide6 import QtCore
from PySide6.QtCore import QLibraryInfo, QTranslator
from PySide6.QtWidgets import QApplication, QMainWindow

from tools.widgets import *
from tools.sub_tasks import *
from tools.directories import *
from tools.menu_actions import *
from tools.main_buttons import *
from tools.default_data import *

from interfaces.ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # ? Datos por defecto de la aplicación
        # ? ----------------------------------------------------------------- *

        load_persistent_data(self)
        load_default_data_lists(self)
        load_default_variables(self)
        load_default_tape_conditions(self)
        load_default_machining_data(self)
        load_default_subroutine_data(self)
        load_default_plate_data(self)
        load_main_buttons(self)
        load_main_title(self)

        # ? Botones y acciones de la pantalla principal
        # ? ----------------------------------------------------------------- *

        load_default_buttons_status(self)
        load_main_buttons_connections(self)
        load_menu_actions(self)

        # ? Widgets de la pantalla principal
        # ? ----------------------------------------------------------------- *

        load_default_window_components(self)
        load_main_widgets_connections(self)

        # ? Folders de almacenamiento de tapes
        # ? ----------------------------------------------------------------- *

        create_machine_folders()

    def closeEvent(self, event: QEvent):
        """Evento de cierre de la ventana

        Args:
            event (QEvent): Evento de cierre
        """

        close_app(self, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    translator = QTranslator(app)
    translations = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    translator.load("qt_es", translations)
    app.installTranslator(translator)

    window = MainWindow()
    window.show()
    window.setWindowState(window.windowState() or QtCore.Qt.WindowMaximized)

    sys.exit(app.exec())
