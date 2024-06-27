from PySide6.QtWidgets import QMainWindow

from tools.sub_windows import key_pressed
from interfaces.ui_graph import Ui_frm_graph
from tools.constants import *

class Graph(QMainWindow, Ui_frm_graph):
    def __init__(self, config_list):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f"{APP_NAME} - Gráfico")

        self.cross_x = [0, 0.005, -0.005, 0, 0.005, -0.005, 0]
        self.cross_y = [0, 0.005, -0.005, 0, -0.005, 0.005, 0]

        self.horizontal_moves = [0, .05, 0.15, 0.25]
        self.vertical_moves = [0, .05, 0.1, 0.1]
        self.trasversal_moves = [0.05, 0.1, 0.15, 0.25]
        self.rapid_horizontal = [-0.05, 0]
        self.rapid_vertical = [-0.05, 0]

        self.moves = [
            [0, 0.1, "darkgray"],
            [0.15, 0.1, "blue"],
            [0.25, 0.2, "gray"],
            [0.35, 0.2, "blue"],
        ]

        self.graph_constructor()

    def graph_constructor(self):

        self.graph1_widget.setTitle("X - Z")
        
        self.graph1_widget.plot(
            self.cross_x,
            self.cross_y,
            pen="yellow",
        )

        for num in range(len(self.moves)):
            first_horiz = 0 if num == 0 else last_horiz
            last_horiz = self.moves[num][0]
            first_vert = 0 if num == 0 else last_vert
            last_vert = self.moves[num][1]

            self.graph1_widget.plot(
                [first_horiz, last_horiz],
                [first_vert, last_vert],
                pen = self.moves[num-1][2],
            )


        self.graph1_widget.setAspectLocked()
        self.graph1_widget.getPlotItem().hideAxis("bottom")
        self.graph1_widget.getPlotItem().hideAxis("left")

        self.graph2_widget.setTitle("Y - Z")
        self.graph2_widget.plot(self.horizontal_moves, self.trasversal_moves)
        self.graph2_widget.setAspectLocked()
        self.graph2_widget.getPlotItem().hideAxis("bottom")
        self.graph2_widget.getPlotItem().hideAxis("left")

        # self.graph1_widget.setXLink(self.graph2_widget)

    def keyPressEvent(self, qKeyEvent) -> None:
        key_pressed(self, qKeyEvent)
