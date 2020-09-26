import sys

from matplotlib.backends.backend_pdf import PdfPages

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

import numpy as np
import pandas as pd

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
myPath = ""
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

global x_1,s_1,g_1,sd1_1,sd2_1 
global x_2,s_2,g_2,sd1_2,sd2_2
global x_3,s_3,g_3,sd1_3,sd2_3
global x_4,s_4,g_4,sd1_4,sd2_4
global x_5,s_5,g_5,sd1_5,sd2_5


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
        global clickStart,x,s,g,sd1,count_graph,smooth
        global x_coordinates1,list_tmp1
        global x_coordinates2,list_tmp2
        global x_coordinates3,list_tmp3
        global x_coordinates4,list_tmp4
        global x_coordinates5,list_tmp5
        global result1,result2,result3,result4,result5

        global x_1,s_1,g_1,sd1_1,sd2_1
        global x_2,s_2,g_2,sd1_2,sd2_2
        global x_3,s_3,g_3,sd1_3,sd2_3
        global x_4,s_4,g_4,sd1_4,sd2_4
        global x_5,s_5,g_5,sd1_5,sd2_5
        global file_spec,myPath
        now = datetime.now()
        # date_arr.append(now)

        current_time = now.strftime("%d %B %Y  %H:%M:%S")
        self.dashborad.dateNtime.setText(current_time)
        self.dashborad.tabWidget.setTabText(0, self.dashborad.label_result1.text())
        self.dashborad.tabWidget.setTabText(1, self.dashborad.label_result2.text())
        self.dashborad.tabWidget.setTabText(2, self.dashborad.label_result3.text())
        self.dashborad.tabWidget.setTabText(3, self.dashborad.label_result4.text())
        self.dashborad.tabWidget.setTabText(4, self.dashborad.label_result5.text())
        Find_file = False
        if(myPath != ""):
                file_spec = []
                files = glob.glob(os.path.join(myPath, '*.txt'))
                if(len(files) > 0 ):
                    files.sort(key=os.path.getmtime)
                    for txtfile in files:
                        file_spec.append(txtfile)
                    Find_file = True
                else:
                    Find_file = False
        if(clickStart == True and Find_file == True):
            if(myPath != ""):
                if(len(file_spec) > 0):
                    f = open(file_spec[len(file_spec)-1], "r")
                    print(f)
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

                if(file_1 != ""):
                    print("file_1")
                    B = x_1
                    x = x_1
                    X = np.array(X)
                    steps = [self.prepro.comboBox.currentText(),self.prepro.comboBox2.currentText(),self.prepro.comboBox3.currentText()]
                    result = B.dot(X)
                    for step in steps :
                        if step == "1st Derivative":
                            s = s_1
                            g = g_1
                            self.FirstDev()
                            result = result*(sd1.transpose())
                        elif step == "2nd Derivative":
                            s = s_2
                            g = g_2
                            self.SecondDev()
                            result = result*(sd2.transpose())
                        elif step == "RAW":
                            result = result*(B.transpose())
                            
                        elif step == "SNV":
                            self.snv()
                            result = result*(snv_data.transpose())
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
                            # result = spmsc
                            result = result*(spmsc.transpose())
                            # print("MSC shape :" , result.shape)

                        elif step == "Smoothing Size":
                            s = s_3
                            g = g_3
                            self.smooth_x()
                            result = result*(smooth.transpose())
                        
                    result = (B.dot(result)) + int(self.systemconfig.spinBox_4.value())
                    print("cal result  :", result)              
                    result1 = result[0][0]
                    self.dashborad.result1.setText(str(int(result1)))
                    self.dashborad.figure.clear()
                    ax2 = self.dashborad.figure.add_subplot(111)
                    x_coordinates1.append(now.strftime('%H:%M:%S'))
                    list_tmp1.append(result1)
                    ax2.plot(x_coordinates1, list_tmp1)

                    ax2.set_xlabel('wavelenght, nm')
                    ax2.set_ylabel('log 1/R')
                    gs = gridspec.GridSpec(3,1)
                    ax2.set_position(gs[0:2].get_position(self.dashborad.figure))
                    ax2.set_subplotspec(gs[0:2])   
                    ax2.set_xticklabels(x_coordinates1, rotation=90 , fontsize=8 )
                    self.dashborad.canvas.draw()
                    print("draw 1 succ !!")

                if(file_2 != ""):
                    print("file_2")
                    B = x_2
                    x = x_2
                    X = np.array(X)
                    steps = [self.prepro.comboBox.currentText(),self.prepro.comboBox2.currentText(),self.prepro.comboBox3.currentText()]
                    result = B.dot(X)

                    for step in steps :
                        if step == "1st Derivative":
                            s = s_1
                            g = g_1
                            self.FirstDev()
                            result = result*(sd1.transpose())
                        elif step == "2nd Derivative":
                            s = s_2
                            g = g_2
                            self.SecondDev()
                            result = result*(sd2.transpose())
                        elif step == "RAW":
                            result = result*(B.transpose())
                            
                        elif step == "SNV":
                            self.snv()
                            result = result*(snv_data.transpose())
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
                            # result = spmsc
                            result = result*(spmsc.transpose())
                        elif step == "Smoothing Size":
                            s = s_3
                            g = g_3
                            self.smooth_x()
                            result = result*(smooth.transpose())
                        
                    result = (B.dot(result)) + int(self.systemconfig.spinBox_5.value())
                    self.dashborad.figure1.clear()
                    ax2 = self.dashborad.figure1.add_subplot(111)
                    result2 = result[0][0]
                    self.dashborad.result2.setText(str(int(result2)))

                    list_tmp2.append(result2)
                    x_coordinates2.append(now.strftime('%H:%M:%S'))
                    ax2.plot(x_coordinates2, list_tmp2)

                    ax2.set_xlabel('wavelenght, nm')
                    ax2.set_ylabel('log 1/R')
                    gs = gridspec.GridSpec(3,1)
                    ax2.set_position(gs[0:2].get_position(self.dashborad.figure1))
                    ax2.set_subplotspec(gs[0:2])   
                    ax2.set_xticklabels(x_coordinates2, rotation=90 , fontsize=8 )
                    self.dashborad.canvas1.draw()
                    print("draw 2 succ !!")

                if(file_3 != ""):
                    B = x_3
                    x = x_3
                    X = np.array(X)
                    steps = [self.prepro.comboBox.currentText(),self.prepro.comboBox2.currentText(),self.prepro.comboBox3.currentText()]
                    result = B.dot(X)

                    for step in steps :
                        if step == "1st Derivative":
                            s = s_1
                            g = g_1
                            self.FirstDev()
                            result = result*(sd1.transpose())
                        elif step == "2nd Derivative":
                            s = s_2
                            g = g_2
                            self.SecondDev()
                            result = result*(sd2.transpose())
                        elif step == "RAW":
                            result = result*(B.transpose())
                            
                        elif step == "SNV":
                            self.snv()
                            result = result*(snv_data.transpose())
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
                            result = result*(spmsc.transpose())

                        elif step == "Smoothing Size":
                            s = s_3
                            g = g_3
                            self.smooth_x()
                            result = result*(smooth.transpose())
                    result = (B.dot(result)) + int(self.systemconfig.spinBox_6.value())
                    self.dashborad.figure2.clear()
                    ax2 = self.dashborad.figure2.add_subplot(111)
                    result3 = result[0][0]
                    self.dashborad.result3.setText(str(int(result3)))

                    list_tmp3.append(result3)
                    x_coordinates3.append(now.strftime('%H:%M:%S'))
                    ax2.plot(x_coordinates3, list_tmp3)
                    ax2.set_xlabel('wavelenght, nm')
                    ax2.set_ylabel('log 1/R')
                    gs = gridspec.GridSpec(3,1)
                    ax2.set_position(gs[0:2].get_position(self.dashborad.figure2))
                    ax2.set_subplotspec(gs[0:2])   
                    ax2.set_xticklabels(x_coordinates3, rotation=90 , fontsize=8 )
                    self.dashborad.canvas2.draw()
                    print("draw 3 succ !!") 

                if(file_4 != ""):
                    B = x_4
                    x = x_4
                    X = np.array(X)
                    steps = [self.prepro.comboBox.currentText(),self.prepro.comboBox2.currentText(),self.prepro.comboBox3.currentText()]
                    result = B.dot(X)
                    for step in steps :
                        if step == "1st Derivative":
                            s = s_1
                            g = g_1
                            self.FirstDev()
                            result = result*(sd1.transpose())
                        elif step == "2nd Derivative":
                            s = s_2
                            g = g_2
                            self.SecondDev()
                            result = result*(sd2.transpose())
                        elif step == "RAW":
                            result = result*(B.transpose())
                            
                        elif step == "SNV":
                            self.snv()
                            result = result*(snv_data.transpose())
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
                            # result = spmsc
                            result = result*(spmsc.transpose())

                        elif step == "Smoothing Size":
                            s = s_3
                            g = g_3
                            self.smooth_x()
                            result = result*(smooth.transpose())
                    result = (B.dot(result)) + int(self.systemconfig.spinBox_7.value())
                    self.dashborad.figure3.clear()
                    ax2 = self.dashborad.figure3.add_subplot(111)
                    result4 = result[0][0]
                    self.dashborad.result4.setText(str(int(result4)))

                    list_tmp4.append(result4)
                    x_coordinates4.append(now.strftime('%H:%M:%S'))

                    ax2.plot(x_coordinates4, list_tmp4)
                    ax2.set_xlabel('wavelenght, nm')
                    ax2.set_ylabel('log 1/R')

                    gs = gridspec.GridSpec(3,1)
                    ax2.set_position(gs[0:2].get_position(self.dashborad.figure3))
                    ax2.set_subplotspec(gs[0:2])   
                    ax2.set_xticklabels(x_coordinates4, rotation=90 , fontsize=8 )
                    self.dashborad.canvas3.draw()
                    print("draw 4 succ !!")
                if(file_5 != ""):
                    B = x_5
                    x = x_5
                    X = np.array(X)
                    steps = [self.prepro.comboBox.currentText(),self.prepro.comboBox2.currentText(),self.prepro.comboBox3.currentText()]
                    result = B.dot(X)

                    for step in steps :
                        if step == "1st Derivative":
                            s = s_1
                            g = g_1
                            self.FirstDev()
                            result = result*(sd1.transpose())
                        elif step == "2nd Derivative":
                            s = s_2
                            g = g_2
                            self.SecondDev()
                            result = result*(sd2.transpose())
                        elif step == "RAW":
                            result = result*(B.transpose())
                            
                        elif step == "SNV":
                            self.snv()
                            result = result*(snv_data.transpose())

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
                            # result = spmsc
                            result = result*(spmsc.transpose())

                        elif step == "Smoothing Size":
                            s = s_3
                            g = g_3
                            self.smooth_x()
                            result = result*(smooth.transpose())
                    result = (B.dot(result)) + int(self.systemconfig.spinBox_8.value())

                    self.dashborad.figure4.clear()
                    ax2 = self.dashborad.figure4.add_subplot(111)
                    x_coordinates5.append(now.strftime('%H:%M:%S'))
                    result5 = result[0][0]
                    self.dashborad.result5.setText(str(int(result5)))

                    list_tmp5.append(result5)
                    ax2.plot(x_coordinates5, list_tmp5)
                    ax2.set_xlabel('wavelenght, nm')
                    ax2.set_ylabel('log 1/R')
                    gs = gridspec.GridSpec(3,1)
                    ax2.set_position(gs[0:2].get_position(self.dashborad.figure4))
                    ax2.set_subplotspec(gs[0:2])   
                    ax2.set_xticklabels(x_coordinates5, rotation=90 , fontsize=8 )
                    self.dashborad.canvas4.draw()
                    print("draw 5 succ !!")

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

        self.prepro.Export.clicked.connect(self.getTxt)
    def specific(self):
        global file_spec,myPath
        myPath = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))

        print("specific path:",myPath)
        self.systemconfig.Label_Upload.setText(str(myPath))

    def getPrepair(self):
        print("[func] : getPrepair")
        global g_1,g_2,g_3,s_1,s_2,s_3

        g_1 = int(self.prepro.spinBox_7.value())
        s_1 = int(self.prepro.spinBox_Seg_1st.value())    
        
        g_2 = int(self.prepro.spinBox_8.value())
        s_2 = int(self.prepro.spinBox_Seg_2nd.value())
        
        g_3 = int(self.prepro.spinBox_grab_Smoothing_w.value())
        s_3 = int(self.prepro.spinBox_Seg_Smoothing.value())

        print("1st    :" , g_1 , s_1)
        print("2nd    :" , g_2 , s_2  )
        print("Smooth :" , g_3 , s_3)

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
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file','c:/', "files (*.csv)")
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

    def getTxt(self):
        if(str(self.prepro.widget_name.text()) == "Type your name..."):
            f = open("undefined.txt", "w")
        else:
            f = open(str(self.prepro.widget_name.text())+".txt", "w")
        f.write(str(self.dashborad.label_result1.text()) +" = "+str(self.dashborad.result1.text())+"\n")
        f.write(str(self.dashborad.label_result2.text()) +" = "+str(self.dashborad.result2.text())+"\n")
        f.write(str(self.dashborad.label_result3.text()) +" = "+str(self.dashborad.result3.text())+"\n")
        f.write(str(self.dashborad.label_result4.text()) +" = "+str(self.dashborad.result4.text())+"\n")
        f.write(str(self.dashborad.label_result5.text()) +" = "+str(self.dashborad.result5.text())+"\n")
        f.close()
        self.prepro.hide()
        self.dashborad.show()

    def getApply(self):
        print("[func] : getApply")
        global file_1,file_2,file_3,file_4,file_5
        global x_1,x_2,x_3,x_4,x_5
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
        list_tmp2 = []
        list_tmp3 = []
        list_tmp4 = []
        list_tmp5 = []

        if(file_1 != ""):
            print(file_1)
            X = pd.read_csv(file_1, header = None)
            x_1 = np.array(X)
        if(file_2 != ""):
            print(file_2)
            X = pd.read_csv(file_2, header = None)
            x_2 = np.array(X)
        if(file_3 != ""):
            print(file_3)
            X = pd.read_csv(file_3, header = None)
            x_3 = np.array(X)
        if(file_4 != ""):
            print(file_4)
            X = pd.read_csv(file_4, header = None)
            x_4 = np.array(X)
        if(file_5 != ""):
            print(file_5)
            X = pd.read_csv(file_5, header = None)
            x_5 = np.array(X)

        self.systemconfig.hide()
        self.dashborad.show()

    def getWave(self ):
        global clickStart
        clickStart = True 
        print("[func] : getWave") 
        
    def FirstDev(self):
        global x,s,g,sd1
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

    def snv(self):
        global x,s,g,snv_data
        xx = x.shape[0]
        xy = x.shape[1]
        mean_x=np.mean(x,axis =1)
        print("mean_x",mean_x)
        std_d=np.std(x,axis=1)
        print("std_d",std_d)
        meand=np.tile(mean_x,(xy,1)).T
        stdd=np.tile(std_d,(xy,1)).T
        print("meand,stdd",meand,stdd)
        snv_data= (x - meand)/stdd

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    # myapp.show()
    sys.exit(app.exec_())

    
