# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Physical_Simulation.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QMainWindow,
    QSizePolicy, QWidget)

class Ui_Simulation(object):
    def setupUi(self, Simulation):
        if not Simulation.objectName():
            Simulation.setObjectName(u"Simulation")
        Simulation.resize(1920, 1280)
        Simulation.setMinimumSize(QSize(1280, 800))
        self.centralwidget = QWidget(Simulation)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        Simulation.setCentralWidget(self.centralwidget)

        self.retranslateUi(Simulation)

        QMetaObject.connectSlotsByName(Simulation)
    # setupUi

    def retranslateUi(self, Simulation):
        Simulation.setWindowTitle(QCoreApplication.translate("Simulation", u"Physical Simulation", None))
    # retranslateUi

