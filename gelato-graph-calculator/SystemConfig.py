# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SystemConfig.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import Qt, QSize

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.scroll = QScrollArea()            
         

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1800, 1200)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 251, 252);\n"
"border:5px;\n"
"")
        # self.widget = QWidget(MainWindow) 
        # self.widget.setLayout(MainWindow)

        # self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.scroll.setWidgetResizable(True)
        # self.scroll.setWidget(MainWindow)
       
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 1800, 1200))
        # self.centralwidget.setWidgetResizable(True)
        self.centralwidget.setObjectName("centralwidget")

        

        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(10, 20, 111, 61))
        # self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")

        self.btnApply = QtWidgets.QPushButton(self.centralwidget)
        self.btnApply.setGeometry(QtCore.QRect(10, 60, 120, 80))
        # self.btnBack.setFont(font)
        self.btnApply.setObjectName("btnApply")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1000, 1000, 350, 100))
        self.pushButton_4.setStyleSheet("border-radius:50px;\n"
"background-color:rgb(0, 170, 0);\n"
"font-size:32px;\n"
"color:#fff;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 1000, 350, 100))
        self.pushButton_3.setStyleSheet("border-radius:50px;\n"
"background-color:#aa0000;\n"
"font-size:32px;\n"
"color:#fff;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(120, 50, 900, 900))
        self.groupBox.setStyleSheet("border-radius: 5px;\n"
"background-color:#rgb(158,158,158);\n"
"border: 2px solid black")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_Cal = QtWidgets.QLabel(self.groupBox)
        self.groupBox_Cal.setGeometry(QtCore.QRect(80, 30, 320, 45)) #Topic_Cal
        self.groupBox_Cal.setStyleSheet("color:black;\n"
                                    "border: none;\n" "font-size:14pt bold;\n")
        self.widget_4 = QtWidgets.QWidget(self.groupBox)
        self.widget_4.setGeometry(QtCore.QRect(80, 100, 750, 120)) #result1W
        self.widget_4.setStyleSheet("background-color:rgb(158, 158, 158);\n"
"border: none")
        self.widget_4.setObjectName("widget_4")

        self.label_5 = QtWidgets.QLabel(self.widget_4)
        self.label_5.setGeometry(QtCore.QRect(350, 5, 120, 25)) #result1L
        self.label_5.setStyleSheet("align:\"center\";\n" "font-size:10pt;\n" "color:#fff")
        self.label_5.setObjectName("label_5")

        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setGeometry(QtCore.QRect(30, 60, 300, 50)) #caliW1
        self.widget_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.widget_5.setObjectName("widget_5")
        
        self.label_1_ = QtWidgets.QLabel(self.widget_4)
        self.label_1_.setGeometry(QtCore.QRect(30, 60, 300, 50)) #browse file1
        self.label_1_.setStyleSheet("background-color: rgb(255, 255, 255);\n""align:\"center\";\n" "font-size:10pt;\n" "color:#000;")
        self.label_1_.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1_.setObjectName("label_1_")

        self.btn1 = QtWidgets.QPushButton(self.widget_4)
        self.btn1.setGeometry(QtCore.QRect(35+230, 70, 45+10, 35))
        self.btn1.setObjectName("btn1")


        self.widget_12 = QtWidgets.QWidget(self.widget_4)
        self.widget_12.setGeometry(QtCore.QRect(340, 60, 100, 50)) #biasW1
        self.widget_12.setStyleSheet("border-radius: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.widget_12.setObjectName("widget_12")
        
        self.spinBox_4 = QtWidgets.QSpinBox(self.widget_12)
        self.spinBox_4.setGeometry(QtCore.QRect(40, 20, 31, 22)) #biasL1
        self.spinBox_4.setObjectName("spinBox_4")
        self.widget_13 = QtWidgets.QWidget(self.widget_4)
        self.widget_13.setGeometry(QtCore.QRect(450, 60, 270, 50)) #selectW1
        self.widget_13.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.widget_13.setObjectName("widget_13")
        self.comboBox = QtWidgets.QComboBox(self.widget_13)
        self.comboBox.setGeometry(QtCore.QRect(40, 10, 200, 30)) #selectL1
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.widget_14 = QtWidgets.QWidget(self.widget_4)
        self.widget_14.setGeometry(QtCore.QRect(30, 35, 300, 30)) #caliHeadW1
        self.widget_14.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"border-radius:15px 50px 30px 5px;\n"
"")
        self.widget_14.setObjectName("widget_14")

        self.label_11 = QtWidgets.QLabel(self.widget_14)
        self.label_11.setGeometry(QtCore.QRect(10, 5, 300, 20)) #caliHeadL1
        self.label_11.setStyleSheet("align:\"center\";\n"
"font-size:8pt;")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")


        self.widget_15 = QtWidgets.QWidget(self.widget_4)
        self.widget_15.setGeometry(QtCore.QRect(340, 35, 100, 30)) #biasHeadW1
        self.widget_15.setStyleSheet("background-color: rgb(236, 236,236);\n"
"border-radius:15px 50px 30px 5px;")
        self.widget_15.setObjectName("widget_15")
        self.label_15 = QtWidgets.QLabel(self.widget_15)
        self.label_15.setGeometry(QtCore.QRect(3, 5, 100, 20)) #biasHeadL1
        self.label_15.setStyleSheet("align:\"center\";\n"
"font-size:8pt;")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.widget_16 = QtWidgets.QWidget(self.widget_4)
        self.widget_16.setGeometry(QtCore.QRect(450, 35, 270, 30)) #selectHeadW1
        self.widget_16.setStyleSheet("background-color: rgb(236, 236,236);\n"
"border-radius:15px 50px 30px 5px;")
        self.widget_16.setObjectName("widget_16")
        self.widget_7 = QtWidgets.QWidget(self.groupBox)
        self.widget_7.setGeometry(QtCore.QRect(80, 250, 750, 120)) #result2W
        self.widget_7.setStyleSheet("background-color:rgb(158, 158, 158);\n"
"border: none")
        self.widget_7.setObjectName("widget_7")
        self.label_6 = QtWidgets.QLabel(self.widget_7)
        self.label_6.setGeometry(QtCore.QRect(350, 5, 120, 25)) #result2L
        self.label_6.setStyleSheet("align:\"center\";\n" "font-size:10pt;\n" "color:#fff")
        self.label_6.setObjectName("label_6")
        self.widget_8 = QtWidgets.QWidget(self.widget_7)
        self.widget_8.setGeometry(QtCore.QRect(30, 60, 300, 50)) #caliW2
        self.widget_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.widget_8.setObjectName("widget_8")
        self.widget_17 = QtWidgets.QWidget(self.widget_7)
        self.widget_17.setGeometry(QtCore.QRect(340, 60, 100, 50)) #biasW2
        self.widget_17.setStyleSheet("border-radius: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.widget_17.setObjectName("widget_17")
        self.spinBox_5 = QtWidgets.QSpinBox(self.widget_17)
        self.spinBox_5.setGeometry(QtCore.QRect(40, 20, 31, 22)) #biasL2
        self.spinBox_5.setObjectName("spinBox_5")
        self.widget_18 = QtWidgets.QWidget(self.widget_7)
        self.widget_18.setGeometry(QtCore.QRect(450, 60, 270, 50)) #selectW2
        self.widget_18.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.widget_18.setObjectName("widget_18")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_18)
        self.comboBox_2.setGeometry(QtCore.QRect(40, 10, 200, 30)) #selectL2
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.widget_19 = QtWidgets.QWidget(self.widget_7)
        self.widget_19.setGeometry(QtCore.QRect(30, 35, 300, 30)) #caliHeadW2
        self.widget_19.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"border-radius:15px 50px 30px 5px;\n"
"")
        self.widget_19.setObjectName("widget_19")
        self.label_17 = QtWidgets.QLabel(self.widget_19)
        self.label_17.setGeometry(QtCore.QRect(10, 5, 300, 20)) #caliHeadL2
        self.label_17.setStyleSheet("align:\"center\";\n"
"font-size:8pt;")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.widget_20 = QtWidgets.QWidget(self.widget_7)
        self.widget_20.setGeometry(QtCore.QRect(340, 35, 100, 30)) #biasHeadW2
        self.widget_20.setStyleSheet("background-color: rgb(236, 236,236);\n"
"border-radius:15px 50px 30px 5px;")
        self.widget_20.setObjectName("widget_20")
        self.label_18 = QtWidgets.QLabel(self.widget_20)
        self.label_18.setGeometry(QtCore.QRect(3, 5, 100, 20)) #biasHeadL2
        self.label_18.setStyleSheet("align:\"center\";\n"
"font-size:8pt;")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.widget_21 = QtWidgets.QWidget(self.widget_7)
        self.widget_21.setGeometry(QtCore.QRect(450, 35, 270, 30)) #selectHeadW2
        self.widget_21.setStyleSheet("background-color: rgb(236, 236,236);\n"
"border-radius:15px 50px 30px 5px;")
        self.widget_21.setObjectName("widget_21")
        self.widget_9 = QtWidgets.QWidget(self.groupBox)
        self.widget_9.setGeometry(QtCore.QRect(80, 400, 750, 120)) #result3W
        self.widget_9.setStyleSheet("background-color:rgb(158, 158, 158);\n"
"border:none")
        self.widget_9.setObjectName("widget_9")
        self.label_7 = QtWidgets.QLabel(self.widget_9)
        self.label_7.setGeometry(QtCore.QRect(350, 5, 120, 25))  #result3L
        self.label_7.setStyleSheet("align:\"center\";\n" "font-size:10pt;\n" "color:#fff")
        self.label_7.setObjectName("label_7")
        self.widget_22 = QtWidgets.QWidget(self.widget_9)
        self.widget_22.setGeometry(QtCore.QRect(30, 60, 300, 50)) #caliW3
        self.widget_22.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.widget_22.setObjectName("widget_22")
        self.widget_23 = QtWidgets.QWidget(self.widget_9)
        self.widget_23.setGeometry(QtCore.QRect(340, 60, 100, 50)) #biasW3
        self.widget_23.setStyleSheet("border-radius: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.widget_23.setObjectName("widget_23")
        self.spinBox_6 = QtWidgets.QSpinBox(self.widget_23)
        self.spinBox_6.setGeometry(QtCore.QRect(40, 20, 31, 22)) #biasL3
        self.spinBox_6.setObjectName("spinBox_6")
        self.widget_24 = QtWidgets.QWidget(self.widget_9)
        self.widget_24.setGeometry(QtCore.QRect(450, 60, 270, 50)) #selectW3
        self.widget_24.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.widget_24.setObjectName("widget_24")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_24)
        self.comboBox_3.setGeometry(QtCore.QRect(40, 10, 200, 30)) #selectL3
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.widget_25 = QtWidgets.QWidget(self.widget_9)
        self.widget_25.setGeometry(QtCore.QRect(30, 35, 300, 30)) #caliHeadW3
        self.widget_25.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"border-radius:15px 50px 30px 5px;\n"
"")
        self.widget_25.setObjectName("widget_25")
        self.label_19 = QtWidgets.QLabel(self.widget_25)
        self.label_19.setGeometry(QtCore.QRect(10, 5, 300, 20)) #caliHeadL3
        self.label_19.setStyleSheet("align:\"center\";\n"
"font-size:8pt;")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.widget_26 = QtWidgets.QWidget(self.widget_9)
        self.widget_26.setGeometry(QtCore.QRect(340, 35, 100, 30)) #biasHeadW3
        self.widget_26.setStyleSheet("background-color: rgb(236, 236,236);\n"
"border-radius:15px 50px 30px 5px;")
        self.widget_26.setObjectName("widget_26")
        self.label_20 = QtWidgets.QLabel(self.widget_26)
        self.label_20.setGeometry(QtCore.QRect(3, 5, 100, 20)) #biasHeadL3
        self.label_20.setStyleSheet("align:\"center\";\n"
"font-size:8pt;")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.widget_27 = QtWidgets.QWidget(self.widget_9)
        self.widget_27.setGeometry(QtCore.QRect(450, 35, 270, 30)) #selectHeadW3
        self.widget_27.setStyleSheet("background-color: rgb(236, 236,236);\n"
"border-radius:15px 50px 30px 5px;")
        self.widget_27.setObjectName("widget_27")
        self.widget_28 = QtWidgets.QWidget(self.groupBox)
        self.widget_28.setGeometry(QtCore.QRect(80, 550, 750, 120)) #result4W
        self.widget_28.setStyleSheet("background-color:rgb(158, 158, 158);\n"
"border:none")
        self.widget_28.setObjectName("widget_28")
        self.label_8 = QtWidgets.QLabel(self.widget_28)
        self.label_8.setGeometry(QtCore.QRect(350, 5, 120, 25))  #result4L
        self.label_8.setStyleSheet("align:\"center\";\n" "font-size:10pt;\n" "color:#fff")
        self.label_8.setObjectName("label_8")
        self.widget_29 = QtWidgets.QWidget(self.widget_28)
        self.widget_29.setGeometry(QtCore.QRect(30, 60, 300, 50)) #caliW4
        self.widget_29.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.widget_29.setObjectName("widget_29")
        self.widget_30 = QtWidgets.QWidget(self.widget_28)
        self.widget_30.setGeometry(QtCore.QRect(340, 60, 100, 50)) #biasW4
        self.widget_30.setStyleSheet("border-radius: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.widget_30.setObjectName("widget_30")
        self.spinBox_7 = QtWidgets.QSpinBox(self.widget_30)
        self.spinBox_7.setGeometry(QtCore.QRect(40, 20, 31, 22)) #biasL4
        self.spinBox_7.setObjectName("spinBox_7")
        self.widget_31 = QtWidgets.QWidget(self.widget_28)
        self.widget_31.setGeometry(QtCore.QRect(450, 60, 270, 50)) #selectW4
        self.widget_31.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.widget_31.setObjectName("widget_31")
        self.comboBox_4 = QtWidgets.QComboBox(self.widget_31)
        self.comboBox_4.setGeometry(QtCore.QRect(40, 10, 200, 30)) #selectL4
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.widget_32 = QtWidgets.QWidget(self.widget_28)
        self.widget_32.setGeometry(QtCore.QRect(30, 35, 300, 30)) #caliHeadW4
        self.widget_32.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"border-radius:15px 50px 30px 5px;\n"
"")
        self.widget_32.setObjectName("widget_32")
        self.label_21 = QtWidgets.QLabel(self.widget_32)
        self.label_21.setGeometry(QtCore.QRect(10, 5, 300, 20)) #caliHeadL4
        self.label_21.setStyleSheet("align:\"center\";\n"
"font-size:8pt;")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.widget_33 = QtWidgets.QWidget(self.widget_28)
        self.widget_33.setGeometry(QtCore.QRect(340, 35, 100, 30)) #biasHeadW4
        self.widget_33.setStyleSheet("background-color: rgb(236, 236,236);\n"
"border-radius:15px 50px 30px 5px;")
        self.widget_33.setObjectName("widget_33")
        self.label_22 = QtWidgets.QLabel(self.widget_33)
        self.label_22.setGeometry(QtCore.QRect(3, 5, 100, 20)) #biasHeadL4
        self.label_22.setStyleSheet("align:\"center\";\n"
"font-size:8pt;")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.widget_34 = QtWidgets.QWidget(self.widget_28)
        self.widget_34.setGeometry(QtCore.QRect(450, 35, 270, 30)) #selectHeadW4
        self.widget_34.setStyleSheet("background-color: rgb(236, 236,236);\n"
"border-radius:15px 50px 30px 5px;")
        self.widget_34.setObjectName("widget_34")
        self.widget_35 = QtWidgets.QWidget(self.groupBox)
        self.widget_35.setGeometry(QtCore.QRect(80, 700, 750, 120)) #result5W
        self.widget_35.setStyleSheet("background-color:rgb(158, 158, 158);\n"
"border:none")
        self.widget_35.setObjectName("widget_35")
        self.label_9 = QtWidgets.QLabel(self.widget_35)
        self.label_9.setGeometry(QtCore.QRect(350, 5, 120, 25))  #result5L
        self.label_9.setStyleSheet("align:\"center\";\n" "font-size:10pt;\n" "color:#fff")
        self.label_9.setObjectName("label_9")
        self.widget_36 = QtWidgets.QWidget(self.widget_35)
        self.widget_36.setGeometry(QtCore.QRect(30, 60, 300, 50)) #caliW5
        self.widget_36.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.widget_36.setObjectName("widget_36")
        self.widget_37 = QtWidgets.QWidget(self.widget_35)
        self.widget_37.setGeometry(QtCore.QRect(340, 60, 100, 50)) #biasW5
        self.widget_37.setStyleSheet("border-radius: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.widget_37.setObjectName("widget_37")
        self.spinBox_8 = QtWidgets.QSpinBox(self.widget_37)
        self.spinBox_8.setGeometry(QtCore.QRect(40, 20, 31, 22)) #biasL5
        self.spinBox_8.setObjectName("spinBox_8")
        self.widget_38 = QtWidgets.QWidget(self.widget_35)
        self.widget_38.setGeometry(QtCore.QRect(450, 60, 270, 50)) #selectW5
        self.widget_38.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.widget_38.setObjectName("widget_38")
        self.comboBox_5 = QtWidgets.QComboBox(self.widget_38)
        self.comboBox_5.setGeometry(QtCore.QRect(40, 10, 200, 30)) #selectL5
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.widget_39 = QtWidgets.QWidget(self.widget_35)
        self.widget_39.setGeometry(QtCore.QRect(30, 35, 300, 30)) #caliHeadW5
        self.widget_39.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"border-radius:15px 50px 30px 5px;\n"
"")
        self.widget_39.setObjectName("widget_39")
        self.label_23 = QtWidgets.QLabel(self.widget_39)
        self.label_23.setGeometry(QtCore.QRect(10, 5, 300, 20)) #caliHeadL5
        self.label_23.setStyleSheet("align:\"center\";\n"
"font-size:8pt;")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.widget_40 = QtWidgets.QWidget(self.widget_35)
        self.widget_40.setGeometry(QtCore.QRect(340, 35, 100, 30)) #biasHeadW5
        self.widget_40.setStyleSheet("background-color: rgb(236, 236,236);\n"
"border-radius:15px 50px 30px 5px;")
        self.widget_40.setObjectName("widget_40")
        self.label_24 = QtWidgets.QLabel(self.widget_40)
        self.label_24.setGeometry(QtCore.QRect(3, 5, 100, 20)) #biasHeadL5
        self.label_24.setStyleSheet("align:\"center\";\n"
"font-size:8pt;")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.widget_41 = QtWidgets.QWidget(self.widget_35)
        self.widget_41.setGeometry(QtCore.QRect(450, 35, 270, 30)) #selectHeadW5
        self.widget_41.setStyleSheet("background-color: rgb(236, 236,236);\n"
"border-radius:15px 50px 30px 5px;")
        self.widget_41.setObjectName("widget_41")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(1100, 300, 600, 270)) #GroupBox2W
        self.groupBox_2.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid black")
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_Spec = QtWidgets.QLabel(self.groupBox_2)
        self.groupBox_Spec.setGeometry(QtCore.QRect(30, 30, 400, 45))  # Topic_Spec
        self.groupBox_Spec.setStyleSheet("color:black;\n"
                                        "border: none;\n" "font-size:14pt bold;\n")
        self.widget_6 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_6.setGeometry(QtCore.QRect(30, 100, 540, 100)) #integrationW
        self.widget_6.setStyleSheet("\n"
"background-color: rgb(153, 153, 153);\n"
"border:none;\n")
        self.widget_6.setObjectName("widget_6")
        self.label_12 = QtWidgets.QLabel(self.widget_6)
        self.label_12.setGeometry(QtCore.QRect(50, 40, 300, 20)) #integrationL
        self.label_12.setStyleSheet("align:\"center\";\n" "font-size:10pt;\n" "color:#fff")
        self.label_12.setObjectName("label_12")
        self.spinBox = QtWidgets.QSpinBox(self.widget_6)
        self.spinBox.setGeometry(QtCore.QRect(310, 40, 40, 20)) #integrationBox
        self.spinBox.setStyleSheet("border-color:rgb(158, 158, 158);\n"
"background-color: rgb(236, 236, 236);\n"
"")
        self.spinBox.setObjectName("spinBox")
        self.label_16 = QtWidgets.QLabel(self.widget_6)
        self.label_16.setGeometry(QtCore.QRect(400, 40, 40, 20)) #integrationMs
        self.label_16.setStyleSheet("align:\"center\";\n" "font-size:10pt;\n" "color:#fff")
        self.label_16.setObjectName("label_16")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(1100, 650, 600, 300)) #GroupBox3W
        self.groupBox_3.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid black;\n")
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_wav = QtWidgets.QLabel(self.groupBox_3)
        self.groupBox_wav.setGeometry(QtCore.QRect(30, 30, 400, 45))  # Topic_Wavelength
        self.groupBox_wav.setStyleSheet("color:black;\n"
                                         "border: none;\n" "font-size:14pt bold;\n")
        self.widget_10 = QtWidgets.QWidget(self.groupBox_3)
        self.widget_10.setGeometry(QtCore.QRect(30, 100, 540, 80)) #M_wavelength_W
        self.widget_10.setStyleSheet("background-color: rgb(158, 158, 158) ;\n" "border:none")
        self.widget_10.setObjectName("widget_10")
        self.label_13 = QtWidgets.QLabel(self.widget_10)
        self.label_13.setGeometry(QtCore.QRect(150, 30, 40, 20)) #M_wavelength_L
        self.label_13.setStyleSheet("align:\"center\"")
        self.label_13.setObjectName("label_13")
        self.spinBox_3 = QtWidgets.QSpinBox(self.widget_10)
        self.spinBox_3.setGeometry(QtCore.QRect(310, 20, 80, 40)) #boxM_wavelength_W
        self.spinBox_3.setStyleSheet("border-color:rgb(158, 158, 158);\n"
"background-color: #fff;\n"
"font-size:14pt;\n")
        self.spinBox_3.setObjectName("spinBox_3")
        self.widget_11 = QtWidgets.QWidget(self.groupBox_3)
        self.widget_11.setGeometry(QtCore.QRect(30, 200, 540, 80)) #N_wavelength_W
        self.widget_11.setStyleSheet("background-color: rgb(158, 158, 158);\n" "border:none")
        self.widget_11.setObjectName("widget_11")
        self.label_14 = QtWidgets.QLabel(self.widget_11)
        self.label_14.setGeometry(QtCore.QRect(150, 30, 80, 30)) #N_wavelength_L
        self.label_14.setStyleSheet("align:\"center\";\n" "font-size:8pt;\n")
        self.label_14.setObjectName("label_14")
        self.spinBox_2 = QtWidgets.QSpinBox(self.widget_11)
        self.spinBox_2.setGeometry(QtCore.QRect(310, 20, 80, 40)) #boxN_wavelength_W
        self.spinBox_2.setStyleSheet("border-color:rgb(158, 158, 158);\n"
"background-color: #fff;\n"
"font-size:14pt;\n")
        self.spinBox_2.setObjectName("spinBox_2")

        # MainWindow.setCentralWidget(self.centralwidget)

        self.labelTime = QtWidgets.QLabel(self.centralwidget)
        self.labelTime.setGeometry(QtCore.QRect(1120, 130, 600, 50))
        self.labelTime.setObjectName("labelTime")
        self.labelTime.setStyleSheet("font-size:18pt")

       

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "System Configuration"))
        self.pushButton_4.setText(_translate("MainWindow", "APPLY"))
        self.pushButton_3.setText(_translate("MainWindow", "CANCEL"))
        #self.groupBox.setTitle(_translate("MainWindow", "Calculation Setting"))
        self.groupBox_Cal.setText(_translate("MainWindow", "Calculation Setting"))
        self.label_5.setText(_translate("MainWindow", "Result1"))
        self.comboBox.setItemText(0, _translate("MainWindow", "---select---"))
        self.comboBox.setItemText(1, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(2, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(3, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(4, _translate("MainWindow", "New Item"))
        self.label_11.setText(_translate("MainWindow", "Calibration file1"))
        self.label_15.setText(_translate("MainWindow", "Bias"))
        self.label_6.setText(_translate("MainWindow", "Result2"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "---select---"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "New Item"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "New Item"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "New Item"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "New Item"))
        self.label_17.setText(_translate("MainWindow", "Calibration file2"))
        self.label_18.setText(_translate("MainWindow", "Bias"))
        self.label_7.setText(_translate("MainWindow", "Result3"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "---select---"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "New Item"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "New Item"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "New Item"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "New Item"))
        self.label_19.setText(_translate("MainWindow", "Calibration file3"))
        self.label_20.setText(_translate("MainWindow", "Bias"))
        self.label_8.setText(_translate("MainWindow", "Result4"))
        self.label_1_.setText(_translate("MainWindow", "...."))

        self.comboBox_4.setItemText(0, _translate("MainWindow", "---select---"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "New Item"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "New Item"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "New Item"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "New Item"))
        self.label_21.setText(_translate("MainWindow", "Calibration file4"))
        self.label_22.setText(_translate("MainWindow", "Bias"))
        self.label_9.setText(_translate("MainWindow", "Result5"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "---select---"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "New Item"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "New Item"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "New Item"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "New Item"))
        self.label_23.setText(_translate("MainWindow", "Calibration file5"))
        self.label_24.setText(_translate("MainWindow", "Bias"))
        #self.groupBox_2.setTitle(_translate("MainWindow", "Spectrometer Setting"))
        self.groupBox_Spec.setText(_translate("MainWindow", "Spectrometer Setting"))
        self.label_12.setText(_translate("MainWindow", "Integration time"))
        self.label_16.setText(_translate("MainWindow", "ms"))
        #self.groupBox_3.setTitle(_translate("MainWindow", "Wave Length"))
        self.groupBox_wav.setText(_translate("MainWindow", "Wave Length"))
        self.label_13.setText(_translate("MainWindow", "N"))
        self.label_14.setText(_translate("MainWindow", "M"))
        self.btnBack.setText(_translate("MainWindow", "Back"))
        self.btn1.setText(_translate("MainWindow", "browse"))
        self.btnApply.setText(_translate("MainWindow", "Apply"))

#        self.labelTime.setText(_translate("MainWindow", x.strftime("%c")))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())