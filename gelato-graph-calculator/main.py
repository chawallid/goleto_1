import sys

from matplotlib.backends.backend_pdf import PdfPages

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from fpdf import FPDF
import os,glob

from PyQt5.QtWidgets import QMainWindow , QScrollArea,QApplication , QWidget , QVBoxLayout, QPushButton, QGroupBox, QGridLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtCore, QtGui, QtWidgets

import time
from datetime import datetime

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from dashborad import Ui_MainWindow as Ui_Dashborad
from prepro import Ui_MainWindow as Ui_Prepro
from SystemConfig import Ui_MainWindow as Ui_SystemConfig
from calculateprogram.code_python import FirstDev,SecondDev,meancen2,snv,msc 

file_1 = ""
file_2 = ""
file_3 = ""
file_4 = ""
file_5 = ""
graph = None
clickStart = False
result1 = []
result2 = []
result3 = []
result4 = []
result5 = []
file_spec = []
date_arr = []
count_graph = 0
x_coordinates1 = []
x_coordinates2 = []
x_coordinates3 = []
x_coordinates4 = []
x_coordinates5 = []
list_tmp1 = []
for j in range(225):
    list_tmp1.append([0])
list_tmp2 = []
for j in range(225):
    list_tmp2.append([0])
list_tmp3 = []
for j in range(225):
    list_tmp3.append([0])
list_tmp4 = []
for j in range(225):
    list_tmp4.append([0])
list_tmp5 = []
for j in range(225):
    list_tmp5.append([0])

global meanC,snv_data,mscval,smooth

global wave,x,s,g,sd1,sd2

global wave_1,x_1,s_1,g_1,sd1_1,sd2_1 
global wave_2,x_2,s_2,g_2,sd1_2,sd2_2
global wave_3,x_3,s_3,g_3,sd1_3,sd2_3
global wave_4,x_4,s_4,g_4,sd1_4,sd2_4
global wave_5,x_5,s_5,g_5,sd1_5,sd2_5


class MyApp(QMainWindow):
    def __init__(self, parent=None):
            QWidget.__init__(self, parent)

            self.dashborad = Ui_Dashborad()
            self.dashborad.show()
            self.prepro =  Ui_Prepro()
            self.prepro.hide()
            self.systemconfig = Ui_SystemConfig()
            self.systemconfig.hide()
            self.setupUi()

            self.timer = QtCore.QTimer()
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.recurring_timer)
            self.timer.start()

    def recurring_timer(self):
        global clickStart,wave_1,x,x_1,sd,sd1_1,result1,count_graph,smooth
        global x_coordinates1,list_tmp1
        global x_coordinates2,list_tmp2
        global x_coordinates3,list_tmp3
        global x_coordinates4,list_tmp4
        global x_coordinates5,list_tmp5
        global result2,result3,result4,result5

        global wave_2,x_2,s_2,g_2,sd1_2,sd2_2
        global wave_3,x_3,s_3,g_3,sd1_3,sd2_3
        global wave_4,x_4,s_4,g_4,sd1_4,sd2_4
        global wave_5,x_5,s_5,g_5,sd1_5,sd2_5
        global file_spec
        now = datetime.now()
        # date_arr.append(now)

        current_time = now.strftime("%d %B %Y  %H:%M:%S")
        self.dashborad.dateNtime.setText(current_time)
        self.dashborad.tabWidget.setTabText(0, self.dashborad.label_result1.text())
        self.dashborad.tabWidget.setTabText(1, self.dashborad.label_result2.text())
        self.dashborad.tabWidget.setTabText(2, self.dashborad.label_result3.text())
        self.dashborad.tabWidget.setTabText(3, self.dashborad.label_result4.text())
        self.dashborad.tabWidget.setTabText(4, self.dashborad.label_result5.text())
        if(clickStart):

            if(file_1 != ""):
                print("file_1")
                f = open(file_spec[count_graph], "r")
                line = 0
                X = []
                for x in f:
                    if(line >= 8):
                        if(x == "\n"):
                            continue;
                        tmp = x.split(";")
                        X.append([float(tmp[4])])
                    line+=1
                f.close()
                if(count_graph < len(X)):
                    B = x_1
                    # x = x_1
                    X = np.array(X)
                    steps = [self.prepro.comboBox.currentText(),self.prepro.comboBox2.currentText(),self.prepro.comboBox3.currentText()]
                    print("steps :",steps)
                    print("Data from file calibrate :",B.shape)
                    print("Data from specific folder :",X.shape)
                    result = X.dot(B)
                    print("X[",count_graph,"].dot(B) :",result.shape)
                    for step in steps :
                        if step == "1st Derivative":
                            s = s_1
                            g = g_1
                            self.FirstDev()
                            print("1st Derivative shape :" , sd1.shape)
                            # print("1st Derivative data :" , sd1)
                            result = result*(sd1)

                        elif step == "2nd Derivative":
                            s = s_2
                            g = g_2
                            self.SecondDev()
                            print("2nd Derivative shape :" , sd2.shape)
                            # print("2nd Derivative data :" , sd2)
                            result = result*(sd2)
                            
                        elif step == "RAW":
                            print("RAW shape :" , B.transpose().shape)
                            # print("RAW data :" , x.transpose())
                            result = result*(B.transpose())
                            
                        elif step == "SNV":
                            self.snv()
                            print("snv_data shape:",snv_data.shape)
                            # print("snv_data data :",snv_data)
                            result = result*(snv_data)

                        elif step == "MSC":
                            sp = x
                            nos = x.shape[0]
                            wave = x.shape[1]
                            meansp=np.mean(sp,axis=0)
                            lbd=np.array(range(0,wave))
                            Ym=np.polyfit(lbd,meansp,1)
                            slopem=Ym[0]
                            interm=Ym[1]
                            Y=np.zeros([nos,2])
                            for i in range(0,nos):
                                Y[i,:]=np.polyfit(lbd,sp[i,:],1)
                            slope=np.tile(Y[:,0],(wave,1)).T
                            inter=np.tile(Y[:,1],(wave,1)).T
                            spmsc=(sp - inter) / slope
                            spmsc=np.multiply(spmsc,slopem) + np.tile(interm,(nos,wave))
                            
                            nos = x.shape[0]
                            wave = x.shape[1]
                            meansp=np.mean(sp,axis=0)
                            lbd=np.array(range(0,wave))
                            
                            Ym=np.polyfit(lbd,meansp,1)
                            mscval=np.copy(Ym)
                            slopem=Ym[0]
                            interm=Ym[1]
                            Y=np.zeros([nos,2])
                            for i in range(0,nos):
                                Y[i,:]=np.polyfit(lbd,sp[i,:],1)
                            slope=np.tile(Y[:,0],(wave,1)).T
                            inter=np.tile(Y[:,1],(wave,1)).T
                            spmsc=(sp - inter) / slope
                            spmsc=np.multiply(spmsc,slopem) + np.tile(interm,(nos,wave))
                            result = mscval
                            print("MSC shape :" , result)

                        elif step == "Smoothing Size":
                            self.smooth_x()
                            print("smooth_x shape:",smooth.shape)
                            result = result*(smooth)
                        

                    print("B shape :" , B.shape ,"bias :" , int(self.systemconfig.spinBox_4.value()))
                    print("before cal result :", result.shape)  
                    result = (result*(B)) + int(self.systemconfig.spinBox_4.value())
                    print("after cal result  :", result.shape)              
                    # print("result :", result)
                    result1 = result[0]
                    # print(result[0][0])
                    # print(np.prod(result[1].shape))
                    self.dashborad.result1.setText(str(result))

                    self.dashborad.figure.clear()
                    ax2 = self.dashborad.figure.add_subplot(111)
                    test = result1
                    x_coordinates1.append(count_graph)
                    for j in range(225):
                        if (count_graph == 0 ):
                            list_tmp1[j] = [test[j]]
                        else:
                            list_tmp1[j].append(test[j])
                        ax2.plot(x_coordinates1, list_tmp1[j])

                    ax2.set_xlabel('wavelenght, nm')
                    ax2.set_ylabel('log 1/R')
                    self.dashborad.canvas.draw()
                    print("draw 1 succ !!")

            if(file_2 != ""):
                if(count_graph < np.prod(result2[0].shape)):
                    wave = wave_2
                    self.dashborad.figure1.clear()
                    ax2 = self.dashborad.figure1.add_subplot(111)
                    test = result2
                    x_coordinates2.append(count_graph)
                    for j in range(225):
                        if (count_graph == 0 ):
                            list_tmp2[j] = [test[count_graph][j]]
                        else:
                            list_tmp2[j].append(test[count_graph][j])
                        ax2.plot(x_coordinates2, list_tmp2[j])

                    ax2.set_xlabel('wavelenght, nm')
                    ax2.set_ylabel('log 1/R')
                    self.dashborad.canvas1.draw()
            if(file_3 != ""):
                if(count_graph < np.prod(result3[0].shape)):
                    # print("111")
                    wave = wave_3
                    self.dashborad.figure2.clear()
                    ax2 = self.dashborad.figure2.add_subplot(111)
                    test = result3
                    x_coordinates3.append(count_graph)
                    for j in range(225):
                        if (count_graph == 0 ):
                            list_tmp3[j] = [test[count_graph][j]]
                        else:
                            list_tmp3[j].append(test[count_graph][j])
                        ax2.plot(x_coordinates3, list_tmp3[j])

                    ax2.set_xlabel('wavelenght, nm')
                    ax2.set_ylabel('log 1/R')
                    self.dashborad.canvas2.draw()

            if(file_4 != ""):
                if(count_graph < np.prod(result4[0].shape)):
                    wave = wave_4
                    self.dashborad.figure3.clear()
                    ax2 = self.dashborad.figure3.add_subplot(111)
                    test = result4
                    x_coordinates4.append(count_graph)
                    for j in range(225):
                        if (count_graph == 0 ):
                            list_tmp4[j] = [test[count_graph][j]]
                        else:
                            list_tmp4[j].append(test[count_graph][j])
                        ax2.plot(x_coordinates4, list_tmp4[j])

                    ax2.set_xlabel('wavelenght, nm')
                    ax2.set_ylabel('log 1/R')
                    self.dashborad.canvas3.draw()

            if(file_5 != ""):
                if(count_graph < np.prod(result5[0].shape)):
                    wave = wave_5
                    self.dashborad.figure4.clear()
                    ax2 = self.dashborad.figure4.add_subplot(111)
                    test = result5
                    x_coordinates5.append(count_graph)
                    for j in range(225):
                        if (count_graph == 0 ):
                            list_tmp5[j] = [test[count_graph][j]]
                        else:
                            list_tmp5[j].append(test[count_graph][j])
                        ax2.plot(x_coordinates5, list_tmp5[j])

                    ax2.set_xlabel('wavelenght, nm')
                    ax2.set_ylabel('log 1/R')
                    self.dashborad.canvas4.draw()

            count_graph = count_graph + 1

    def setupUi(self):
        self.dashborad.buttonSysConfig.clicked.connect(self.systemconfig.show)
        self.dashborad.buttonSysConfig.clicked.connect(self.dashborad.hide)

        self.dashborad.buttonPrePro.clicked.connect(self.prepro.show)
        self.dashborad.buttonPrePro.clicked.connect(self.dashborad.hide)

        # self.prepro.btnBack.clicked.connect(self.prepro.centralwidget.hide)
        # self.prepro.btnBack.clicked.connect(self.dashborad.centralwidget.show)

        self.prepro.pushButton_3.clicked.connect(self.prepro.hide)
        self.prepro.pushButton_3.clicked.connect(self.dashborad.show)
        
        self.systemconfig.pushButton_3.clicked.connect(self.systemconfig.hide)
        self.systemconfig.pushButton_3.clicked.connect(self.dashborad.show)


        self.systemconfig.btn_Upload.clicked.connect(self.specific)
        # self.systemconfig.btnBack.clicked.connect(self.systemconfig.centralwidget.hide)
        # self.systemconfig.btnBack.clicked.connect(self.dashborad.centralwidget.show)

        self.systemconfig.btn1.clicked.connect(self.getbtn1)
        self.systemconfig.btn2.clicked.connect(self.getbtn2)
        self.systemconfig.btn3.clicked.connect(self.getbtn3)
        self.systemconfig.btn4.clicked.connect(self.getbtn4)
        self.systemconfig.btn5.clicked.connect(self.getbtn5)

        self.dashborad.START.clicked.connect(self.getWave)
        
        self.dashborad.STOP.clicked.connect(self.getApply)

        self.systemconfig.pushButton_4.clicked.connect(self.getApply)
        self.prepro.pushButton_4.clicked.connect(self.getPrepair)

        # self.systemconfig.btnApply.clicked.connect(self.getApply)
        # self.prepro.btnApply.clicked.connect(self.getPrepair)

        # self.setInterval(self ,10, self.hello, 'world!')
        # self.prepro.btnApply.clicked.connect(self.getPDF)
    def specific(self):
        global file_spec
        myPath = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        
        file_spec = []
        for txtfile in glob.glob(os.path.join(myPath, '*.txt')):
            file_spec.append(txtfile)
        print("specific path:",myPath,",numbers :",len(file_spec))

    def getPrepair(self):
        print("[func] : getPrepair")

        global g_1,g_2,s_1,s_2
        g_1 = int(self.prepro.spinBox_7.value())
        g_2 = int(self.prepro.spinBox_Seg_1st.value())
        # print("1st :" , g_1 , g_2)
        s_1 = int(self.prepro.spinBox_8.value())
        s_2 = int(self.prepro.spinBox_Seg_2nd.value())

       
        print("1st :" , g_1 , s_1)
        print("2nd :" , s_2 , g_2)

        self.prepro.hide()
        self.dashborad.show()
    
    def getbtn1(self):
        print()
        global file_1
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file','c:/', "files (*.csv)")
        imagePath = fname[0]
        file_1 = fname[0]
        file_tmp = imagePath.split("/")
        self.systemconfig.label_1_.setText(file_tmp[len(file_tmp)-1])

    def getbtn2(self):
        global file_2
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file','c:/', "files (*.csv)")
        imagePath = fname[0]
        file_2 = fname[0]
        file_tmp = imagePath.split("/")
        self.systemconfig.label_2_.setText(file_tmp[len(file_tmp)-1])

    def getbtn3(self):
        global file_3
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:/', "files (*.csv)")
        imagePath = fname[0]
        file_3 = fname[0]
        file_tmp = imagePath.split("/")
        self.systemconfig.label_3_.setText(file_tmp[len(file_tmp)-1])

    def getbtn4(self):
        global file_4
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file','c:/', "files (*.csv)")
        imagePath = fname[0]
        file_4 = fname[0]
        file_tmp = imagePath.split("/")
        self.systemconfig.label_4_.setText(file_tmp[len(file_tmp)-1])

    def getbtn5(self):
        global file_5
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file','c:/', "files (*.csv)")
        imagePath = fname[0]
        file_5 = fname[0]
        file_tmp = imagePath.split("/")
        self.systemconfig.label_5_.setText(file_tmp[len(file_tmp)-1])

    def getPDF(self):
        global wave,x,s,g,sd1,sd2,meanC,snv_data,mscval
        print(self.prepro.comboBox.currentText())
        print(self.prepro.comboBox_2.currentText())
        print(self.prepro.comboBox_3.currentText())
        arr = [self.prepro.comboBox.currentText(),self.prepro.comboBox_2.currentText(),self.prepro.comboBox_3.currentText()]
        with PdfPages('exportPDF.pdf') as pdf:
            for files in arr :
                print(files)
                if files == "RAW":
                    pdf.savefig(self.dashborad.figure)
                elif files == "SNV":
                    pdf.savefig(self.dashborad.figure1)
                elif files == "MSC":
                    pdf.savefig(self.dashborad.figure2)
                elif files == "1st Derivative":
                    pdf.savefig(self.dashborad.figure3)
                elif files == "2nd Derivative":
                    print("2nd Derivative")
                else: 
                    pdf.savefig()
        self.prepro.hide()
        self.dashborad.show()
                
        

    
    def clickMethod(self):
        QMessageBox.about(self, "Title", "Message")

    def getApply(self):

        print("[func] : getApply")
        global file_1,file_2,file_3,file_4,file_5
        global wave_1,x_1,s_1,g_1,sd1_1,sd2_1
        global wave_2,x_2,s_2,g_2,sd1_2,sd2_2
        global wave_3,x_3,s_3,g_3,sd1_3,sd2_3
        global wave_4,x_4,s_4,g_4,sd1_4,sd2_4
        global wave_5,x_5,s_5,g_5,sd1_5,sd2_5

        global x_coordinates1,list_tmp1
        global x_coordinates2,list_tmp2
        global x_coordinates3,list_tmp3
        global x_coordinates4,list_tmp4
        global x_coordinates5,list_tmp5
        global result1,result2,result3,result4,result5
        global count_graph,clickStart


        clickStart = False

        result1 = []
        result2 = []
        result3 = []
        result4 = []
        result5 = []


        count_graph = 0
        x_coordinates1 = []
        x_coordinates2 = []
        x_coordinates3 = []
        x_coordinates4 = []
        x_coordinates5 = []
        list_tmp1 = []
        for j in range(225):
            list_tmp1.append([0])
        list_tmp2 = []
        for j in range(225):
            list_tmp2.append([0])
        list_tmp3 = []
        for j in range(225):
            list_tmp3.append([0])
        list_tmp4 = []
        for j in range(225):
            list_tmp4.append([0])
        list_tmp5 = []
        for j in range(225):
            list_tmp5.append([0])

        if(file_1 != ""):
            print(file_1)
            X = pd.read_csv(file_1, header = None)
            # print(X)
            # wl = pd.read_excel(file_1, sheet_name='wl', header = None)
            # wave_1 = np.array(0).reshape(-1)
            x_1 = np.array(X)
            # print(x_1)
            # x = x_1

        if(file_2 != ""):
            print(file_2)
            X = pd.read_excel(file_2, sheet_name='X', header = None)
            wl = pd.read_excel(file_2, sheet_name='wl', header = None)
            wave_2 = np.array(wl).reshape(-1)
            x_2 = np.array(X)
           

        if(file_3 != ""):
            print(file_3)
            X = pd.read_excel(file_3, sheet_name='X', header = None)
            wl = pd.read_excel(file_3, sheet_name='wl', header = None)
            wave_3 = np.array(wl).reshape(-1)
            x_3 = np.array(X)

        if(file_4 != ""):
            print(file_4)
            X = pd.read_excel(file_4, sheet_name='X', header = None)
            wl = pd.read_excel(file_4, sheet_name='wl', header = None)
            wave_4 = np.array(wl).reshape(-1)
            x_4 = np.array(X)
          
            
        if(file_5 != ""):
            print(file_5)
            X = pd.read_excel(file_5, sheet_name='X', header = None)
            wl = pd.read_excel(file_5, sheet_name='wl', header = None)
            wave_5 = np.array(wl).reshape(-1)
            x_5 = np.array(X)


        self.systemconfig.hide()
        self.dashborad.show()

    def getWave(self ):
        global clickStart
        clickStart = True 
        print("[func] : getWave")

        global file_1,file_2,file_3,file_4,file_5,meanC,snv_data,mscval
        global graph 
        global wave,x,s,g,sd1,sd2,result1
        global result2,result3,result4,result5
        global wave_1,x_1,s_1,g_1,sd1_1,sd2_1
        global wave_2,x_2,s_2,g_2,sd1_2,sd2_2
        global wave_3,x_3,s_3,g_3,sd1_3,sd2_3
        global wave_4,x_4,s_4,g_4,sd1_4,sd2_4
        global wave_5,x_5,s_5,g_5,sd1_5,sd2_5


        s = 0
        g = 0

        if(file_2 != ""):
            wave = wave_2
            print("file_2")
            x = x_2
            # files = self.systemconfig.comboBox_2.currentText()
            steps = [self.prepro.comboBox.currentText(),self.prepro.comboBox2.currentText(),self.prepro.comboBox3.currentText()]
            result = x_2
            fristLoop = True
            for files in steps :
                if files == "1st Derivative":
                    s = s_1
                    g = g_1
                    self.FirstDev()
                    print("1st Derivative shape :" , sd1.shape)
                    print("1st Derivative data :" , sd1)
                    result = result.dot(sd1)

                elif files == "2nd Derivative":
                    s = s_2
                    g = g_2
                    self.SecondDev()
                    print("2nd Derivative shape :" , sd2.shape)
                    print("2nd Derivative data :" , sd2)
                    result = result.dot(sd2)
                    
                elif files == "RAW":
                    print("RAW shape :" , x.transpose().shape)
                    print("RAW data :" , x.transpose())
                    result = result.dot(x.transpose())
                    
                elif files == "SNV":
                    self.snv()
                    print("snv_data shape:",snv_data.shape)
                    print("snv_data data :",snv_data)
                    result = result.dot(snv_data)

                elif files == "MSC":
                    sp = x
                    nos = x.shape[0]
                    wave = x.shape[1]
                    meansp=np.mean(sp,axis=0)
                    lbd=np.array(range(0,wave))
                    Ym=np.polyfit(lbd,meansp,1)
                    slopem=Ym[0]
                    interm=Ym[1]
                    Y=np.zeros([nos,2])
                    for i in range(0,nos):
                        Y[i,:]=np.polyfit(lbd,sp[i,:],1)
                    slope=np.tile(Y[:,0],(wave,1)).T
                    inter=np.tile(Y[:,1],(wave,1)).T
                    spmsc=(sp - inter) / slope
                    spmsc=np.multiply(spmsc,slopem) + np.tile(interm,(nos,wave))
                    
                    nos = x.shape[0]
                    wave = x.shape[1]
                    meansp=np.mean(sp,axis=0)
                    lbd=np.array(range(0,wave))
                    
                    Ym=np.polyfit(lbd,meansp,1)
                    mscval=np.copy(Ym)
                    slopem=Ym[0]
                    interm=Ym[1]
                    Y=np.zeros([nos,2])
                    for i in range(0,nos):
                        Y[i,:]=np.polyfit(lbd,sp[i,:],1)
                    slope=np.tile(Y[:,0],(wave,1)).T
                    inter=np.tile(Y[:,1],(wave,1)).T
                    spmsc=(sp - inter) / slope
                    spmsc=np.multiply(spmsc,slopem) + np.tile(interm,(nos,wave))
                    result = mscval
                    print("MSC shape :" , result)
                else: 
                    print("other")

            print("x_2 shape :" , x_2.shape)
            print("bias :" , int(self.systemconfig.spinBox_5.value()))
            result = (result.dot(x_2)) + int(self.systemconfig.spinBox_5.value())
            print("result shape :", result.shape)              
            print("result :", result)
            result2 = result
            self.dashborad.result2.setText(str(int(result[0][0])))

            self.dashborad.figure1.clear()
            ax2 = self.dashborad.figure1.add_subplot(111)
            ax2.set_xlabel('wavelenght, nm')
            ax2.set_ylabel('log 1/R')
            ax2.set_xlim(np.min(wave),np.max(wave))
            self.dashborad.canvas1.draw()
            print("draw succ2")

        if(file_3 != ""):
            print("file_3")
            wave = wave_3
            x = x_3
            steps = [self.prepro.comboBox.currentText(),self.prepro.comboBox2.currentText(),self.prepro.comboBox3.currentText()]
            result = x_3
            fristLoop = True
            for files in steps :
                if files == "1st Derivative":
                    s = s_1
                    g = g_1
                    self.FirstDev()
                    print("1st Derivative shape :" , sd1.shape)
                    print("1st Derivative data :" , sd1)
                    result = result.dot(sd1)

                elif files == "2nd Derivative":
                    s = s_2
                    g = g_2
                    self.SecondDev()
                    print("2nd Derivative shape :" , sd2.shape)
                    print("2nd Derivative data :" , sd2)
                    result = result.dot(sd2)
                    
                elif files == "RAW":
                    print("RAW shape :" , x.transpose().shape)
                    print("RAW data :" , x.transpose())
                    result = result.dot(x.transpose())
                    
                elif files == "SNV":
                    self.snv()
                    print("snv_data shape:",snv_data.shape)
                    print("snv_data data :",snv_data)
                    result = result.dot(snv_data)

                elif files == "MSC":
                    sp = x
                    nos = x.shape[0]
                    wave = x.shape[1]
                    meansp=np.mean(sp,axis=0)
                    lbd=np.array(range(0,wave))
                    Ym=np.polyfit(lbd,meansp,1)
                    slopem=Ym[0]
                    interm=Ym[1]
                    Y=np.zeros([nos,2])
                    for i in range(0,nos):
                        Y[i,:]=np.polyfit(lbd,sp[i,:],1)
                    slope=np.tile(Y[:,0],(wave,1)).T
                    inter=np.tile(Y[:,1],(wave,1)).T
                    spmsc=(sp - inter) / slope
                    spmsc=np.multiply(spmsc,slopem) + np.tile(interm,(nos,wave))
                    
                    nos = x.shape[0]
                    wave = x.shape[1]
                    meansp=np.mean(sp,axis=0)
                    lbd=np.array(range(0,wave))
                    
                    Ym=np.polyfit(lbd,meansp,1)
                    mscval=np.copy(Ym)
                    slopem=Ym[0]
                    interm=Ym[1]
                    Y=np.zeros([nos,2])
                    for i in range(0,nos):
                        Y[i,:]=np.polyfit(lbd,sp[i,:],1)
                    slope=np.tile(Y[:,0],(wave,1)).T
                    inter=np.tile(Y[:,1],(wave,1)).T
                    spmsc=(sp - inter) / slope
                    spmsc=np.multiply(spmsc,slopem) + np.tile(interm,(nos,wave))
                    result = mscval
                    print("MSC shape :" , result)
                else: 
                    print("other")

            print("x_3 shape :" , x_3.shape)
            print("bias :" , int(self.systemconfig.spinBox_6.value()))
            result = (result.dot(x_3)) + int(self.systemconfig.spinBox_6.value())
            print("result shape :", result.shape)              
            print("result :", result)
            result3 = result
            self.dashborad.result3.setText(str(int(result[0][0])))

            self.dashborad.figure2.clear()
            ax2 = self.dashborad.figure2.add_subplot(111)
            ax2.set_xlabel('wavelenght, nm')
            ax2.set_ylabel('log 1/R')
            ax2.set_xlim(np.min(wave),np.max(wave))

            self.dashborad.canvas2.draw()
            print("draw succ3")

        if(file_4 != ""):
            print("file_4")
            wave = wave_4
            x = x_4
            steps = [self.prepro.comboBox.currentText(),self.prepro.comboBox2.currentText(),self.prepro.comboBox3.currentText()]
            result = x_4
            fristLoop = True
            for files in steps :
                if files == "1st Derivative":
                    s = s_1
                    g = g_1
                    self.FirstDev()
                    print("1st Derivative shape :" , sd1.shape)
                    print("1st Derivative data :" , sd1)
                    result = result.dot(sd1)

                elif files == "2nd Derivative":
                    s = s_2
                    g = g_2
                    self.SecondDev()
                    print("2nd Derivative shape :" , sd2.shape)
                    print("2nd Derivative data :" , sd2)
                    result = result.dot(sd2)
                    
                elif files == "RAW":
                    print("RAW shape :" , x.transpose().shape)
                    print("RAW data :" , x.transpose())
                    result = result.dot(x.transpose())
                    
                elif files == "SNV":
                    self.snv()
                    print("snv_data shape:",snv_data.shape)
                    print("snv_data data :",snv_data)
                    result = result.dot(snv_data)

                elif files == "MSC":
                    sp = x
                    nos = x.shape[0]
                    wave = x.shape[1]
                    meansp=np.mean(sp,axis=0)
                    lbd=np.array(range(0,wave))
                    Ym=np.polyfit(lbd,meansp,1)
                    slopem=Ym[0]
                    interm=Ym[1]
                    Y=np.zeros([nos,2])
                    for i in range(0,nos):
                        Y[i,:]=np.polyfit(lbd,sp[i,:],1)
                    slope=np.tile(Y[:,0],(wave,1)).T
                    inter=np.tile(Y[:,1],(wave,1)).T
                    spmsc=(sp - inter) / slope
                    spmsc=np.multiply(spmsc,slopem) + np.tile(interm,(nos,wave))
                    
                    nos = x.shape[0]
                    wave = x.shape[1]
                    meansp=np.mean(sp,axis=0)
                    lbd=np.array(range(0,wave))
                    
                    Ym=np.polyfit(lbd,meansp,1)
                    mscval=np.copy(Ym)
                    slopem=Ym[0]
                    interm=Ym[1]
                    Y=np.zeros([nos,2])
                    for i in range(0,nos):
                        Y[i,:]=np.polyfit(lbd,sp[i,:],1)
                    slope=np.tile(Y[:,0],(wave,1)).T
                    inter=np.tile(Y[:,1],(wave,1)).T
                    spmsc=(sp - inter) / slope
                    spmsc=np.multiply(spmsc,slopem) + np.tile(interm,(nos,wave))
                    result = mscval
                    print("MSC shape :" , result)
                else: 
                    print("other")

            print("x_4 shape :" , x_4.shape)
            print("bias :" , int(self.systemconfig.spinBox_7.value()))
            result = (result.dot(x_4)) + int(self.systemconfig.spinBox_7.value())
            print("result shape :", result.shape)              
            print("result :", result)
            result4 = result
            self.dashborad.result4.setText(str(int(result[0][0])))

            self.dashborad.figure3.clear()
            ax2 = self.dashborad.figure3.add_subplot(111)
            ax2.set_xlabel('wavelenght, nm')
            ax2.set_ylabel('log 1/R')
            ax2.set_xlim(np.min(wave),np.max(wave))
            self.dashborad.canvas3.draw()
            print("draw succ4")

        if(file_5 != ""):
            print("file_5")
            wave = wave_5
            x = x_5
            steps = [self.prepro.comboBox.currentText(),self.prepro.comboBox2.currentText(),self.prepro.comboBox3.currentText()]
            result = x_5
            fristLoop = True
            for files in steps :
                if files == "1st Derivative":
                    s = s_1
                    g = g_1
                    self.FirstDev()
                    print("1st Derivative shape :" , sd1.shape)
                    print("1st Derivative data :" , sd1)
                    result = result.dot(sd1)

                elif files == "2nd Derivative":
                    s = s_2
                    g = g_2
                    self.SecondDev()
                    print("2nd Derivative shape :" , sd2.shape)
                    print("2nd Derivative data :" , sd2)
                    result = result.dot(sd2)
                    
                elif files == "RAW":
                    print("RAW shape :" , x.transpose().shape)
                    print("RAW data :" , x.transpose())
                    result = result.dot(x.transpose())
                    
                elif files == "SNV":
                    self.snv()
                    print("snv_data shape:",snv_data.shape)
                    print("snv_data data :",snv_data)
                    result = result.dot(snv_data)

                elif files == "MSC":
                    sp = x
                    nos = x.shape[0]
                    wave = x.shape[1]
                    meansp=np.mean(sp,axis=0)
                    lbd=np.array(range(0,wave))
                    Ym=np.polyfit(lbd,meansp,1)
                    slopem=Ym[0]
                    interm=Ym[1]
                    Y=np.zeros([nos,2])
                    for i in range(0,nos):
                        Y[i,:]=np.polyfit(lbd,sp[i,:],1)
                    slope=np.tile(Y[:,0],(wave,1)).T
                    inter=np.tile(Y[:,1],(wave,1)).T
                    spmsc=(sp - inter) / slope
                    spmsc=np.multiply(spmsc,slopem) + np.tile(interm,(nos,wave))
                    
                    nos = x.shape[0]
                    wave = x.shape[1]
                    meansp=np.mean(sp,axis=0)
                    lbd=np.array(range(0,wave))
                    
                    Ym=np.polyfit(lbd,meansp,1)
                    mscval=np.copy(Ym)
                    slopem=Ym[0]
                    interm=Ym[1]
                    Y=np.zeros([nos,2])
                    for i in range(0,nos):
                        Y[i,:]=np.polyfit(lbd,sp[i,:],1)
                    slope=np.tile(Y[:,0],(wave,1)).T
                    inter=np.tile(Y[:,1],(wave,1)).T
                    spmsc=(sp - inter) / slope
                    spmsc=np.multiply(spmsc,slopem) + np.tile(interm,(nos,wave))
                    result = mscval
                    print("MSC shape :" , result)
                else: 
                    print("other")

            print("x_5 shape :" , x_5.shape)
            print("bias :" , int(self.systemconfig.spinBox_8.value()))
            result = (result.dot(x_5)) + int(self.systemconfig.spinBox_8.value())
            print("result shape :", result.shape)              
            print("result :", result)
            result5 = result
            self.dashborad.result5.setText(str(int(result[0][0])))
            self.dashborad.figure4.clear()
            ax2 = self.dashborad.figure4.add_subplot(111)
            ax2.set_xlabel('wavelenght, nm')
            ax2.set_ylabel('log 1/R')
            ax2.set_xlim(np.min(wave),np.max(wave))
            self.dashborad.canvas4.draw()
            print("draw succ5")
        
    def FirstDev(self):
        global wave,x,s,g,sd1
        xx = x.shape[0]
        xy = x.shape[1]
        sd1= np.zeros([xx,xy])
        for i in range(int(s + g / 2 + 0.5), int(xy - s - g / 2 + 0.5)):
            sa=np.mean(x[:,int(i - s - g / 2 + 0.5):int(i - g / 2 - 0.5)], axis = 1)
            sc=np.mean(x[:,int(i + g / 2 + 0.5):int(i + g / 2 - 0.5 + s)], axis = 1)
            sd1[:,i]=sc - sa

    def SecondDev(self):
        global x,s,g,sd2
        xx = x.shape[0]
        xy = x.shape[1]
        sd2= np.zeros([xx,xy])

        for i in range(int(np.dot(3 / 2,s) + g + 0.5),int(xy - np.dot(3 / 2,s) - g + 0.5)):
            x_c=np.mean(x[:,int(i + s / 2 + g + 0.5):int(i +  np.dot(3 / 2,s) + g - 0.5)],axis = 1)
            x_a=np.mean(x[:,int(i - np.dot(3 / 2,s) - g + 0.5):int(i - s / 2 - g - 0.5)],axis = 1)
            x_b=np.mean(x[:,int(i - s / 2 + 0.5):int(i + s / 2 - 0.5)],axis = 1)
            sd2[:,i]=(x_c) - np.dot(2,(x_b)) + (x_a)

    def smooth_x(self):
        global x,s,g,smooth
        xx = x.shape[0]
        xy = x.shape[1]
        smooth = np.zeros([xx, xy])
        for i in range(s+1, xy-s):
            sa = np.mean(x[:, int(i - s):int(i + s)], axis=1)
            smooth[:, i] = sa

    # def meancen2(self):
    #     global wave,x,s,g,meanC
    #     # global graph
    #     xx = x.shape[0]
    #     xy = x.shape[1]
    #     mean_x=np.sum(x,axis =0)
    #     mean_x=mean_x / xx
    #     meand=np.tile(mean_x,(xx,1))
    #     meanC=(x - meand)

    #     graph.clear() 

    #     ax = graph.add_subplot(121)
    #     for i in range (x.shape[0]):  
    #         ax.plot(wave.tolist(),x[i].tolist())
    #     ax.set_xlabel('wavelenght, nm')
    #     ax.set_ylabel('log 1/R')
    #     ax.set_xlim(np.min(wave),np.max(wave))
        
    #     ax2 = graph.add_subplot(122)
    #     for i in range (x.shape[0]):  
    #         ax2.plot(wave,meanC[i])
    #     ax2.set_xlabel('wavelenght, nm')
    #     ax2.set_ylabel('Log 1/R')
    #     ax2.set_xlim(np.min(wave),np.max(wave))

    def snv(self):
        global x,s,g,snv_data
        xx = x.shape[0]
        xy = x.shape[1]
        mean_x=np.mean(x,axis =1)
        std_d=np.std(x,axis=1)
        meand=np.tile(mean_x,(xy,1)).T
        stdd=np.tile(std_d,(xy,1)).T
        snv_data= (x - meand)/stdd

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    # myapp.show()
    sys.exit(app.exec_())

    
