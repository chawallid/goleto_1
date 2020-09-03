
from PyQt5.QtWidgets import QMainWindow,QScrollArea,QApplication, QWidget , QVBoxLayout, QPushButton, QGroupBox, QGridLayout
import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class  Ui_MainWindow(QMainWindow):
        def __init__(self, parent=None):
                QWidget.__init__(self, parent)
                self.setWindowTitle("Dashborad")

                self.setMinimumSize(480, 360) 
                self.showMaximized()
                
                font = QFont()
                font.setFamily("MS Shell Dlg 2")
                self.setFont(font)
                self.setStyleSheet("background-color: rgb(255, 251, 252);\n"
        "border:5px;\n"
        "")     
                self.centralwidget = QWidget(self)
                self.centralwidget.setGeometry(0, 0, 1280, 960)
                self.centralwidget.setObjectName("centralwidget")


                self.setCentralWidget(self.centralwidget)
                self.box = QVBoxLayout(self.centralwidget) 

                scroll = QScrollArea()
                content_widget = QWidget()
                scroll.setWidget(content_widget)
                scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
                scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
                scroll.setWidgetResizable(True) 

                lay = QVBoxLayout(content_widget)
                self.groupBox = QGroupBox()
                self.groupBox.setFont(QFont("Sanserif", 13))
                gridLayout = QGridLayout(self)

                self.frame = QtWidgets.QFrame(self.centralwidget)
                # self.frame.setGeometry(QtCore.QRect(0, 0, 1291, 321))
                self.frame.setAutoFillBackground(False)
                self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.539318, y1:0, x2:0.551273, y2:1, stop:0 rgba(56, 74, 173, 255), stop:0.607955 rgba(60, 203, 175, 255), stop:1 rgba(5, 199, 170, 255));")
                self.frame.setLocale(QtCore.QLocale(QtCore.QLocale.Thai, QtCore.QLocale.Thailand))
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setProperty("Color", QtGui.QColor(0, 0, 0))
                self.frame.setObjectName("frame")

                sub_gridLayout = QGridLayout(self.frame)

                self.dateNtime = QtWidgets.QLabel(self.frame)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(24)
                font.setBold(True)
                font.setWeight(75)
                self.dateNtime.setFont(font)
                self.dateNtime.setObjectName("dateNtime")
                self.dateNtime.setText("<font color=\"black\">DD MMM | HH : MM AM/PM</font>")
                self.dateNtime.setAlignment(QtCore.Qt.AlignCenter)

                self.result1 = QtWidgets.QLineEdit(self.frame)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(18)
                font.setBold(True)
                font.setWeight(75)
                self.result1.setFont(font)
                self.result1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border: 1px solid grey;\n"
        "border-radius: 20px;")
                self.result1.setAlignment(QtCore.Qt.AlignCenter)
                self.result1.setObjectName("result1")

                self.result2 = QtWidgets.QLineEdit(self.frame)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(18)
                font.setBold(True)
                font.setWeight(75)
                self.result2.setFont(font)
                self.result2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border: 1px solid grey;\n"
        "border-radius: 20px;")

                self.result2.setAlignment(QtCore.Qt.AlignCenter)
                self.result2.setObjectName("result2")

                self.result3 = QtWidgets.QLineEdit(self.frame)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(18)
                font.setBold(True)
                font.setWeight(75)
                self.result3.setFont(font)
                self.result3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border: 0px solid grey;\n"
        "border-radius: 20px;")
                self.result3.setAlignment(QtCore.Qt.AlignCenter)
                self.result3.setObjectName("result3")

                self.result4 = QtWidgets.QLineEdit(self.frame)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(18)
                font.setBold(True)
                font.setWeight(75)
                self.result4.setFont(font)
                self.result4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border: 1px solid grey;\n"
        "border-radius: 20px;")
                self.result4.setAlignment(QtCore.Qt.AlignCenter)
                self.result4.setObjectName("result4")

                self.result5 = QtWidgets.QLineEdit(self.frame)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(18)
                font.setBold(True)
                font.setWeight(75)
                self.result5.setFont(font)
                self.result5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border: 1px solid grey;\n"
        "border-radius: 20px;")
                self.result5.setAlignment(QtCore.Qt.AlignCenter)
                self.result5.setObjectName("result5")

                self.label_result1 = QtWidgets.QLineEdit(self.frame)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(16)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                self.label_result1.setFont(font)
                self.label_result1.setStyleSheet("font: 75 16pt \"Tahoma\";\n"
        "color: \"white\";\n"
        "background-color: rgba(255, 255, 255, 0);")
                self.label_result1.setObjectName("label_result1")

                self.label_result2 = QtWidgets.QLineEdit(self.frame)
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
                self.label_result2.setObjectName("label_result2")

                self.label_result3 = QtWidgets.QLineEdit(self.frame)
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
                # self.label_result3.setWordWrap(False)
                self.label_result3.setObjectName("label_result3")

                self.label_result4 = QtWidgets.QLineEdit(self.frame)
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
                # self.label_result4.setWordWrap(False)
                self.label_result4.setObjectName("label_result4")

                self.label_result5 = QtWidgets.QLineEdit(self.frame)
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
                self.label_result5.setObjectName("label_result5")

                self.result1.setFixedHeight(100)
                self.result2.setFixedHeight(100)
                self.result3.setFixedHeight(100)
                self.result4.setFixedHeight(100)
                self.result5.setFixedHeight(100)
                self.label_result1.setAlignment(QtCore.Qt.AlignCenter)
                self.label_result2.setAlignment(QtCore.Qt.AlignCenter)
                self.label_result3.setAlignment(QtCore.Qt.AlignCenter)
                self.label_result4.setAlignment(QtCore.Qt.AlignCenter)
                self.label_result5.setAlignment(QtCore.Qt.AlignCenter)

                sub_gridLayout.addWidget(self.dateNtime,0,0,1,6)
                sub_gridLayout.addWidget(self.result1,1,0,1,1)
                sub_gridLayout.addWidget(self.result2,1,1,1,1)
                sub_gridLayout.addWidget(self.result3,1,2,1,1)
                sub_gridLayout.addWidget(self.result4,1,3,1,1)
                sub_gridLayout.addWidget(self.result5,1,4,1,1)

                sub_gridLayout.addWidget(self.label_result1,2,0,1,1)
                sub_gridLayout.addWidget(self.label_result2,2,1,1,1)
                sub_gridLayout.addWidget(self.label_result3,2,2,1,1)
                sub_gridLayout.addWidget(self.label_result4,2,3,1,1)
                sub_gridLayout.addWidget(self.label_result5,2,4,1,1)
                
                gridLayout.addWidget(self.frame,0, 0, 1, 6)

                self.body = QtWidgets.QFrame(self.centralwidget)
                self.body.setLocale(QtCore.QLocale(QtCore.QLocale.Thai, QtCore.QLocale.Thailand))
                self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.body.setFrameShadow(QtWidgets.QFrame.Raised)
                self.body.setProperty("Color", QtGui.QColor(0, 0, 0))
                self.body.setObjectName("body")

                subBody_gridLayout = QGridLayout(self.body)

                self.tabWidget = QtWidgets.QTabWidget(self.body)
                self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "selection-color: rgb(211, 255, 229);\n"
        "font: 12pt \"Tahoma\";\n"
        "")
                self.tabWidget.setObjectName("tabWidget")
                self.figure = plt.figure(figsize=(4,2))
                self.canvas = FigureCanvas(self.figure)

                self.figure1 = plt.figure(figsize=(4,2))
                self.canvas1 = FigureCanvas(self.figure1)

                self.figure2 = plt.figure(figsize=(4,2))
                self.canvas2 = FigureCanvas(self.figure2)
                
                self.figure3 = plt.figure(figsize=(4,2))
                self.canvas3 = FigureCanvas(self.figure3)

                self.figure4 = plt.figure(figsize=(4,2))
                self.canvas4 = FigureCanvas(self.figure4)

                self.tabWidget.addTab(self.canvas, "")
                self.tabWidget.addTab(self.canvas1, "")
                self.tabWidget.addTab(self.canvas2, "")
                self.tabWidget.addTab(self.canvas3, "")
                self.tabWidget.addTab(self.canvas4, "")

                self.frame_2 = QtWidgets.QFrame(self.body)
                self.frame_2.setLocale(QtCore.QLocale(QtCore.QLocale.Thai, QtCore.QLocale.Thailand))
                self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_2.setProperty("Color", QtGui.QColor(0, 0, 0))
                self.frame_2.setObjectName("frame_2")

                subFrame2_gridLayout = QGridLayout(self.frame_2)
                self.buttonSysConfig = QtWidgets.QPushButton(self.frame_2)
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

                self.EXIT = QtWidgets.QPushButton(self.frame_2)
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

                self.START = QtWidgets.QPushButton(self.frame_2)
                self.START.setGeometry(QtCore.QRect(1100, 325, 140, 40))
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

                self.STOP = QtWidgets.QPushButton(self.frame_2)
                self.STOP.setGeometry(QtCore.QRect(1100, 370, 140, 40))
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(18)
                font.setBold(True)
                font.setWeight(75)
                self.STOP.setFont(font)
                self.STOP.setStyleSheet("border: 0px solid red;\n"
        "border-radius: 20px;\n"
        "background-color: rgb(255,0,0);")
                self.STOP.setObjectName("STOP")

                self.START.setFixedHeight(75)
                self.STOP.setFixedHeight(75)
                self.buttonSysConfig.setFixedHeight(75)
                self.buttonPrePro.setFixedHeight(75)
                self.EXIT.setFixedHeight(50)
                # self.START.setFixedWidth(100)
                # self.STOP.setFixedWidth(100)
                # self.buttonSysConfig.setFixedWidth(100)
                # self.buttonPrePro.setFixedWidth(100)
                # self.EXIT.setFixedWidth(100)
                subFrame2_gridLayout.addWidget(self.START,0,0)
                subFrame2_gridLayout.addWidget(self.STOP,1,0)
                subFrame2_gridLayout.addWidget(QtWidgets.QLabel(""),2,0)
                subFrame2_gridLayout.addWidget(self.buttonSysConfig,3,0)
                subFrame2_gridLayout.addWidget(self.buttonPrePro,4,0)
                subFrame2_gridLayout.addWidget(self.EXIT,5,0)

                self.frame_2.setFixedWidth(200)
                subBody_gridLayout.addWidget(self.tabWidget,0,0)
                subBody_gridLayout.addWidget(self.frame_2 ,0,1)
        

                gridLayout.addWidget(self.body,1, 0, 3, 6)

                self.groupBox.setLayout(gridLayout)
                lay.addWidget(self.groupBox)
                lay.addStretch()

                # scroll.setFixedHeight(960)
                # scroll.setFixedWidth(1280)
                self.box.addWidget(scroll)
                # self.retranslateUi(self)
                self.tabWidget.setCurrentIndex(0)
                self.EXIT.clicked.connect(self.close)
        
 
#     def setIcon(self):
#         appIcon = QIcon("icon.png")
#         MainWindow.setWindowIcon(appIcon)

        # def retranslateUi(self):
        #         _translate = QtCore.QCoreApplication.translate
                self.setWindowTitle("MainWindow")
                self.EXIT.setText( "EXIT")
                self.START.setText("START")
                self.STOP.setText("STOP")
                self.dateNtime.setText("<font color=\"black\">DD MMM | HH : MM AM/PM</font>")
                self.result1.setText("0")
                self.result2.setText("0")
                self.result4.setText("0")
                self.result5.setText("0")
                self.result3.setText("0")
                self.label_result1.setText("Result 1")
                self.label_result2.setText("Result 2")
                self.label_result3.setText("Result 3")
                self.label_result4.setText("Result 4")
                self.label_result5.setText("Result 5")
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.canvas),  "Curves 1")
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.canvas1),  "Curves 2")
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.canvas2),  "Curves 3")
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.canvas3),  "Curves 4")
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.canvas4),  "Curves 5")
                self.buttonSysConfig.setText( "System Config")
                self.buttonPrePro.setText( "Pre-Processing")

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     MainWindow = QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = Ui_MainWindow()
    myapp.show()
    sys.exit(app.exec_())