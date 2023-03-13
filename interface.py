# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 378)
        icon = QIcon()
        icon.addFile(u":/imgs/imgs/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#centralwidget{\n"
"	background-color : #2B3339;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color : #3A414A;\n"
"	border :none;\n"
"	height : 35px;\n"
"	color : #fff;\n"
"	border-radius : 5px;\n"
"	font-family : Montserrat;\n"
"}\n"
"\n"
"#btn_start{\n"
"	padding : 10px;\n"
"	background-color : #EA4D84;\n"
"	color : white;\n"
"	font-family : Montserrat;\n"
"	border : none;\n"
"	border-radius : 5px;\n"
"\n"
"}\n"
"\n"
"#btn_start:hover{\n"
"	background-color : #f25e92\n"
"}\n"
"#btn_start:pressed{\n"
"	background-color : #f578a4;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	color : white;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bgApp = QFrame(self.centralwidget)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.StyledPanel)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.bgApp)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.main_body = QFrame(self.bgApp)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setMinimumSize(QSize(0, 200))
        self.main_body.setMaximumSize(QSize(16777215, 200))
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.main_body)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.system_btn_frame = QFrame(self.main_body)
        self.system_btn_frame.setObjectName(u"system_btn_frame")
        self.system_btn_frame.setStyleSheet(u"QPushButton{\n"
"	border : none;\n"
"}")
        self.system_btn_frame.setFrameShape(QFrame.StyledPanel)
        self.system_btn_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.system_btn_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_4.addWidget(self.system_btn_frame, 0, Qt.AlignRight|Qt.AlignTop)

        self.le_main = QLineEdit(self.main_body)
        self.le_main.setObjectName(u"le_main")
        self.le_main.setMinimumSize(QSize(500, 0))
        self.le_main.setMaximumSize(QSize(500, 16777215))
        self.le_main.setMaxLength(100)
        self.le_main.setFrame(True)
        self.le_main.setCursorPosition(0)
        self.le_main.setAlignment(Qt.AlignCenter)
        self.le_main.setDragEnabled(True)
        self.le_main.setReadOnly(False)

        self.verticalLayout_4.addWidget(self.le_main, 0, Qt.AlignHCenter)

        self.margin = QFrame(self.main_body)
        self.margin.setObjectName(u"margin")
        self.margin.setFrameShape(QFrame.StyledPanel)
        self.margin.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.margin)

        self.btn_start = QPushButton(self.main_body)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setMinimumSize(QSize(200, 50))
        self.btn_start.setMaximumSize(QSize(200, 50))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(12)
        self.btn_start.setFont(font)

        self.verticalLayout_4.addWidget(self.btn_start, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.main_body)

        self.error_frame = QFrame(self.bgApp)
        self.error_frame.setObjectName(u"error_frame")
        self.error_frame.setMinimumSize(QSize(0, 0))
        self.error_frame.setFrameShape(QFrame.StyledPanel)
        self.error_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.error_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 9, 0, 0)
        self.success = QFrame(self.error_frame)
        self.success.setObjectName(u"success")
        self.success.setMinimumSize(QSize(0, 0))
        self.success.setMaximumSize(QSize(16777215, 0))
        self.success.setStyleSheet(u"background-color : #1fab36;\n"
"border-radius : 5px;")
        self.success.setFrameShape(QFrame.StyledPanel)
        self.success.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.success)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_success = QLabel(self.success)
        self.lbl_success.setObjectName(u"lbl_success")
        self.lbl_success.setStyleSheet(u"font-family : Montserrat;\n"
"font-size : 16px;")
        self.lbl_success.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lbl_success)


        self.verticalLayout_3.addWidget(self.success)

        self.error = QFrame(self.error_frame)
        self.error.setObjectName(u"error")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error.sizePolicy().hasHeightForWidth())
        self.error.setSizePolicy(sizePolicy)
        self.error.setMaximumSize(QSize(16777215, 0))
        self.error.setStyleSheet(u"background-color : #c40c4d;\n"
"border-radius : 5px;")
        self.error.setFrameShape(QFrame.StyledPanel)
        self.error.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.error)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_error = QLabel(self.error)
        self.lbl_error.setObjectName(u"lbl_error")
        self.lbl_error.setStyleSheet(u"font-family : Montserrat;\n"
"font-size : 16px;")
        self.lbl_error.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lbl_error)


        self.verticalLayout_3.addWidget(self.error)


        self.verticalLayout_2.addWidget(self.error_frame, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"XConverter", None))
        self.le_main.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u043b\u0438\u043d\u044b", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.lbl_success.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u0430, \u043c\u043e\u0436\u043d\u043e \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a!", None))
        self.lbl_error.setText(QCoreApplication.translate("MainWindow", u"Жаль, но из этого треугольник не сделать", None))
    # retranslateUi

