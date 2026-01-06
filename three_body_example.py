from PySide6.QtWidgets import QFrame
from ui.three_body_example_ui import Ui_Frame


class three_body_example(QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super(three_body_example, self).__init__(parent)
        self.setupUi(self)