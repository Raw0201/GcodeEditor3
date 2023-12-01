from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QEvent

from tools.sub_windows import image_load, key_pressed
from subtasks.helper import Helper
from tools.config_list import *


class Subtask(QMainWindow):
    def __init__(self):
        super().__init__()
        self.helper1 = Helper()
        self.setupUi(self)
        self.move(0, 0)

        self.data_pack = None
        self.modification = False
        self.btn_save.clicked.connect(self.collector)

        self.btn_help.clicked.connect(lambda: self.helper(self.image))

    def change_to(self, window, task):
        """Cambia a la función indicada

        Args:
            task (method): Función indicada
        """

        self.close()
        collect_data(window, task)

    def collector(self):
        pass

    def helper(self, image):
        self.helper1.show()
        image_load(self.helper1.lbl_image, image)

    def keyPressEvent(self, qKeyEvent) -> None:
        key_pressed(self, qKeyEvent)

    def closeEvent(self, event: QEvent):
        """Evento de cierre de la ventana

        Args:
            event (QEvent): Evento de cierre
        """

        if self.helper1:
            self.helper1.close()
