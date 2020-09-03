
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
                self.setWindowTitle("SystemConfig")
                self.setMinimumSize(480, 360) 
                self.showMaximized()
                font = QFont()
                font.setFamily("MS Shell Dlg 2")
                self.setFont(font)
                self.centralwidget = QWidget(self)
                self.centralwidget.setGeometry(0, 0, 1280, 960)
                self.centralwidget.setObjectName("centralwidge t")
        #         self.centralwidget.setStyleSheet("border-radius:0px;\n"
        # "background-color:rgb(255, 0, 0);\n"
        # "font-size:32px;\n"
        # "color:#fff;")


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

                self.body = QtWidgets.QFrame(self.centralwidget)
                self.body.setLocale(QtCore.QLocale(QtCore.QLocale.Thai, QtCore.QLocale.Thailand))
                self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.body.setFrameShadow(QtWidgets.QFrame.Raised)
                self.body.setProperty("Color", QtGui.QColor(0, 0, 0))
                self.body.setObjectName("body")

                subBody_gridLayout = QGridLayout(self.body)
                self.groupBox_cal = QtWidgets.QGroupBox(self.body)
                self.groupBox_cal.setStyleSheet("border-radius: 5px;\n"
        "background-color:#rgb(158,158,158);\n"
        "border: 2px solid black")
                self.groupBox_cal.setObjectName("groupBox")

                sub_groupbox_cal = QGridLayout(self.groupBox_cal)

                self.Label = QtWidgets.QLabel()#Topic_Cal
                self.Label.setAutoFillBackground(False)
                self.Label.setStyleSheet("border-radius: 0px;\n"
        "border: 0px solid black;\n font-size:14pt bold;\n background-color: transparent;");
                self.Label.setAlignment(QtCore.Qt.AlignCenter)

                self.widget_4 = QtWidgets.QWidget(self.groupBox_cal) #result1W
                self.widget_4.setStyleSheet("background-color:rgb(158, 158, 158);\n"
        "border: none")
                self.widget_4.setObjectName("widget_4")
                
                sub_GridCal_1 = QGridLayout(self.widget_4)

                self.label_5 = QtWidgets.QLabel(self.widget_4)#result1L
                self.label_5.setStyleSheet("align:\"center\";\n" "font-size:10pt;\n" "color:#fff")
                self.label_5.setObjectName("label_5")
                self.label_5.setText("Result1")
                sub_GridCal_1.addWidget( self.label_5,0,0)

                self.widget_5 = QtWidgets.QWidget(self.widget_4)#caliW1
                self.widget_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-radius: 0px;")
                self.widget_5.setObjectName("widget_5")
                sub_GridCal_1.addWidget(self.widget_5,2,0,1,3)

                sub_GridCal_1_1 = QGridLayout(self.widget_5)
                self.label_1_ = QtWidgets.QLabel(self.widget_5)#browse file1
                self.label_1_.setStyleSheet("background-color: rgb(255, 255, 255);\n""align:\"center\";\n" "font-size:5pt;\n" "color:#000;")
                self.label_1_.setAlignment(QtCore.Qt.AlignCenter)
                self.label_1_.setObjectName("label_1_")
                self.label_1_.setText("555")
                sub_GridCal_1_1.addWidget(self.label_1_,0,0,1,3)

                self.label_11 = QtWidgets.QLabel(self.widget_4)
                self.label_11.setGeometry(QtCore.QRect(10, 5, 300, 20)) #caliHeadL1
                self.label_11.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.label_11.setAlignment(QtCore.Qt.AlignCenter)
                self.label_11.setObjectName("label_11")
                self.label_11.setText("Calibration file1")
                sub_GridCal_1.addWidget(self.label_11, 1, 0, 1, 3)
                
                self.label_15 = QtWidgets.QLabel(self.widget_4)
                self.label_15.setGeometry(QtCore.QRect(3, 5, 100, 20)) #biasHeadL1
                self.label_15.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.label_15.setAlignment(QtCore.Qt.AlignCenter)
                self.label_15.setObjectName("label_15")
                sub_GridCal_1.addWidget(self.label_15, 1, 3 ,1 ,1)

                self.btn1 = QtWidgets.QPushButton(self.widget_5)
                self.btn1.setObjectName("btn1")
                self.btn1.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                sub_GridCal_1_1.addWidget(self.btn1,0,3,1,1)

                self.widget_12 = QtWidgets.QWidget(self.widget_4)#biasW1
                self.widget_12.setStyleSheet("border-radius: 0px;\n"
        "background-color: rgb(255, 255, 255);")
                self.widget_12.setObjectName("widget_12")
                sub_GridCal_1.addWidget(self.widget_12,2,3,1,1)
                sub_GridCal_1_2 = QGridLayout(self.widget_12)

                self.spinBox_4 = QtWidgets.QSpinBox(self.widget_12) #biasL1
                self.spinBox_4.setObjectName("spinBox_4")
                sub_GridCal_1_2.addWidget(self.spinBox_4, 0,0)


                self.widget_7 = QtWidgets.QWidget(self.groupBox_cal)
                self.widget_7.setGeometry(QtCore.QRect(80, 250, 450, 120)) #result2W
                self.widget_7.setStyleSheet("background-color:rgb(158, 158, 158);\n"
        "border: none")
                self.widget_7.setObjectName("widget_7")

                sub_GridCal_1 = QGridLayout(self.widget_7)
                self.label_6 = QtWidgets.QLabel(self.widget_7)#result2L
                self.label_6.setStyleSheet("align:\"center\";\n" "font-size:10pt;\n" "color:#fff")
                self.label_6.setObjectName("label_6")
                self.label_6.setText("Result1")
                sub_GridCal_1.addWidget( self.label_6,0,0)

                self.widget_8 = QtWidgets.QWidget(self.widget_7)#caliW2
                self.widget_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-radius: 0px;")
                self.widget_8.setObjectName("widget_8")
                sub_GridCal_1.addWidget(self.widget_8,2,0,1,3)

                sub_GridCal_1_1 = QGridLayout(self.widget_8)
                self.label_2_ = QtWidgets.QLabel(self.widget_8)#browse file2
                self.label_2_.setStyleSheet("background-color: rgb(255, 255, 255);\n""align:\"center\";\n" "font-size:5pt;\n" "color:#000;")
                self.label_2_.setAlignment(QtCore.Qt.AlignCenter)
                self.label_2_.setObjectName("label_2_")
                self.label_2_.setText("555")
                sub_GridCal_1_1.addWidget(self.label_2_,0,0,1,3)

                self.label_17 = QtWidgets.QLabel(self.widget_7)
                self.label_17.setGeometry(QtCore.QRect(10, 5, 300, 20)) #caliHeadL2
                self.label_17.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.label_17.setAlignment(QtCore.Qt.AlignCenter)
                self.label_17.setObjectName("label_17")
                self.label_17.setText("Calibration file2")
                sub_GridCal_1.addWidget(self.label_17, 1, 0, 1, 3)
                
                self.label_18 = QtWidgets.QLabel(self.widget_7)
                self.label_18.setGeometry(QtCore.QRect(3, 5, 100, 20)) #biasHeadL2
                self.label_18.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.label_18.setAlignment(QtCore.Qt.AlignCenter)
                self.label_18.setObjectName("label_18")
                sub_GridCal_1.addWidget(self.label_18, 1, 3 ,1 ,1)

                self.btn2 = QtWidgets.QPushButton(self.widget_8)
                self.btn2.setObjectName("btn2")
                self.btn2.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                sub_GridCal_1_1.addWidget(self.btn2,0,3,1,1)

                self.widget_17 = QtWidgets.QWidget(self.widget_7)#biasW2
                self.widget_17.setStyleSheet("border-radius: 0px;\n"
        "background-color: rgb(255, 255, 255);")
                self.widget_17.setObjectName("widget_17")
                sub_GridCal_1.addWidget(self.widget_17,2,3,1,1)

                sub_GridCal_1_2 = QGridLayout(self.widget_17)
                self.spinBox_5 = QtWidgets.QSpinBox(self.widget_17) #biasL2
                self.spinBox_5.setObjectName("spinBox_5")
                sub_GridCal_1_2.addWidget(self.spinBox_5, 0,0)


                self.widget_9 = QtWidgets.QWidget(self.groupBox_cal)
                self.widget_9.setGeometry(QtCore.QRect(80, 400, 450, 120)) #result3W
                self.widget_9.setStyleSheet("background-color:rgb(158, 158, 158);\n"
        "border:none")
                self.widget_9.setObjectName("widget_9")


                sub_GridCal_1 = QGridLayout(self.widget_9)
                self.label_7 = QtWidgets.QLabel(self.widget_9)#result3L
                self.label_7.setStyleSheet("align:\"center\";\n" "font-size:10pt;\n" "color:#fff")
                self.label_7.setObjectName("label_7")
                self.label_7.setText("Result3")
                sub_GridCal_1.addWidget( self.label_7,0,0)

                self.widget_22 = QtWidgets.QWidget(self.widget_9)#caliW3
                self.widget_22.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-radius: 0px;")
                self.widget_22.setObjectName("widget_22")
                sub_GridCal_1.addWidget(self.widget_22,2,0,1,3)

                sub_GridCal_1_1 = QGridLayout(self.widget_22)
                self.label_3_ = QtWidgets.QLabel(self.widget_22)#browse file3
                self.label_3_.setStyleSheet("background-color: rgb(255, 255, 255);\n""align:\"center\";\n" "font-size:5pt;\n" "color:#000;")
                self.label_3_.setAlignment(QtCore.Qt.AlignCenter)
                self.label_3_.setObjectName("label_3_")
                self.label_3_.setText("555")
                sub_GridCal_1_1.addWidget(self.label_3_,0,0,1,3)

                self.label_19 = QtWidgets.QLabel(self.widget_9)
                self.label_19.setGeometry(QtCore.QRect(10, 5, 300, 20)) #caliHeadL3
                self.label_19.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.label_19.setAlignment(QtCore.Qt.AlignCenter)
                self.label_19.setObjectName("label_19")
                self.label_19.setText("Calibration file2")
                sub_GridCal_1.addWidget(self.label_19, 1, 0, 1, 3)
                
                self.label_20 = QtWidgets.QLabel(self.widget_9)
                self.label_20.setGeometry(QtCore.QRect(3, 5, 100, 20)) #biasHeadL3
                self.label_20.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.label_20.setAlignment(QtCore.Qt.AlignCenter)
                self.label_20.setObjectName("label_20")
                sub_GridCal_1.addWidget(self.label_20, 1, 3 ,1 ,1)

                self.btn3 = QtWidgets.QPushButton(self.widget_22)
                self.btn3.setObjectName("btn3")
                self.btn3.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                sub_GridCal_1_1.addWidget(self.btn3,0,3,1,1)

                self.widget_23 = QtWidgets.QWidget(self.widget_9)#biasW3
                self.widget_23.setStyleSheet("border-radius: 0px;\n"
        "background-color: rgb(255, 255, 255);")
                self.widget_23.setObjectName("widget_17")
                sub_GridCal_1.addWidget(self.widget_23,2,3,1,1)

                sub_GridCal_1_2 = QGridLayout(self.widget_23)
                self.spinBox_6 = QtWidgets.QSpinBox(self.widget_23) #biasL3
                self.spinBox_6.setObjectName("spinBox_6")
                sub_GridCal_1_2.addWidget(self.spinBox_6, 0,0)


                self.widget_28 = QtWidgets.QWidget(self.groupBox_cal)#result4W
                self.widget_28.setStyleSheet("background-color:rgb(158, 158, 158);\n"
        "border:none")
                self.widget_28.setObjectName("widget_28")

                sub_GridCal_1 = QGridLayout(self.widget_28)
                self.label_8 = QtWidgets.QLabel(self.widget_28)#result4L
                self.label_8.setStyleSheet("align:\"center\";\n" "font-size:10pt;\n" "color:#fff")
                self.label_8.setObjectName("label_8")
                self.label_8.setText("Result4")
                sub_GridCal_1.addWidget( self.label_8,0,0)

                self.widget_29 = QtWidgets.QWidget(self.widget_28)#caliW4
                self.widget_29.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-radius: 0px;")
                self.widget_29.setObjectName("widget_29")
                sub_GridCal_1.addWidget(self.widget_29,2,0,1,3)

                sub_GridCal_1_1 = QGridLayout(self.widget_29)
                self.label_4_ = QtWidgets.QLabel(self.widget_29)#browse file4
                self.label_4_.setStyleSheet("background-color: rgb(255, 255, 255);\n""align:\"center\";\n" "font-size:5pt;\n" "color:#000;")
                self.label_4_.setAlignment(QtCore.Qt.AlignCenter)
                self.label_4_.setObjectName("label_4_")
                self.label_4_.setText("5556")
                sub_GridCal_1_1.addWidget(self.label_4_,0,0,1,3)

                self.label_21 = QtWidgets.QLabel(self.widget_28)
                self.label_21.setGeometry(QtCore.QRect(10, 5, 300, 20)) #caliHeadL4
                self.label_21.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.label_21.setAlignment(QtCore.Qt.AlignCenter)
                self.label_21.setObjectName("label_21")
                self.label_21.setText("Calibration file4")
                sub_GridCal_1.addWidget(self.label_21, 1, 0, 1, 3)
                
                self.label_22 = QtWidgets.QLabel(self.widget_28)
                self.label_22.setGeometry(QtCore.QRect(3, 5, 100, 20)) #biasHeadL4
                self.label_22.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.label_22.setAlignment(QtCore.Qt.AlignCenter)
                self.label_22.setObjectName("label_22")
                sub_GridCal_1.addWidget(self.label_22, 1, 3 ,1 ,1)

                self.btn4 = QtWidgets.QPushButton(self.widget_29)
                self.btn4.setObjectName("btn4")
                self.btn4.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                sub_GridCal_1_1.addWidget(self.btn4,0,3,1,1)

                self.widget_30 = QtWidgets.QWidget(self.widget_28)#biasW4
                self.widget_30.setStyleSheet("border-radius: 0px;\n"
        "background-color: rgb(255, 255, 255);")
                self.widget_30.setObjectName("widget_30")
                sub_GridCal_1.addWidget(self.widget_30,2,3,1,1)

                sub_GridCal_1_2 = QGridLayout(self.widget_30)
                self.spinBox_7 = QtWidgets.QSpinBox(self.widget_30) #biasL4
                self.spinBox_7.setObjectName("spinBox_7")
                sub_GridCal_1_2.addWidget(self.spinBox_7, 0,0)



                self.widget_35 = QtWidgets.QWidget(self.groupBox_cal)#result5W
                self.widget_35.setStyleSheet("background-color:rgb(158, 158, 158);\n"
        "border:none")
                self.widget_35.setObjectName("widget_35")

                sub_GridCal_1 = QGridLayout(self.widget_35)
                self.label_9 = QtWidgets.QLabel(self.widget_35)#result5L
                self.label_9.setStyleSheet("align:\"center\";\n" "font-size:10pt;\n" "color:#fff")
                self.label_9.setObjectName("label_8")
                self.label_9.setText("Result5")
                sub_GridCal_1.addWidget( self.label_9,0,0)
                self.widget_36 = QtWidgets.QWidget(self.widget_35)#caliW5
                self.widget_36.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-radius: 0px;")
                self.widget_36.setObjectName("widget_36")
                sub_GridCal_1.addWidget(self.widget_36,2,0,1,3)

                sub_GridCal_1_1 = QGridLayout(self.widget_36)
                self.label_5_ = QtWidgets.QLabel(self.widget_36)#browse file5
                self.label_5_.setStyleSheet("background-color: rgb(255, 255, 255);\n""align:\"center\";\n" "font-size:5pt;\n" "color:#000;")
                self.label_5_.setAlignment(QtCore.Qt.AlignCenter)
                self.label_5_.setObjectName("label_5_")
                self.label_5_.setText("555")
                sub_GridCal_1_1.addWidget(self.label_5_,0,0,1,3)

                self.label_23 = QtWidgets.QLabel(self.widget_35)
                self.label_23.setGeometry(QtCore.QRect(10, 5, 300, 20)) #caliHeadL5
                self.label_23.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.label_23.setAlignment(QtCore.Qt.AlignCenter)
                self.label_23.setObjectName("label_23")
                self.label_23.setText("Calibration file5")
                sub_GridCal_1.addWidget(self.label_23, 1, 0, 1, 3)
                
                self.label_24 = QtWidgets.QLabel(self.widget_35)
                self.label_24.setGeometry(QtCore.QRect(3, 5, 100, 20)) #biasHeadL5
                self.label_24.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.label_24.setAlignment(QtCore.Qt.AlignCenter)
                self.label_24.setObjectName("label_24")
                sub_GridCal_1.addWidget(self.label_24, 1, 3 ,1 ,1)

                self.btn5 = QtWidgets.QPushButton(self.widget_36)
                self.btn5.setObjectName("btn5")
                self.btn5.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                sub_GridCal_1_1.addWidget(self.btn5,0,3,1,1)

                self.widget_41 = QtWidgets.QWidget(self.widget_35)#biasW5
                self.widget_41.setStyleSheet("border-radius: 0px;\n"
        "background-color: rgb(255, 255, 255);")
                self.widget_41.setObjectName("widget_41")
                sub_GridCal_1.addWidget(self.widget_41,2,3,1,1)
                
                sub_GridCal_1_2 = QGridLayout(self.widget_41)
                self.spinBox_8 = QtWidgets.QSpinBox(self.widget_41) #biasL5
                self.spinBox_8.setObjectName("spinBox_8")
                sub_GridCal_1_2.addWidget(self.spinBox_8, 0,0)


                sub_groupbox_cal.addWidget(self.Label , 0 , 0 , 1 , 6)
                sub_groupbox_cal.addWidget(self.widget_4 , 1 , 1 , 1 , 4)
                sub_groupbox_cal.addWidget(self.widget_7 , 2 , 1 , 1 , 4)
                sub_groupbox_cal.addWidget(self.widget_9 , 3 , 1 , 1 , 4)
                sub_groupbox_cal.addWidget(self.widget_28 , 4 , 1 , 1 , 4)
                sub_groupbox_cal.addWidget(self.widget_35 , 5 , 1 , 1 , 4)


                self.groupBox_Spec = QtWidgets.QGroupBox(self.body)
                self.groupBox_Spec.setStyleSheet("border-radius: 5px;\n"
        "border: 2px solid black")
                self.groupBox_Spec.setObjectName("groupBox_Spec")

                sub_GridSpec = QGridLayout(self.groupBox_Spec)

                self.groupBox_Spec_integration = QtWidgets.QGroupBox(self.groupBox_Spec)
                self.groupBox_Spec_integration.setStyleSheet("border-radius: 0px;\n"
        "border: 0px solid black;\n background-color: transparent;")

                sub_groupBox_Spec_integration = QGridLayout(self.groupBox_Spec_integration)

                self.Label_Spec = QtWidgets.QLabel(self.groupBox_Spec_integration)
                self.Label_Spec.setStyleSheet("color:black;\n"
                "border: none;\n" "font-size:14pt bold;\n")

                self.widget_6 = QtWidgets.QWidget(self.groupBox_Spec_integration)
                self.widget_6.setStyleSheet("\n"
        "background-color: rgb(153, 153, 153);\n"
        "border:none;\n")
                self.widget_6.setObjectName("widget_6")

                integration = QGridLayout(self.widget_6)
                self.label_12 = QtWidgets.QLabel()#integrationL
                self.label_12.setObjectName("label_12")
                self.spinBox = QtWidgets.QSpinBox(self.widget_6)#integrationspinBox
                self.spinBox.setStyleSheet("border-color:rgb(158, 158, 158);\n"
        "background-color: rgb(236, 236, 236);\n""")
                self.spinBox.setObjectName("spinBox")
                self.label_16 = QtWidgets.QLabel(self.widget_6)
                self.label_16.setStyleSheet("align:\"center\";\n" "font-size:10pt;\n" "color:#fff")
                self.label_16.setObjectName("label_16")

                integration.addWidget(self.label_12,0,0)
                integration.addWidget(self.spinBox,0,1)
                integration.addWidget(self.label_16,0,2)


                sub_groupBox_Spec_integration.addWidget(self.Label_Spec,0,0)
                sub_groupBox_Spec_integration.addWidget(self.widget_6,1,0)


                self.groupBox_Spec_Wave = QtWidgets.QGroupBox(self.groupBox_Spec)
                self.groupBox_Spec_Wave.setStyleSheet("border-radius: 0px;\n"
        "border: 0px solid black;\nbackground-color: transparent;")

                sub_groupBox_Spec_Wave  = QGridLayout(self.groupBox_Spec_Wave)
                self.Label_Wave= QtWidgets.QLabel(self.groupBox_Spec_Wave)
                self.Label_Wave.setStyleSheet("color:black;\n"
                "border: none;\n" "font-size:14pt bold;\n")

                self.Label_Wave.setObjectName("Label_Wave")

                self.widget_10 = QtWidgets.QWidget(self.groupBox_Spec_Wave)
                self.widget_10.setStyleSheet("\n"
        "background-color: rgb(153, 153, 153);\n"
        "border:none;\n")
                self.widget_10.setObjectName("widget_10")

                Wave = QGridLayout(self.widget_10)

                self.label_13 = QtWidgets.QLabel()#M_wavelength_L
                self.label_13.setStyleSheet("align:\"center\";\n" "font-size:10pt;\n" "color:#fff")
                self.label_13.setObjectName("label_13")

                self.spinBox_3 = QtWidgets.QSpinBox(self.widget_10)#N_wavelength_W
                self.spinBox_3.setStyleSheet("border-color:rgb(158, 158, 158);\n"
        "background-color: #fff;\n"
        "font-size:14pt;\n")
                self.spinBox_3.setObjectName("spinBox_3")

                self.label_14 = QtWidgets.QLabel(self.widget_10)
                self.label_14.setStyleSheet("align:\"center\";\n" "font-size:10pt;\n" "color:#fff")
                self.label_14.setObjectName("label_14")

                self.spinBox_2 = QtWidgets.QSpinBox(self.widget_10)#boxN_wavelength_W
                self.spinBox_2.setStyleSheet("border-color:rgb(158, 158, 158);\n"
        "background-color: #fff;\n"
        "font-size:14pt;\n")
                self.spinBox_2.setObjectName("spinBox_2")

                Wave.addWidget(self.label_13,0,0)
                Wave.addWidget(self.spinBox_3,0,1)
                Wave.addWidget(self.label_14,1,0)
                Wave.addWidget(self.spinBox_2,1,1)

                sub_groupBox_Spec_Wave.addWidget(self.Label_Wave,0,0)
                sub_groupBox_Spec_Wave.addWidget(self.widget_10,1,0)

                self.groupBox_Spec_Upload = QtWidgets.QGroupBox(self.groupBox_Spec)
                self.groupBox_Spec_Upload .setStyleSheet("border-radius: 0px;\n"
        "border: 0px solid black;\nbackground-color: transparent;")

                sub_groupBox_Spec_Upload  = QGridLayout(self.groupBox_Spec_Upload)
                self.Label_Upload= QtWidgets.QLabel(self.groupBox_Spec_Upload)
                self.Label_Upload.setStyleSheet("color:black;\n"
                "border: none;\n" "font-size:10pt bold;\n")

                self.Label_Upload.setObjectName("Label_Upload")

                self.widget_Upload = QtWidgets.QWidget(self.groupBox_Spec_Upload)
                self.widget_Upload .setStyleSheet("\n"
        "background-color: rgb(153, 153, 153);\n"
        "border:none;\n")
                self.widget_Upload .setObjectName("widget_Upload")

                Upload = QGridLayout(self.widget_Upload)

                self.btn_Upload = QtWidgets.QPushButton(self.widget_Upload)
                self.btn_Upload.setStyleSheet("border-radius:50px;\n"
        "background-color:rgb(255, 255, 255);\n"
        "font-size:14px;\n"
        "color:#000;")

                self.btn_Upload.setObjectName("btn_Upload")
                # self.btn_Upload.setIcon()
                Upload.addWidget(self.btn_Upload,0,0,2,1)




                sub_groupBox_Spec_Upload.addWidget(self.Label_Upload,0,0)
                sub_groupBox_Spec_Upload.addWidget(self.widget_Upload,1,0)

                sub_GridSpec.addWidget(self.groupBox_Spec_integration,0,0)
                sub_GridSpec.addWidget(self.groupBox_Spec_Wave,1,0)
                sub_GridSpec.addWidget(self.groupBox_Spec_Upload,2,0)


                subBody_gridLayout.addWidget(self.groupBox_cal,0,0,1,3)
                subBody_gridLayout.addWidget(self.groupBox_Spec,0,3,1,1)

                gridLayout.addWidget(self.body,0, 0, 5, 6)

                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setLocale(QtCore.QLocale(QtCore.QLocale.Thai, QtCore.QLocale.Thailand))
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setProperty("Color", QtGui.QColor(0, 0, 0))
                self.frame.setObjectName("frame")

                sub_gridLayout = QGridLayout(self.frame)
                self.pushButton_4 = QtWidgets.QPushButton(self.frame)
                self.pushButton_4.setStyleSheet("border-radius:30px;\n"
        "background-color:rgb(0, 170, 0);\n"
        "font-size:24px;\n"
        "color:#fff;")
                self.pushButton_4.setObjectName("pushButton_4")
                self.pushButton_3 = QtWidgets.QPushButton(self.frame)
                self.pushButton_3.setStyleSheet("border-radius:30px;\n"
        "background-color:#aa0000;\n"
        "font-size:24px;\n"
        "color:#fff;")
                self.pushButton_3.setObjectName("pushButton_3")

                self.pushButton_4.setFixedHeight(80)
                self.pushButton_3.setFixedHeight(80)
                sub_gridLayout.addWidget(QtWidgets.QLabel(self.body),0,0)
                sub_gridLayout.addWidget(self.pushButton_4,0,1)
                sub_gridLayout.addWidget(QtWidgets.QLabel(self.body),0,2)
                sub_gridLayout.addWidget(self.pushButton_3,0,3)
                sub_gridLayout.addWidget(QtWidgets.QLabel(self.body),0,4)

                gridLayout.addWidget(self.frame,5, 0, 1, 6)

                

                self.groupBox.setLayout(gridLayout)
                lay.addWidget(self.groupBox)
                # lay.addStretch()
                self.Label_Spec.setAlignment(QtCore.Qt.AlignCenter)
                self.Label_Wave.setAlignment(QtCore.Qt.AlignCenter)
                self.Label_Upload.setAlignment(QtCore.Qt.AlignCenter)
                # scroll.setFixedHeight(960)
                # scroll.setFixedWidth(1280)
                self.box.addWidget(scroll)
                self.pushButton_3.clicked.connect(self.close)
                # self.retranslateUi(self)

        
        
        # def setIcon(self):
                # appIcon = QIcon("icon.png")
                # MainWindow.setWindowIcon(appIcon)
        # def retranslateUi(self, MainWindow):
        #         _translate = QtCore.QCoreApplication.translate
                # MainWindow.setWindowTitle(_translate("MainWindow", "System Configuration"))
                self.pushButton_4.setText("APPLY")
                self.pushButton_3.setText("CANCEL")
                self.Label.setText("Calculation Setting")
                self.label_5.setText("Result1")


                self.label_11.setText("Calibration file1")
                self.label_15.setText("Bias")
                self.label_6.setText("Result2")


                self.label_17.setText("Calibration file2")
                self.label_18.setText("Bias")
                self.label_7.setText("Result3")

                self.btn_Upload.setText("Upload file")
                self.Label_Upload.setText("Directory Folder")



                self.label_19.setText("Calibration file3")
                self.label_20.setText("Bias")
                self.label_8.setText("Result4")
                self.label_1_.setText("....")
                self.label_2_.setText("....")
                self.label_3_.setText("....")
                self.label_4_.setText("....")
                self.label_5_.setText("....")

                self.label_21.setText("Calibration file4")
                self.label_22.setText("Bias")
                self.label_9.setText("Result5")

                
                self.label_23.setText("Calibration file5")
                self.label_24.setText("Bias")
                #self.groupBox_2.setTitle(_translate("MainWindow", "Spectrometer Setting"))
                self.Label_Spec.setText("Spectrometer Setting")
                self.label_12.setText("Integration time")
                self.label_16.setText("ms")
                #self.groupBox_3.setTitle(_translate("MainWindow", "Wave Length"))
                self.Label_Wave.setText("Wave Length")
                self.label_13.setText("N")
                self.label_14.setText( "M")
                # self.btnBack.setText(_translate("MainWindow", "Back"))
                self.btn1.setText("browse")
                self.btn2.setText("browse")
                self.btn3.setText("browse")
                self.btn4.setText("browse")
                self.btn5.setText("browse")

if __name__ == '__main__':
        app = QApplication(sys.argv)
        myapp = Ui_MainWindow()
        myapp.show()
        sys.exit(app.exec_())