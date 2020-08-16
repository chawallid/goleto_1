from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Pre-Processing")
        MainWindow.resize(1800, 1200)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:5px;\n"
"")     
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 1800, 1200))
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)

        # self.error_dialog = QtWidgets.QErrorMessage(self.centralwidget)

        self.widget.setGeometry(QtCore.QRect(30, 40, 900, 900)) #snv...
        self.widget.setStyleSheet("  border-radius: 5px;\n"
"  border: 0px solid;\n"
"background-color: rgb(153, 153, 153);\n"
"font-size: 10pt;\n"
"\n"
"")
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(10, 20, 111, 61))
        # self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")

        self.btnApply = QtWidgets.QPushButton(self.centralwidget)
        self.btnApply.setGeometry(QtCore.QRect(10, 60, 111, 61))
        # self.btnBack.setFont(font)
        self.btnApply.setObjectName("btnApply")

        self.widget.setObjectName("widget")
        self.widget_10 = QtWidgets.QWidget(self.widget)
        self.widget_10.setGeometry(QtCore.QRect(100, 100, 700, 80)) #WidgetRAW
        self.widget_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_10.setObjectName("widget_10")

        self.label_12 = QtWidgets.QLabel(self.widget_10)
        self.label_12.setGeometry(QtCore.QRect(50, 30, 100, 20)) #LabelRAW
        self.label_12.setObjectName("label_12")

        self.label_RAW = QtWidgets.QLabel(self.widget_10)
        self.label_RAW.setGeometry(QtCore.QRect(150, 30, 100, 20)) #LabelRAW
        self.label_RAW.setObjectName("label_RAW")

        self.widget_11 = QtWidgets.QWidget(self.widget)
        self.widget_11.setGeometry(QtCore.QRect(100, 200, 700, 80)) #WidgeSNV
        self.widget_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_11.setObjectName("widget_11")

        self.label_13 = QtWidgets.QLabel(self.widget_11)
        self.label_13.setGeometry(QtCore.QRect(50, 30, 80, 30)) #LabelSNV
        self.label_13.setStyleSheet("align:\"center\"")
        self.label_13.setObjectName("label_13")

        self.label_SNV = QtWidgets.QLabel(self.widget_11)
        self.label_SNV.setGeometry(QtCore.QRect(150, 30, 80, 30)) #LabelSNV
        self.label_SNV.setObjectName("label_SNV")

        self.widget_12 = QtWidgets.QWidget(self.widget)
        self.widget_12.setGeometry(QtCore.QRect(100, 300, 700, 80)) #WidgetMSC
        self.widget_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_12.setObjectName("widget_12")

        self.label_14 = QtWidgets.QLabel(self.widget_12)
        self.label_14.setGeometry(QtCore.QRect(50, 30, 80, 30)) #LabelMSC
        self.label_14.setStyleSheet("align:\"center\"")
        self.label_14.setObjectName("label_14")

        self.label_MSC = QtWidgets.QLabel(self.widget_12)
        self.label_MSC.setGeometry(QtCore.QRect(150, 30, 80, 30)) #LabelSNV
        self.label_MSC.setObjectName("label_MSC")

        self.widget_14 = QtWidgets.QWidget(self.widget)
        self.widget_14.setGeometry(QtCore.QRect(100, 570, 700, 100)) #2ndDeri
        self.widget_14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_14.setObjectName("widget_14")

        self.label_16 = QtWidgets.QLabel(self.widget_14)
        self.label_16.setGeometry(QtCore.QRect(50, 30, 250, 30)) #2ndDeri
        self.label_16.setStyleSheet("align:\"center\"")
        self.label_16.setObjectName("label_16")

        self.label_2ndDeri = QtWidgets.QLabel(self.widget_14)
        self.label_2ndDeri.setGeometry(QtCore.QRect(150, 30, 250, 30)) #2ndDeri
        self.label_2ndDeri.setStyleSheet("align:\"center\"")
        self.label_2ndDeri.setObjectName("label_2ndDeri")


        self.spinBox = QtWidgets.QSpinBox(self.widget_14)
        self.spinBox.setGeometry(QtCore.QRect(385, 40, 80, 40)) #Gab2ndB
        self.spinBox.setStyleSheet("color:rgb(0, 0, 0);\n"
"\n"
"")
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.widget_14)
        self.label.setGeometry(QtCore.QRect(370, 10, 50, 30)) #Gab2ndL
        self.label.setObjectName("label")




        self.spinBox_2 = QtWidgets.QSpinBox(self.widget_14)
        self.spinBox_2.setGeometry(QtCore.QRect(565, 40, 80, 40)) #Segment2ndB
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_6 = QtWidgets.QLabel(self.widget_14)
        self.label_6.setGeometry(QtCore.QRect(530, 10, 120, 30)) #Segment2ndL
        self.label_6.setObjectName("label_6")
        self.widget_15 = QtWidgets.QWidget(self.widget)
        self.widget_15.setGeometry(QtCore.QRect(100, 690, 700, 100)) #smoothW
        self.widget_15.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_15.setObjectName("widget_15")
        self.label_17 = QtWidgets.QLabel(self.widget_15)
        self.label_17.setGeometry(QtCore.QRect(50, 25, 200, 30)) #smoothL
        self.label_17.setStyleSheet("align:\"center\"")
        self.label_17.setObjectName("label_17")
        self.spinBox_3 = QtWidgets.QSpinBox(self.widget_15)
        self.spinBox_3.setGeometry(QtCore.QRect(385, 40, 80, 40)) #GabSmoothB
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(self.widget_15)
        self.spinBox_4.setGeometry(QtCore.QRect(565, 40, 80, 40)) #SegSmoothB
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_2 = QtWidgets.QLabel(self.widget_15)
        self.label_2.setGeometry(QtCore.QRect(370, 10, 50, 30)) #GabSmoothL
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.widget_15)
        self.label_7.setGeometry(QtCore.QRect(530, 10, 120, 30)) #SegSmoothL
        self.label_7.setObjectName("label_7")

        self.widget_18 = QtWidgets.QWidget(self.widget)
        self.widget_18.setGeometry(QtCore.QRect(100, 450, 700, 100)) #1stDeri
        self.widget_18.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_18.setObjectName("widget_18")
        self.label_19 = QtWidgets.QLabel(self.widget_18)
        self.label_19.setGeometry(QtCore.QRect(50, 25, 250, 50)) #1stDeri
        self.label_19.setStyleSheet("align:\"center\"")
        self.label_19.setObjectName("label_19")

        self.label_1stDeri = QtWidgets.QLabel(self.widget_18)
        self.label_1stDeri.setGeometry(QtCore.QRect(150, 25, 250, 50)) #1stDeri
        self.label_1stDeri.setStyleSheet("align:\"center\"")
        self.label_1stDeri.setObjectName("label_1stDeri")

        self.spinBox_7 = QtWidgets.QSpinBox(self.widget_18)
        self.spinBox_7.setGeometry(QtCore.QRect(385, 40, 80, 40)) #Gab1st
        self.spinBox_7.setStyleSheet(";\n"
"\n"
"")
        self.spinBox_7.setObjectName("spinBox_7")
        self.label_15 = QtWidgets.QLabel(self.widget_18)
        self.label_15.setGeometry(QtCore.QRect(370, 10, 50, 30)) #Gab1stL
        self.label_15.setObjectName("label_15")

        self.spinBox_8 = QtWidgets.QSpinBox(self.widget_18)
        self.spinBox_8.setGeometry(QtCore.QRect(565, 40, 80, 40)) #Segment1st
        self.spinBox_8.setObjectName("spinBox_8")
        self.label_20 = QtWidgets.QLabel(self.widget_18)
        self.label_20.setGeometry(QtCore.QRect(530, 10, 120, 30)) #Gab1st
        self.label_20.setObjectName("label_20")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(960, 40, 810, 570)) #CalculationStep
        self.widget_2.setStyleSheet("border-radius: 5px;\n"
"  background: #73AD21;\n"
"background-color: rgb(153, 153, 153);")
        self.widget_2.setObjectName("widget_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(160, 50, 500, 50)) #CalStepL
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("text-align:\"center\";\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        self.widget_6.setGeometry(QtCore.QRect(100, 200, 600, 80)) #step1W
        self.widget_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_6.setObjectName("widget_6")
        self.label_8 = QtWidgets.QLabel(self.widget_6)
        self.label_8.setGeometry(QtCore.QRect(100, 25, 80, 30)) #Step1L
        self.label_8.setStyleSheet("align:\"center\";\n"
                                   "font-size: 10pt;")
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(self.widget_6)
        self.comboBox.setGeometry(QtCore.QRect(250, 10, 250, 60)) #Step1Sel
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setStyleSheet("align: \"center\";\n"
                                      "font-size: 10pt;\n")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(200, 130, 400, 30)) #SelectL
        self.label_5.setStyleSheet("align:\"center\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.widget_7 = QtWidgets.QWidget(self.widget_2)
        self.widget_7.setGeometry(QtCore.QRect(100, 300, 600, 80)) #Step2W
        self.widget_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_7.setObjectName("widget_7")
        self.label_9 = QtWidgets.QLabel(self.widget_7)
        self.label_9.setGeometry(QtCore.QRect(100, 25, 80, 30)) #Step2L
        self.label_9.setStyleSheet("align:\"center\";\n"
                                   "font-size: 10pt;\n")
        self.label_9.setObjectName("label_9")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_7)
        self.comboBox_2.setGeometry(QtCore.QRect(250, 10, 250, 60)) #step2Sel
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setStyleSheet("align: \"center\";\n"
                                      "font-size: 10pt;\n")
        self.widget_9 = QtWidgets.QWidget(self.widget_2)
        self.widget_9.setGeometry(QtCore.QRect(100, 400, 600, 80)) #step3W
        self.widget_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_9.setObjectName("widget_9")
        self.label_11 = QtWidgets.QLabel(self.widget_9)
        self.label_11.setGeometry(QtCore.QRect(100, 25, 80, 30))
        self.label_11.setStyleSheet("align:\"center\";\n"
                                   "font-size: 10pt;\n")
        self.label_11.setObjectName("label_11")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_9)
        self.comboBox_3.setGeometry(QtCore.QRect(250, 10, 250, 60))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setStyleSheet("align: \"center\";\n"
                                      "font-size: 10pt;\n")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(960, 640, 810, 300)) #name
        self.widget_3.setStyleSheet("border-radius: 5px;\n"
"  background: #73AD21;\n"
"background-color: rgb(153, 153, 153);")
        self.widget_3.setObjectName("widget_3")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(100, 50, 300, 40)) #username
        self.label_4.setStyleSheet("font: 14pt \"Tahoma\";")
        self.label_4.setObjectName("label_4")
        
        self.widget_8 = QtWidgets.QWidget(self.widget_3)
        self.widget_8.setGeometry(QtCore.QRect(100, 100, 600, 80))
        self.widget_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 32pt \"Tahoma\";")
        self.widget_8.setObjectName("widget_8")

       

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 1000, 350, 100))
        self.pushButton_3.setStyleSheet("border-radius:50px;\n"
"background-color:#aa0000;\n"
"font-size:32px;\n"
"color:#fff;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1000, 1000, 350, 100))
        self.pushButton_4.setStyleSheet("border-radius:50px;\n"
"background-color:rgb(0, 170, 0);\n"
"font-size:32px;\n"
"color:#fff;")
        self.pushButton_4.setObjectName("pushButton_4")
        # MainWindow.setCentralWidget(self.centralwidget)

        self.lineEdit = QtWidgets.QLineEdit(self.widget_8)
        self.lineEdit.setGeometry(QtCore.QRect(200, 100, 250, 100)) #boxToTypeUsername
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "Pre-Processing"))
        self.label_12.setText(_translate("MainWindow", "RAW"))
        self.label_RAW.setText(_translate("MainWindow", "..."))
        self.label_13.setText(_translate("MainWindow", "SNV"))
        self.label_SNV.setText(_translate("MainWindow", "..."))
        self.label_14.setText(_translate("MainWindow", "MSC"))
        self.label_MSC.setText(_translate("MainWindow", "..."))
        self.label_16.setText(_translate("MainWindow", "2nd Derivative"))
        self.label_2ndDeri.setText(_translate("MainWindow", "..."))
        self.label_1stDeri.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Gab"))
        self.label_6.setText(_translate("MainWindow", "Segment"))
        self.label_17.setText(_translate("MainWindow", "Smoothing size"))
        self.label_2.setText(_translate("MainWindow", "Gab"))
        self.label_7.setText(_translate("MainWindow", "Segment"))
        self.label_19.setText(_translate("MainWindow", "1st Derivative"))
        self.label_15.setText(_translate("MainWindow", "Gab"))
        self.label_20.setText(_translate("MainWindow", "Segment"))
        self.label_3.setText(_translate("MainWindow", "CALCULATION STEP"))
        self.label_8.setText(_translate("MainWindow", "Step 1"))
        self.comboBox.setItemText(0, _translate("MainWindow", "---select---"))
        self.comboBox.setItemText(1, _translate("MainWindow", "RAW"))
        self.comboBox.setItemText(2, _translate("MainWindow", "SNV"))
        self.comboBox.setItemText(3, _translate("MainWindow", "MSC"))
        self.comboBox.setItemText(4, _translate("MainWindow", "1st Derivative"))
        self.comboBox.setItemText(5, _translate("MainWindow", "2nd Derivative"))

        self.label_5.setText(_translate("MainWindow", "Select Your Step to Calculate"))
        self.label_9.setText(_translate("MainWindow", "Step 2"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "---select---"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "RAW"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "SNV"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "MSC"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "1st Derivative"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "2nd Derivative"))

        self.label_11.setText(_translate("MainWindow", "Step 3"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "---select---"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "RAW"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "SNV"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "MSC"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "1st Derivative"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "2nd Derivative"))
        self.label_4.setText(_translate("MainWindow", "Username"))
        self.lineEdit.setText(_translate("MainWindow", "Type your name..."))
        self.pushButton_3.setText(_translate("MainWindow", "CANCEL"))
        self.pushButton_4.setText(_translate("MainWindow", "APPLY"))
        self.btnBack.setText(_translate("MainWindow", "Back"))
        self.btnApply.setText(_translate("MainWindow", "Apply"))




# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
