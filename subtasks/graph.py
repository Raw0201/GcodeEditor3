from PySide6.QtWidgets import QMainWindow

from tools.sub_windows import key_pressed
from interfaces.ui_graph import Ui_frm_graph


class Graph(QMainWindow, Ui_frm_graph):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.vertical_moves = [0, 0, 0.1, 0.1]
        self.trasversal_moves = [0.05, 0.1, 0.15, 0.25]
        self.horizontal_moves = [0, 0, 0.15, 0.25]
        self.rapid_horizontal = [-0.05, 0]
        self.rapid_vertical = [-0.05, 0]

        self.graph_constructor()

    def graph_constructor(self):

        self.graph1_widget.setTitle("X - Z")
        self.graph1_widget.plot(
            self.horizontal_moves,
            self.vertical_moves,
            pen="blue",
        )
        self.graph1_widget.plot(
            self.rapid_horizontal,
            self.rapid_vertical,
            pen="gray",
        )
        # self.graph1_widget.setAspectLocked()
        self.graph1_widget.getPlotItem().hideAxis("bottom")
        self.graph1_widget.getPlotItem().hideAxis("left")

        self.graph2_widget.setTitle("Y - Z")
        self.graph2_widget.plot(self.horizontal_moves, self.trasversal_moves)
        # self.graph2_widget.setAspectLocked()
        self.graph2_widget.getPlotItem().hideAxis("bottom")
        self.graph2_widget.getPlotItem().hideAxis("left")

        # self.graph1_widget.setXLink(self.graph2_widget)

    def keyPressEvent(self, qKeyEvent) -> None:
        key_pressed(self, qKeyEvent)
