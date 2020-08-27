
from PyQt5.QtWidgets import QLineEdit,QMainWindow,QScrollArea,QApplication, QWidget , QVBoxLayout, QPushButton, QGroupBox, QGridLayout
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

                self.setWindowTitle("Pre Processing")
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
        "background-color:transparent;\n"
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
                # self.label_5.setText("Result1")
                sub_GridCal_1.addWidget( self.label_5,0,0)

                self.widget_5 = QtWidgets.QWidget(self.widget_4)#caliW1
                self.widget_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-radius: 0px;")
                self.widget_5.setObjectName("widget_5")
                sub_GridCal_1.addWidget(self.widget_5,2,0,1,3)

                sub_GridCal_1_1 = QGridLayout(self.widget_5)
                self.label_RAW = QtWidgets.QLabel(self.widget_5)#browse file1
                self.label_RAW.setStyleSheet("background-color: rgb(255, 255, 255);\n""align:\"center\";\n" "font-size:5pt;\n" "color:#000;")
                self.label_RAW.setAlignment(QtCore.Qt.AlignCenter)
                self.label_RAW.setObjectName("label_RAW")
                sub_GridCal_1_1.addWidget(self.label_RAW,0,0,1,3)

                self.Topic_RAW = QtWidgets.QLabel(self.widget_4)
                self.Topic_RAW.setGeometry(QtCore.QRect(10, 5, 300, 20)) #caliHeadL1
                self.Topic_RAW.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.Topic_RAW.setAlignment(QtCore.Qt.AlignCenter)
                self.Topic_RAW.setObjectName("Topic_RAW")
                sub_GridCal_1.addWidget(self.Topic_RAW, 1, 0, 1, 3)
            
                self.widget_7 = QtWidgets.QWidget(self.groupBox_cal)
                self.widget_7.setGeometry(QtCore.QRect(80, 250, 450, 120)) #result2W
                self.widget_7.setStyleSheet("background-color:rgb(158, 158, 158);\n"
        "border: none")
                self.widget_7.setObjectName("widget_7")

                sub_GridCal_1 = QGridLayout(self.widget_7)
                self.label_6 = QtWidgets.QLabel(self.widget_7)#result2L
                self.label_6.setStyleSheet("align:\"center\";\n" "font-size:10pt;\n" "color:#fff")
                self.label_6.setObjectName("label_6")
                sub_GridCal_1.addWidget( self.label_6,0,0)

                self.widget_8 = QtWidgets.QWidget(self.widget_7)#caliW2
                self.widget_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-radius: 0px;")
                self.widget_8.setObjectName("widget_8")
                sub_GridCal_1.addWidget(self.widget_8,2,0,1,3)

                sub_GridCal_1_1 = QGridLayout(self.widget_8)
                self.label_SNV = QtWidgets.QLabel(self.widget_8)#browse file2
                self.label_SNV.setStyleSheet("background-color: rgb(255, 255, 255);\n""align:\"center\";\n" "font-size:5pt;\n" "color:#000;")
                self.label_SNV.setAlignment(QtCore.Qt.AlignCenter)
                self.label_SNV.setObjectName("label_SNV")
                sub_GridCal_1_1.addWidget(self.label_SNV,0,0,1,3)

                self.Topic_SNV = QtWidgets.QLabel(self.widget_7)
                self.Topic_SNV.setGeometry(QtCore.QRect(10, 5, 300, 20)) #caliHeadL2
                self.Topic_SNV.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.Topic_SNV.setAlignment(QtCore.Qt.AlignCenter)
                self.Topic_SNV.setObjectName("Topic_SNV")
                sub_GridCal_1.addWidget(self.Topic_SNV, 1, 0, 1, 3)
                

                self.widget_9 = QtWidgets.QWidget(self.groupBox_cal)
                self.widget_9.setGeometry(QtCore.QRect(80, 400, 450, 120)) #result3W
                self.widget_9.setStyleSheet("background-color:rgb(158, 158, 158);\n"
        "border:none")
                self.widget_9.setObjectName("widget_9")


                sub_GridCal_1 = QGridLayout(self.widget_9)
                self.label_7 = QtWidgets.QLabel(self.widget_9)#result3L
                self.label_7.setStyleSheet("align:\"center\";\n" "font-size:10pt;\n" "color:#fff")
                self.label_7.setObjectName("label_7")
                sub_GridCal_1.addWidget( self.label_7,0,0)

                self.widget_22 = QtWidgets.QWidget(self.widget_9)#caliW3
                self.widget_22.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-radius: 0px;")
                self.widget_22.setObjectName("widget_22")
                sub_GridCal_1.addWidget(self.widget_22,2,0,1,3)

                sub_GridCal_1_1 = QGridLayout(self.widget_22)
                self.label_MSC = QtWidgets.QLabel(self.widget_22)#browse file3
                self.label_MSC.setStyleSheet("background-color: rgb(255, 255, 255);\n""align:\"center\";\n" "font-size:5pt;\n" "color:#000;")
                self.label_MSC.setAlignment(QtCore.Qt.AlignCenter)
                self.label_MSC.setObjectName("label_MSC")
                sub_GridCal_1_1.addWidget(self.label_MSC,0,0,1,3)

                self.Topic_MSC = QtWidgets.QLabel(self.widget_9)
                self.Topic_MSC.setGeometry(QtCore.QRect(10, 5, 300, 20)) #caliHeadL3
                self.Topic_MSC.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.Topic_MSC.setAlignment(QtCore.Qt.AlignCenter)
                self.Topic_MSC.setObjectName("Topic_MSC")
                sub_GridCal_1.addWidget(self.Topic_MSC, 1, 0, 1, 3)
                


                self.widget_28 = QtWidgets.QWidget(self.groupBox_cal)
                self.widget_28.setStyleSheet("background-color:rgb(158, 158, 158);\n"
        "border:none")
                self.widget_28.setObjectName("widget_28")

                sub_GridCal_1 = QGridLayout(self.widget_28)
                self.label_8 = QtWidgets.QLabel(self.widget_28)
                self.label_8.setStyleSheet("align:\"center\";\n" "font-size:10pt;\n" "color:#fff")
                self.label_8.setObjectName("label_8")
                sub_GridCal_1.addWidget( self.label_8,0,0)

                self.widget_29 = QtWidgets.QWidget(self.widget_28)
                self.widget_29.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-radius: 0px;")
                self.widget_29.setObjectName("widget_29")
                sub_GridCal_1.addWidget(self.widget_29,2,0,1,3)

                sub_GridCal_1_1 = QGridLayout(self.widget_29)
                self.label_1stDeri = QtWidgets.QLabel(self.widget_29)#result1
                self.label_1stDeri.setStyleSheet("background-color: rgb(255, 255, 255);\n""align:\"center\";\n" "font-size:5pt;\n" "color:#000;")
                self.label_1stDeri.setAlignment(QtCore.Qt.AlignCenter)
                self.label_1stDeri.setObjectName("label_1stDeri")
                sub_GridCal_1_1.addWidget(self.label_1stDeri,0,0,1,3)

                self.Topic_1stDerivative = QtWidgets.QLabel(self.widget_28)
                self.Topic_1stDerivative.setGeometry(QtCore.QRect(10, 5, 300, 20))
                self.Topic_1stDerivative.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.Topic_1stDerivative.setAlignment(QtCore.Qt.AlignCenter)
                self.Topic_1stDerivative.setObjectName("Topic_1stDerivative")
                sub_GridCal_1.addWidget(self.Topic_1stDerivative, 1, 0, 1, 3)
                
                self.label_22 = QtWidgets.QLabel(self.widget_28)
                self.label_22.setGeometry(QtCore.QRect(3, 5, 100, 20)) 
                self.label_22.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.label_22.setAlignment(QtCore.Qt.AlignCenter)
                self.label_22.setObjectName("label_22")
                sub_GridCal_1.addWidget(self.label_22, 1, 3 ,1 ,1)

                self.widget_30 = QtWidgets.QWidget(self.widget_28)#grab_1
                self.widget_30.setStyleSheet("border-radius: 0px;\n"
        "background-color: rgb(255, 255, 255);")
                self.widget_30.setObjectName("widget_30")
                sub_GridCal_1.addWidget(self.widget_30,2,3,1,1)

                sub_GridCal_4_1 = QGridLayout(self.widget_30)
                self.spinBox_7 = QtWidgets.QSpinBox(self.widget_30) #grab_1
                self.spinBox_7.setObjectName("spinBox_7")
                sub_GridCal_4_1.addWidget(self.spinBox_7, 0,0)

                self.Seg_1st = QtWidgets.QLabel(self.widget_28)
                self.Seg_1st.setGeometry(QtCore.QRect(3, 5, 100, 20)) #grab_1
                self.Seg_1st.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.Seg_1st.setAlignment(QtCore.Qt.AlignCenter)
                self.Seg_1st.setObjectName("Seg_1st")
                sub_GridCal_1.addWidget(self.Seg_1st, 1, 4 ,1 ,1)

                self.Seg_1st_W = QtWidgets.QWidget(self.widget_28)#spinBox_Seg_1st
                self.Seg_1st_W.setStyleSheet("border-radius: 0px;\n"
        "background-color: rgb(255, 255, 255);")
                self.Seg_1st_W.setObjectName("Seg_1st_W")
                sub_GridCal_1.addWidget(self.Seg_1st_W,2,4,1,1)

                sub_GridCal_4_2 = QGridLayout(self.Seg_1st_W)
                self.spinBox_Seg_1st = QtWidgets.QSpinBox(self.widget_30) #spinBox_Seg_1st
                self.spinBox_Seg_1st .setObjectName("spinBox_Seg_1st ")
                sub_GridCal_4_2.addWidget(self.spinBox_Seg_1st , 0,0)



                self.widget_35 = QtWidgets.QWidget(self.groupBox_cal)#2
                self.widget_35.setStyleSheet("background-color:rgb(158, 158, 158);\n"
        "border:none")
                self.widget_35.setObjectName("widget_35")

                sub_GridCal_1 = QGridLayout(self.widget_35)
                self.label_9 = QtWidgets.QLabel(self.widget_35)#2
                self.label_9.setStyleSheet("align:\"center\";\n" "font-size:10pt;\n" "color:#fff")
                self.label_9.setObjectName("label_8")

                sub_GridCal_1.addWidget( self.label_9,0,0)
                self.widget_36 = QtWidgets.QWidget(self.widget_35)#2
                self.widget_36.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-radius: 0px;")
                self.widget_36.setObjectName("widget_36")
                sub_GridCal_1.addWidget(self.widget_36,2,0,1,3)

                sub_GridCal_1_1 = QGridLayout(self.widget_36)
                self.label_2ndDeri = QtWidgets.QLabel(self.widget_36)#result 2
                self.label_2ndDeri.setStyleSheet("background-color: rgb(255, 255, 255);\n""align:\"center\";\n" "font-size:5pt;\n" "color:#000;")
                self.label_2ndDeri.setAlignment(QtCore.Qt.AlignCenter)
                self.label_2ndDeri.setObjectName("label_2ndDeri")
                sub_GridCal_1_1.addWidget(self.label_2ndDeri,0,0,1,3)

                self.Topic_2ndDerivative = QtWidgets.QLabel(self.widget_35)
                self.Topic_2ndDerivative.setGeometry(QtCore.QRect(10, 5, 300, 20)) #2
                self.Topic_2ndDerivative.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.Topic_2ndDerivative.setAlignment(QtCore.Qt.AlignCenter)
                self.Topic_2ndDerivative.setObjectName("Topic_2ndDerivative")
                sub_GridCal_1.addWidget(self.Topic_2ndDerivative, 1, 0, 1, 3)
                
                self.label_24 = QtWidgets.QLabel(self.widget_35)
                self.label_24.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.label_24.setAlignment(QtCore.Qt.AlignCenter)
                self.label_24.setObjectName("label_24")
                sub_GridCal_1.addWidget(self.label_24, 1, 3 ,1 ,1)

                self.widget_41 = QtWidgets.QWidget(self.widget_35)#grab2
                self.widget_41.setStyleSheet("border-radius: 0px;\n"
        "background-color: rgb(255, 255, 255);")
                self.widget_41.setObjectName("widget_41")
                sub_GridCal_1.addWidget(self.widget_41,2,3,1,1)
                
                sub_GridCal_5_1 = QGridLayout(self.widget_41)
                self.spinBox_8 = QtWidgets.QSpinBox(self.widget_41)#grab2
                self.spinBox_8.setObjectName("spinBox_8")
                sub_GridCal_5_1.addWidget(self.spinBox_8, 0,0)

                self.Seg_2nd = QtWidgets.QLabel(self.widget_35)
                self.Seg_2nd.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.Seg_2nd.setAlignment(QtCore.Qt.AlignCenter)
                self.Seg_2nd.setObjectName("Seg_2nd")
                sub_GridCal_1.addWidget(self.Seg_2nd, 1, 4 ,1 ,1)

                self.Seg_2nd_W = QtWidgets.QWidget(self.widget_35)#Seg_2nd_W
                self.Seg_2nd_W.setStyleSheet("border-radius: 0px;\n"
        "background-color: rgb(255, 255, 255);")
                self.Seg_2nd_W.setObjectName("Seg_2nd_W")
                sub_GridCal_1.addWidget(self.Seg_2nd_W,2,4,1,1)
                
                sub_GridCal_5_2 = QGridLayout(self.Seg_2nd_W)
                self.spinBox_Seg_2nd = QtWidgets.QSpinBox(self.Seg_2nd_W)#Seg_2nd_W
                self.spinBox_Seg_2nd.setObjectName("spinBox_Seg_2nd")
                sub_GridCal_5_2.addWidget(self.spinBox_Seg_2nd, 0,0)

                self.Smoothing = QtWidgets.QWidget(self.groupBox_cal)#Smoothing
                self.Smoothing.setStyleSheet("background-color:rgb(158, 158, 158);\n"
        "border:none")
                self.Smoothing.setObjectName("Smoothing")

                sub_GridCal_6 = QGridLayout(self.Smoothing)
                self.tmp = QtWidgets.QLabel(self.Smoothing)#Smoothing
                self.tmp.setStyleSheet("align:\"center\";\n" "font-size:10pt;\n" "color:#fff")
                self.tmp.setObjectName("tmp")

                sub_GridCal_6.addWidget(self.tmp,0,0)

                self.widget_Smoothing = QtWidgets.QWidget(self.Smoothing)#Smoothing
                self.widget_Smoothing.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-radius: 0px;")
                self.widget_Smoothing.setObjectName("widget_Smoothing")
                sub_GridCal_6.addWidget(self.widget_Smoothing,2,0,1,3)

                sub_GridCal_1_1 = QGridLayout(self.widget_Smoothing)
                self.label_Smoothing = QtWidgets.QLabel(self.widget_Smoothing)#label_Smoothing
                self.label_Smoothing.setStyleSheet("background-color: rgb(255, 255, 255);\n""align:\"center\";\n" "font-size:5pt;\n" "color:#000;")
                self.label_Smoothing.setAlignment(QtCore.Qt.AlignCenter)
                self.label_Smoothing.setObjectName("label_2ndDeri")
                sub_GridCal_1_1.addWidget(self.label_Smoothing,0,0,1,3)

                self.Topic_Smoothing = QtWidgets.QLabel(self.Smoothing)
                self.Topic_Smoothing.setGeometry(QtCore.QRect(10, 5, 300, 20)) #2
                self.Topic_Smoothing.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.Topic_Smoothing.setAlignment(QtCore.Qt.AlignCenter)
                self.Topic_Smoothing.setObjectName("Topic_Smoothing")
                sub_GridCal_6.addWidget(self.Topic_Smoothing, 1, 0, 1, 3)
                
                self.grab_Smoothing = QtWidgets.QLabel(self.Smoothing)
                self.grab_Smoothing.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.grab_Smoothing.setAlignment(QtCore.Qt.AlignCenter)
                self.grab_Smoothing.setObjectName("grab_Smoothing")
                sub_GridCal_6.addWidget(self.grab_Smoothing, 1, 3 ,1 ,1)

                self.grab_Smoothing_w = QtWidgets.QWidget(self.Smoothing)#grab2
                self.grab_Smoothing_w.setStyleSheet("border-radius: 0px;\n"
        "background-color: rgb(255, 255, 255);")
                self.grab_Smoothing_w.setObjectName("grab_Smoothing_w")
                sub_GridCal_6.addWidget(self.grab_Smoothing_w,2,3,1,1)
                
                sub_GridCal_6_1 = QGridLayout(self.grab_Smoothing_w)
                self.spinBox_grab_Smoothing_w = QtWidgets.QSpinBox(self.grab_Smoothing_w)#grab2
                self.spinBox_grab_Smoothing_w.setObjectName("grab_Smoothing_w")
                sub_GridCal_6_1.addWidget(self.spinBox_grab_Smoothing_w, 0,0)

                self.Seg_Smoothing = QtWidgets.QLabel(self.Smoothing)
                self.Seg_Smoothing.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border-radius:15px 50px 30px 5px;\n" "align:\"center\";\n"
        "font-size:8pt;")
                self.Seg_Smoothing.setAlignment(QtCore.Qt.AlignCenter)
                self.Seg_Smoothing.setObjectName("Seg_Smoothing")
                sub_GridCal_6.addWidget(self.Seg_Smoothing, 1, 4 ,1 ,1)

                self.Seg_Smoothing_W = QtWidgets.QWidget(self.widget_35)#Seg_Smoothing
                self.Seg_Smoothing_W.setStyleSheet("border-radius: 0px;\n"
        "background-color: rgb(255, 255, 255);")
                self.Seg_Smoothing_W.setObjectName("Seg_Smoothing_W")
                sub_GridCal_6.addWidget(self.Seg_Smoothing_W,2,4,1,1)
                
                sub_GridCal_6_2 = QGridLayout(self.Seg_Smoothing_W)
                self.spinBox_Seg_Smoothing = QtWidgets.QSpinBox(self.Seg_Smoothing_W)#Seg_Smoothing
                self.spinBox_Seg_Smoothing.setObjectName("spinBox_Seg_Smoothing")
                sub_GridCal_6_2.addWidget(self.spinBox_Seg_Smoothing, 0,0)


                sub_groupbox_cal.addWidget(self.Label , 0 , 0 , 1 , 6)
                sub_groupbox_cal.addWidget(self.widget_4 , 1 , 1 , 1 , 4)
                sub_groupbox_cal.addWidget(self.widget_7 , 2 , 1 , 1 , 4)
                sub_groupbox_cal.addWidget(self.widget_9 , 3 , 1 , 1 , 4)
                sub_groupbox_cal.addWidget(self.widget_28 , 4 , 1 , 1 , 4)
                sub_groupbox_cal.addWidget(self.widget_35 , 5 , 1 , 1 , 4)
                sub_groupbox_cal.addWidget(self.Smoothing , 6 , 1 , 1 , 4)


                self.groupBox_Spec = QtWidgets.QGroupBox(self.body)
                self.groupBox_Spec.setStyleSheet("border-radius: 5px;\n"
        "border: 2px solid black")
                self.groupBox_Spec.setObjectName("groupBox_Spec")

                sub_GridSpec = QGridLayout(self.groupBox_Spec)

                self.groupBox_Spec_integration = QtWidgets.QGroupBox(self.groupBox_Spec)
                self.groupBox_Spec_integration.setStyleSheet("border-radius: 0px;\n"
        "border: 0px solid black;\n background-color: transparent;")

                sub_groupBox_Spec_integration = QGridLayout(self.groupBox_Spec_integration)

                self.Label_STEP = QtWidgets.QLabel(self.groupBox_Spec_integration)
                self.Label_STEP.setStyleSheet("color:black;\n"
                "border: none;\n" "font-size:14pt bold;\n")

                self.widget_6 = QtWidgets.QWidget(self.groupBox_Spec_integration)
                self.widget_6.setStyleSheet("\n"
        "background-color: rgb(153, 153, 153);\n"
        "border:none;\n")
                self.widget_6.setObjectName("widget_6")

                integration = QGridLayout(self.widget_6)

                self.label_step1 = QtWidgets.QLabel()
                self.label_step1.setStyleSheet("align:\"center\";\n"
        "font-size: 10pt;")
                self.label_step1.setObjectName("label_step1")

                self.comboBox = QtWidgets.QComboBox(self.widget_6)
                self.comboBox.setObjectName("comboBox")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.setStyleSheet("\n""background-color: rgb(255, 255, 255);\n"
        "border:none;\n align: \"center\";\n""font-size: 10pt;\n")

                self.label_step2 = QtWidgets.QLabel()
                self.label_step2.setStyleSheet("align:\"center\";\n"
        "font-size: 10pt;")
                self.label_step2.setObjectName("label_step2")
                self.comboBox2 = QtWidgets.QComboBox(self.widget_6)
                self.comboBox2.setObjectName("comboBox2")
                self.comboBox2.addItem("")
                self.comboBox2.addItem("")
                self.comboBox2.addItem("")
                self.comboBox2.addItem("")
                self.comboBox2.addItem("")
                self.comboBox2.addItem("")
                self.comboBox2.setStyleSheet("\n""background-color: rgb(255, 255, 255);\n"
        "border:none;\n align: \"center\";\n""font-size: 10pt;\n")


                self.label_step3 = QtWidgets.QLabel()
                self.label_step3.setStyleSheet("align:\"center\";\n"
        "font-size: 10pt;")
                self.label_step3.setObjectName("label_step3")
                self.comboBox3 = QtWidgets.QComboBox(self.widget_6)
                self.comboBox3.setObjectName("comboBox2")
                self.comboBox3.addItem("")
                self.comboBox3.addItem("")
                self.comboBox3.addItem("")
                self.comboBox3.addItem("")
                self.comboBox3.addItem("")
                self.comboBox3.addItem("")
                self.comboBox3.setStyleSheet("\n""background-color: rgb(255, 255, 255);\n"
        "border:none;\n align: \"center\";\n""font-size: 10pt;\n")


                integration.addWidget(self.label_step1,0,0)
                integration.addWidget(self.comboBox ,0,1)
                integration.addWidget(self.label_step2,1,0)
                integration.addWidget(self.comboBox2 ,1,1)
                integration.addWidget(self.label_step3,2,0)
                integration.addWidget(self.comboBox3 ,2,1)

                self.Export = QtWidgets.QPushButton(self.groupBox_Spec_integration)
                self.Export.setStyleSheet("border-radius:30px;\n"
        "background-color:rgb(0, 170, 0);\n"
        "font-size:24px;\n"
        "color:#fff;")
                self.Export.setObjectName("Export")
                self.Export.setText("Export")
                sub_groupBox_Spec_integration.addWidget(self.Label_STEP,0,0)
                sub_groupBox_Spec_integration.addWidget(self.widget_6,1,0)
                sub_groupBox_Spec_integration.addWidget(self.Export,2,0)



                self.groupBox_Spec_Wave = QtWidgets.QGroupBox(self.groupBox_Spec)
                self.groupBox_Spec_Wave.setStyleSheet("border-radius: 0px;\n"
        "border: 0px solid black;\nbackground-color: transparent;")
                sub_groupBox_Spec_Wave  = QGridLayout(self.groupBox_Spec_Wave)

                self.Label_Wave = QtWidgets.QLabel(self.groupBox_Spec_Wave)
                self.Label_Wave.setStyleSheet("color:black;\n"
                "border: none;\n" "font-size:14pt bold;\n")
                self.Label_Wave.setObjectName("Label_Wave")

                self.widget_name = QtWidgets.QLineEdit(self.groupBox_Spec_Wave)
                self.widget_name.setStyleSheet("\n"
        "background-color: rgb(255, 255, 255);\n"
        "border: 2px solid black;\n font-size:14pt bold;\n")
                self.widget_name.setObjectName("widget_name")
                self.widget_name.move(0, 200)
                self.widget_name.resize(295,40)

                sub_groupBox_Spec_Wave.addWidget(self.Label_Wave,0,0)
                # sub_groupBox_Spec_Wave.addWidget(self.widget_name,1,0)

                # sub_groupBox_Spec_Wave(200)
                sub_GridSpec.addWidget(self.groupBox_Spec_integration,0,0)
                sub_GridSpec.addWidget(self.groupBox_Spec_Wave,1,0)
                # sub_GridSpec.addWidget(self.widget_name,3,0)


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
                self.Label_STEP.setAlignment(QtCore.Qt.AlignCenter)
                self.Label_Wave.setAlignment(QtCore.Qt.AlignCenter)
                # scroll.setFixedHeight(960)
                # scroll.setFixedWidth(1280)
                self.box.addWidget(scroll)
                self.pushButton_3.clicked.connect(self.close)
                # self.retranslateUi(MainWindow)

        
        
        # # def setIcon(self):
        # #         appIcon = QIcon("icon.png")
        # #         MainWindow.setWindowIcon(appIcon)
        # def retranslateUi(self, MainWindow):
        #     _translate = QtCore.QCoreApplication.translate
                self.Label.setText("Pre-Processing")
                self.Topic_RAW.setText("RAW")
                self.label_RAW.setText("...")
                self.Topic_SNV.setText("SNV")
                self.label_SNV.setText("...")
                self.Topic_MSC.setText("MSC")
                self.label_MSC.setText("...")
                self.Topic_2ndDerivative.setText("2nd Derivative")
                self.label_2ndDeri.setText("...")
                self.label_1stDeri.setText("...")
                self.label_Smoothing.setText("...")

                self.grab_Smoothing.setText("Gab")
                self.Seg_Smoothing.setText("Segment")
                self.Topic_Smoothing.setText("Smoothing size")

                self.label_24.setText("Gab")
                self.Seg_2nd.setText("Segment")
                self.Topic_1stDerivative.setText("1st Derivative")
                self.label_22.setText("Gab")
                self.Seg_1st.setText("Segment")

                self.Label_STEP.setText("CALCULATION STEP")
                self.label_step1.setText("Step 1")
                self.comboBox.setItemText(0, "---select---")
                self.comboBox.setItemText(1, "RAW")
                self.comboBox.setItemText(2, "SNV")
                self.comboBox.setItemText(3, "MSC")
                self.comboBox.setItemText(4, "1st Derivative")
                self.comboBox.setItemText(5,"2nd Derivative")
                self.label_step2.setText("Step 2")
                self.comboBox2.setItemText(0,"---select---")
                self.comboBox2.setItemText(1,"RAW")
                self.comboBox2.setItemText(2,"SNV")
                self.comboBox2.setItemText(3,"MSC")
                self.comboBox2.setItemText(4,"1st Derivative")
                self.comboBox2.setItemText(5,"2nd Derivative")

                self.label_step3.setText("Step 3")
                self.comboBox3.setItemText(0,"---select---")
                self.comboBox3.setItemText(1, "RAW")
                self.comboBox3.setItemText(2,"SNV")
                self.comboBox3.setItemText(3, "MSC")
                self.comboBox3.setItemText(4,"1st Derivative")
                self.comboBox3.setItemText(5,"2nd Derivative")

                self.Label_Wave.setText("Username")
                self.widget_name.setText("Type your name...")
                self.pushButton_3.setText("CANCEL")
                self.pushButton_4.setText("APPLY")
        

if __name__ == '__main__':
        app = QApplication(sys.argv)
        myapp = Ui_MainWindow()
        myapp.show()
        sys.exit(app.exec_())