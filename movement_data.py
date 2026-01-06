from PySide6.QtWidgets import QFrame
from ui.movement_data_ui import Ui_Frame


class movement_data(QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super(movement_data, self).__init__(parent)
        self.setupUi(self)

        self.openGLWidget.setStyleSheet("background-color: white;")
        self.openGLWidget_2.setStyleSheet("background-color: white;")
        self.openGLWidget_3.setStyleSheet("background-color: white;")
        self.openGLWidget_4.setStyleSheet("background-color: white;")
        self.openGLWidget_5.setStyleSheet("background-color: white;")