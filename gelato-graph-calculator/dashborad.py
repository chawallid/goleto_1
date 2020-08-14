# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import matplotlib.pyplot as plt


from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        # self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        # self.widget = QWidget()    
          
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.centralwidget.setObjectName("centralwidget")
        self.EXIT = QtWidgets.QPushButton(self.centralwidget)
        self.EXIT.setGeometry(QtCore.QRect(1090, 700, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.EXIT.setFont(font)
        self.EXIT.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.EXIT.setStyleSheet("border: 0px solid;\n"
"border-radius: 20px;\n"
"background-color: rgb(128, 11, 0);\n"
"color: \"white\";\n"
"font: 20pt \"Tahoma\";")
        self.EXIT.setAutoDefault(False)
        self.EXIT.setDefault(False)
        self.EXIT.setObjectName("EXIT")
        self.START = QtWidgets.QPushButton(self.centralwidget)
        self.START.setGeometry(QtCore.QRect(1090, 340, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.START.setFont(font)
        self.START.setStyleSheet("border: 0px solid grey;\n"
"border-radius: 20px;\n"
"background-color: rgb(106, 255, 106);")
        self.START.setObjectName("START")
        self.dateNtime = QtWidgets.QLabel(self.centralwidget)
        self.dateNtime.setGeometry(QtCore.QRect(430, 20, 448, 39))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dateNtime.setFont(font)
        self.dateNtime.setObjectName("dateNtime")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1291, 321))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.539318, y1:0, x2:0.551273, y2:1, stop:0 rgba(56, 74, 173, 255), stop:0.607955 rgba(60, 203, 175, 255), stop:1 rgba(5, 199, 170, 255));")
        self.frame.setLocale(QtCore.QLocale(QtCore.QLocale.Thai, QtCore.QLocale.Thailand))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setProperty("Color", QtGui.QColor(0, 0, 0))
        self.frame.setObjectName("frame")
        self.result1 = QtWidgets.QLabel(self.frame)
        self.result1.setGeometry(QtCore.QRect(20, 110, 211, 111))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.result1.setFont(font)
        self.result1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px solid grey;\n"
"border-radius: 20px;")
        self.result1.setAlignment(QtCore.Qt.AlignCenter)
        self.result1.setObjectName("result1")
        self.result2 = QtWidgets.QLabel(self.frame)
        self.result2.setGeometry(QtCore.QRect(270, 110, 211, 111))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.result2.setFont(font)
        self.result2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px solid grey;\n"
"border-radius: 20px;")
        self.result2.setAlignment(QtCore.Qt.AlignCenter)
        self.result2.setObjectName("result2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 79, 2, 2))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.result4 = QtWidgets.QLabel(self.frame)
        self.result4.setGeometry(QtCore.QRect(790, 110, 211, 111))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.result4.setFont(font)
        self.result4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px solid grey;\n"
"border-radius: 20px;")
        self.result4.setAlignment(QtCore.Qt.AlignCenter)
        self.result4.setObjectName("result4")
        self.result5 = QtWidgets.QLabel(self.frame)
        self.result5.setGeometry(QtCore.QRect(1050, 110, 211, 111))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.result5.setFont(font)
        self.result5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px solid grey;\n"
"border-radius: 20px;")
        self.result5.setAlignment(QtCore.Qt.AlignCenter)
        self.result5.setObjectName("result5")
        self.result3 = QtWidgets.QLabel(self.frame)
        self.result3.setGeometry(QtCore.QRect(530, 110, 211, 111))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.result3.setFont(font)
        self.result3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px solid grey;\n"
"border-radius: 20px;")
        self.result3.setAlignment(QtCore.Qt.AlignCenter)
        self.result3.setObjectName("result3")
        self.label_result1 = QtWidgets.QLabel(self.frame)
        self.label_result1.setGeometry(QtCore.QRect(30, 230, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_result1.setFont(font)
        self.label_result1.setAutoFillBackground(False)
        self.label_result1.setStyleSheet("font: 75 16pt \"Tahoma\";\n"
"color: \"white\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_result1.setWordWrap(False)
        self.label_result1.setObjectName("label_result1")
        self.label_result2 = QtWidgets.QLabel(self.frame)
        self.label_result2.setGeometry(QtCore.QRect(280, 230, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_result2.setFont(font)
        self.label_result2.setAutoFillBackground(False)
        self.label_result2.setStyleSheet("font: 75 16pt \"Tahoma\";\n"
"color: \"white\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_result2.setWordWrap(False)
        self.label_result2.setObjectName("label_result2")
        self.label_result3 = QtWidgets.QLabel(self.frame)
        self.label_result3.setGeometry(QtCore.QRect(540, 230, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_result3.setFont(font)
        self.label_result3.setAutoFillBackground(False)
        self.label_result3.setStyleSheet("font: 75 16pt \"Tahoma\";\n"
"color: \"white\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_result3.setWordWrap(False)
        self.label_result3.setObjectName("label_result3")
        self.label_result4 = QtWidgets.QLabel(self.frame)
        self.label_result4.setGeometry(QtCore.QRect(800, 230, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_result4.setFont(font)
        self.label_result4.setAutoFillBackground(False)
        self.label_result4.setStyleSheet("font: 75 16pt \"Tahoma\";\n"
"color: \"white\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_result4.setWordWrap(False)
        self.label_result4.setObjectName("label_result4")
        self.label_result5 = QtWidgets.QLabel(self.frame)
        self.label_result5.setGeometry(QtCore.QRect(1060, 230, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_result5.setFont(font)
        self.label_result5.setAutoFillBackground(False)
        self.label_result5.setStyleSheet("font: 75 16pt \"Tahoma\";\n"
"color: \"white\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_result5.setWordWrap(False)
        self.label_result5.setObjectName("label_result5")
        self.label_result1_2 = QtWidgets.QLabel(self.frame)
        self.label_result1_2.setGeometry(QtCore.QRect(200, 230, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_result1_2.setFont(font)
        self.label_result1_2.setAutoFillBackground(False)
        self.label_result1_2.setStyleSheet("\n"
"color: \"white\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_result1_2.setWordWrap(False)
        self.label_result1_2.setObjectName("label_result1_2")
        self.label_result1_3 = QtWidgets.QLabel(self.frame)
        self.label_result1_3.setGeometry(QtCore.QRect(450, 230, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_result1_3.setFont(font)
        self.label_result1_3.setAutoFillBackground(False)
        self.label_result1_3.setStyleSheet("\n"
"color: \"white\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_result1_3.setWordWrap(False)
        self.label_result1_3.setObjectName("label_result1_3")
        self.label_result1_4 = QtWidgets.QLabel(self.frame)
        self.label_result1_4.setGeometry(QtCore.QRect(710, 230, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_result1_4.setFont(font)
        self.label_result1_4.setAutoFillBackground(False)
        self.label_result1_4.setStyleSheet("\n"
"color: \"white\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_result1_4.setWordWrap(False)
        self.label_result1_4.setObjectName("label_result1_4")
        self.label_result1_5 = QtWidgets.QLabel(self.frame)
        self.label_result1_5.setGeometry(QtCore.QRect(970, 230, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_result1_5.setFont(font)
        self.label_result1_5.setAutoFillBackground(False)
        self.label_result1_5.setStyleSheet("\n"
"color: \"white\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_result1_5.setWordWrap(False)
        self.label_result1_5.setObjectName("label_result1_5")
        self.label_result1_6 = QtWidgets.QLabel(self.frame)
        self.label_result1_6.setGeometry(QtCore.QRect(1230, 230, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_result1_6.setFont(font)
        self.label_result1_6.setAutoFillBackground(False)
        self.label_result1_6.setStyleSheet("\n"
"color: \"white\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_result1_6.setWordWrap(False)
        self.label_result1_6.setObjectName("label_result1_6")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 350, 991, 391))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(211, 255, 229);\n"
"font: 12pt \"Tahoma\";\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        # self.toolbar = NavigationToolbar(self.canvas, self)


        # self.curves1 = QtWidgets.QWidget()
        # self.curves1.setObjectName("curves1")
        self.tabWidget.addTab(self.canvas, "")
        self.curves2 = QtWidgets.QWidget()
        self.curves2.setObjectName("curves2")
        self.tabWidget.addTab(self.curves2, "")
        self.curves3 = QtWidgets.QWidget()
        self.curves3.setObjectName("curves3")
        self.tabWidget.addTab(self.curves3, "")
        self.curves4 = QtWidgets.QWidget()
        self.curves4.setObjectName("curves4")
        self.tabWidget.addTab(self.curves4, "")
        self.curves5 = QtWidgets.QWidget()
        self.curves5.setObjectName("curves5")
        self.tabWidget.addTab(self.curves5, "")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1291, 751))
        self.frame_2.setStyleSheet("background-color: rgb(211, 255, 229);")
        self.frame_2.setLocale(QtCore.QLocale(QtCore.QLocale.Thai, QtCore.QLocale.Thailand))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setProperty("Color", QtGui.QColor(0, 0, 0))
        self.frame_2.setObjectName("frame_2")
        self.buttonSysConfig = QtWidgets.QPushButton(self.frame_2)
        self.buttonSysConfig.setGeometry(QtCore.QRect(1090, 640, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.buttonSysConfig.setFont(font)
        self.buttonSysConfig.setStyleSheet("border: 0px solid;\n"
"border-radius: 20px;\n"
"background-color: rgb(0, 97, 114);\n"
"color: \"white\";\n"
"font: 14pt \"Tahoma\";")
        self.buttonSysConfig.setObjectName("buttonSysConfig")
        
        self.buttonPrePro = QtWidgets.QPushButton(self.frame_2)
        self.buttonPrePro.setGeometry(QtCore.QRect(1090, 590, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.buttonPrePro.setFont(font)
        self.buttonPrePro.setStyleSheet("border: 0px solid;\n"
"border-radius: 20px;\n"
"background-color: rgb(7, 61, 134);\n"
"color: \"white\";\n"
"font: 14pt \"Tahoma\";")
        self.buttonPrePro.setObjectName("buttonPrePro")
        self.widget_status = QtWidgets.QWidget(self.frame_2)
        self.widget_status.setGeometry(QtCore.QRect(1100, 410, 141, 161))
        self.widget_status.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-raduis: 20px;")
        self.widget_status.setObjectName("widget_status")
        self.frame_2.raise_()
        self.frame.raise_()
        self.EXIT.raise_()
        self.START.raise_()
        self.dateNtime.raise_()
        self.tabWidget.raise_()
        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuHel = QtWidgets.QMenu(self.menubar)
        self.menuHel.setObjectName("menuHel")
        self.menuHelp_2 = QtWidgets.QMenu(self.menubar)
        self.menuHelp_2.setObjectName("menuHelp_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_Files = QtWidgets.QAction(MainWindow)
        self.actionSave_Files.setObjectName("actionSave_Files")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setObjectName("actionStop")
        self.menuFile.addAction(self.actionSave_Files)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionStart)
        self.menuEdit.addAction(self.actionStop)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuHel.menuAction())
        self.menubar.addAction(self.menuHelp_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.EXIT.clicked.connect(MainWindow.close)
        self.START.clicked.connect(self.result5.update)
        self.START.clicked.connect(self.result4.update)
        self.START.clicked.connect(self.result3.update)
        self.START.clicked.connect(self.result2.update)
        self.START.clicked.connect(self.result1.update)

        self.label_result1_2.objectNameChanged['QString'].connect(self.label_result1.setText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.EXIT.setText(_translate("MainWindow", "EXIT"))
        self.START.setText(_translate("MainWindow", "START"))
        self.dateNtime.setText(_translate("MainWindow", "<font color=\"white\">DD MMM | HH : MM AM/PM</font>"))
        self.result1.setText(_translate("MainWindow", "0"))
        self.result2.setText(_translate("MainWindow", "0"))
        self.result4.setText(_translate("MainWindow", "0"))
        self.result5.setText(_translate("MainWindow", "0"))
        self.result3.setText(_translate("MainWindow", "0"))
        self.label_result1.setText(_translate("MainWindow", "Result 1"))
        self.label_result2.setText(_translate("MainWindow", "Result 2"))
        self.label_result3.setText(_translate("MainWindow", "Result 3"))
        self.label_result4.setText(_translate("MainWindow", "Result 4"))
        self.label_result5.setText(_translate("MainWindow", "Result 5"))
        self.label_result1_2.setText(_translate("MainWindow", "Edit"))
        self.label_result1_3.setText(_translate("MainWindow", "Edit"))
        self.label_result1_4.setText(_translate("MainWindow", "Edit"))
        self.label_result1_5.setText(_translate("MainWindow", "Edit"))
        self.label_result1_6.setText(_translate("MainWindow", "Edit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.canvas), _translate("MainWindow", "Curves 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.curves2), _translate("MainWindow", "Curves 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.curves3), _translate("MainWindow", "Curves 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.curves4), _translate("MainWindow", "Curves 4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.curves5), _translate("MainWindow", "Curves 5"))
        self.buttonSysConfig.setText(_translate("MainWindow", "System Config"))
        self.buttonPrePro.setText(_translate("MainWindow", "Pre-Processing"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Setting"))
        self.menuHel.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp_2.setTitle(_translate("MainWindow", "Help"))
        self.actionSave_Files.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionStart.setText(_translate("MainWindow", "Start"))
        self.actionStop.setText(_translate("MainWindow", "Stop"))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

