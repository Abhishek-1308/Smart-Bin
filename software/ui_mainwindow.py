# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLCDNumber,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(973, 596)
        MainWindow.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lcdNumber = QLCDNumber(self.frame_3)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.lcdNumber.setDigitCount(9)
        self.lcdNumber.setMode(QLCDNumber.Bin)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber.setProperty("intValue", 1)

        self.horizontalLayout.addWidget(self.lcdNumber)

        self.lcdNumber_2 = QLCDNumber(self.frame_3)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.lcdNumber_2.setDigitCount(8)
        self.lcdNumber_2.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout.addWidget(self.lcdNumber_2)

        self.lcdNumber_3 = QLCDNumber(self.frame_3)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        self.lcdNumber_3.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.lcdNumber_3.setDigitCount(8)
        self.lcdNumber_3.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout.addWidget(self.lcdNumber_3)

        self.h1status = QLabel(self.frame_3)
        self.h1status.setObjectName(u"h1status")
        font = QFont()
        font.setPointSize(16)
        self.h1status.setFont(font)
        self.h1status.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.h1status.setTextFormat(Qt.AutoText)
        self.h1status.setScaledContents(True)
        self.h1status.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.h1status)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lcdNumber_5 = QLCDNumber(self.frame_4)
        self.lcdNumber_5.setObjectName(u"lcdNumber_5")
        self.lcdNumber_5.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.lcdNumber_5.setDigitCount(9)
        self.lcdNumber_5.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_5.setProperty("intValue", 2)

        self.horizontalLayout_2.addWidget(self.lcdNumber_5)

        self.lcdNumber_6 = QLCDNumber(self.frame_4)
        self.lcdNumber_6.setObjectName(u"lcdNumber_6")
        self.lcdNumber_6.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.lcdNumber_6.setDigitCount(8)
        self.lcdNumber_6.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_2.addWidget(self.lcdNumber_6)

        self.lcdNumber_7 = QLCDNumber(self.frame_4)
        self.lcdNumber_7.setObjectName(u"lcdNumber_7")
        self.lcdNumber_7.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.lcdNumber_7.setDigitCount(8)
        self.lcdNumber_7.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_2.addWidget(self.lcdNumber_7)

        self.h2status = QLabel(self.frame_4)
        self.h2status.setObjectName(u"h2status")
        self.h2status.setFont(font)
        self.h2status.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.h2status)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"color:rgb(170, 0, 127);")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; text-decoration: underline; color:#aa0000;\">Realtime Garbage Monitor</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700; color:#aa007f;\">HOUSE ID</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; color:#aa007f;\">Garbage Weight(Kgs)</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; color:#aa007f;\">Garbage Volume(cm3)</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; color:#aa007f;\">Status</span></p></body></html>", None))
        self.h1status.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.h2status.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
    # retranslateUi

