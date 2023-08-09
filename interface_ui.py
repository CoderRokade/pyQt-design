# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(848, 753)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainmenu = QFrame(self.centralwidget)
        self.mainmenu.setObjectName(u"mainmenu")
        self.mainmenu.setMaximumSize(QSize(1200, 16777215))
        self.mainmenu.setFrameShape(QFrame.StyledPanel)
        self.mainmenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainmenu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.navbar2 = QFrame(self.mainmenu)
        self.navbar2.setObjectName(u"navbar2")
        self.navbar2.setMaximumSize(QSize(16777215, 16777215))
        self.navbar2.setFrameShape(QFrame.StyledPanel)
        self.navbar2.setFrameShadow(QFrame.Raised)
        self.navbar = QFrame(self.navbar2)
        self.navbar.setObjectName(u"navbar")
        self.navbar.setGeometry(QRect(-20, -20, 1900, 100))
        self.navbar.setMaximumSize(QSize(16777215, 100))
        self.navbar.setFrameShape(QFrame.StyledPanel)
        self.navbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.navbar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.navbar)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 70))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-10, 0, 311, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gamenamehere = QFrame(self.frame_2)
        self.gamenamehere.setObjectName(u"gamenamehere")
        self.gamenamehere.setGeometry(QRect(20, -10, 224, 60))
        self.gamenamehere.setFrameShape(QFrame.StyledPanel)
        self.gamenamehere.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.gamenamehere)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 0, 167, 50))
        self.frame_3.setMaximumSize(QSize(300, 50))
        self.frame_3.setBaseSize(QSize(10, 20))
        self.frame_3.setCursor(QCursor(Qt.OpenHandCursor))
        self.frame_3.setAcceptDrops(False)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 10, 171, 41))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:  rgb(255, 31, 2);\n"
"\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(600, 0, 257, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(5)
        self.frame_4.setMidLineWidth(2)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color:rgb(125, 255, 229);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(40, 20))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(u"background-color:rgb(125, 255, 229);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"background-color:rgb(125, 255, 229);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_5 = QFrame(self.navbar2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 50, 831, 121))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 10, 91, 31))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 0, 75, 23))
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(180, 0, 91, 41))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.pushButton_6 = QPushButton(self.frame_7)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(10, 10, 75, 23))
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(100, 10, 91, 31))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.pushButton_5 = QPushButton(self.frame_8)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 0, 75, 23))
        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(240, 0, 121, 41))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.pushButton_7 = QPushButton(self.frame_9)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(30, 10, 75, 23))
        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(340, 10, 91, 31))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.pushButton_8 = QPushButton(self.frame_10)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(10, 0, 75, 23))
        self.frame_13 = QFrame(self.frame_5)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(580, 10, 91, 31))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.pushButton_11 = QPushButton(self.frame_13)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(10, 0, 75, 23))

        self.verticalLayout_2.addWidget(self.navbar2)

        self.herobox = QFrame(self.mainmenu)
        self.herobox.setObjectName(u"herobox")
        self.herobox.setFrameShape(QFrame.StyledPanel)
        self.herobox.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.herobox)


        self.verticalLayout.addWidget(self.mainmenu)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"GAME NAME", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"DIFFICULTY", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PATIENT", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"EXCERCISE", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"GAME", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"ANALYSIS", None))
    # retranslateUi

