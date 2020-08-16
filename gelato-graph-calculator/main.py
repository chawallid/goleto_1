import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QFileDialog, QLabel
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from matplotlib.backends.backend_pdf import PdfPages

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from fpdf import FPDF

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
global meanC,snv_data,mscval
global wave,x,s,g
global wave_1,x_1,s_1,g_1,sd1_1,sd2_1
global wave_2,x_2,s_2,g_2,sd1_2,sd2_2
global wave_3,x_3,s_3,g_3,sd1_3,sd2_3
global wave_4,x_4,s_4,g_4,sd1_4,sd2_4
global wave_5,x_5,s_5,g_5,sd1_5,sd2_5


class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.dashborad = Ui_Dashborad()
        self.prepro =  Ui_Prepro()
        self.systemconfig = Ui_SystemConfig()

       
        self.dashborad.setupUi(self)

        self.prepro.setupUi(self)
        self.prepro.centralwidget.hide()

        self.systemconfig.setupUi(self)
        self.systemconfig.centralwidget.hide()
        
        
        self.setupUi()
    
    def setupUi(self):
        self.dashborad.buttonSysConfig.clicked.connect(self.systemconfig.centralwidget.show)
        self.dashborad.buttonSysConfig.clicked.connect(self.dashborad.centralwidget.hide)

        self.dashborad.buttonPrePro.clicked.connect(self.prepro.centralwidget.show)
        self.dashborad.buttonPrePro.clicked.connect(self.dashborad.centralwidget.hide)

        self.prepro.btnBack.clicked.connect(self.prepro.centralwidget.hide)
        self.prepro.btnBack.clicked.connect(self.dashborad.centralwidget.show)
        
        self.systemconfig.btnBack.clicked.connect(self.systemconfig.centralwidget.hide)
        self.systemconfig.btnBack.clicked.connect(self.dashborad.centralwidget.show)

        self.systemconfig.btn1.clicked.connect(self.getbtn1)
        self.systemconfig.btn2.clicked.connect(self.getbtn2)
        self.systemconfig.btn3.clicked.connect(self.getbtn3)
        self.systemconfig.btn4.clicked.connect(self.getbtn4)
        self.systemconfig.btn5.clicked.connect(self.getbtn5)

        self.dashborad.START.clicked.connect(self.getWave)
        self.systemconfig.btnApply.clicked.connect(self.getApply)

        self.prepro.btnApply.clicked.connect(self.getPrepair)
        # self.prepro.btnApply.clicked.connect(self.getPDF)
    def getPrepair(self):
        
        global g_1,g_2,s_1,s_2

        g_1 = int(self.prepro.spinBox_7.value())
        g_2 = int(self.prepro.spinBox.value())
        # print("1st :" , g_1 , g_2)
        s_1 = int(self.prepro.spinBox_8.value())
        s_2 = int(self.prepro.spinBox_2.value())

        print("[func] : getPrepair")
        print("1st :" , g_1 , s_1)
        print("2nd :" , s_2 , g_2)
       
    def getbtn1(self):
        global file_1
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:/', "files (*.xlsx)")
        imagePath = fname[0]
        file_1 = fname[0]
        file_tmp = imagePath.split("/")
        self.systemconfig.label_1_.setText(file_tmp[len(file_tmp)-1])

    def getbtn2(self):
        global file_2
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:/', "files (*.xlsx)")
        imagePath = fname[0]
        file_2 = fname[0]
        file_tmp = imagePath.split("/")
        self.systemconfig.label_2_.setText(file_tmp[len(file_tmp)-1])

    def getbtn3(self):
        global file_3
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:/', "files (*.xlsx)")
        imagePath = fname[0]
        file_3 = fname[0]
        file_tmp = imagePath.split("/")
        self.systemconfig.label_3_.setText(file_tmp[len(file_tmp)-1])

    def getbtn4(self):
        global file_4
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:/', "files (*.xlsx)")
        imagePath = fname[0]
        file_4 = fname[0]
        file_tmp = imagePath.split("/")
        self.systemconfig.label_4_.setText(file_tmp[len(file_tmp)-1])

    def getbtn5(self):
        global file_5
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:/', "files (*.xlsx)")
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
        self.prepro.centralwidget.hide()
        self.dashborad.centralwidget.show()
                
        

    
    def clickMethod(self):
        QMessageBox.about(self, "Title", "Message")

    def getApply(self):
        global file_1,file_2,file_3,file_4,file_5
        global wave_1,x_1,s_1,g_1,sd1_1,sd2_1
        global wave_2,x_2,s_2,g_2,sd1_2,sd2_2
        global wave_3,x_3,s_3,g_3,sd1_3,sd2_3
        global wave_4,x_4,s_4,g_4,sd1_4,sd2_4
        global wave_5,x_5,s_5,g_5,sd1_5,sd2_5

        if(file_1 != ""):
            print("pass")
            print(file_1)
            X = pd.read_excel(file_1, sheet_name='X', header = None)
            wl = pd.read_excel(file_1, sheet_name='wl', header = None)

            wave_1 = np.array(wl).reshape(-1)
            x_1 = np.array(X)
            
            self.dashborad.result1.setText(str(x_1))
            files = self.systemconfig.comboBox.currentText()

        if(file_2 != ""):
            X = pd.read_excel(file_2, sheet_name='X', header = None)
            wl = pd.read_excel(file_2, sheet_name='wl', header = None)
            wave_2 = np.array(wl).reshape(-1)
            x_2 = np.array(X)
            self.dashborad.result2.setText(str(x_2))
            files = self.systemconfig.comboBox_2.currentText()

        if(file_3 != ""):
            X = pd.read_excel(file_3, sheet_name='X', header = None)
            wl = pd.read_excel(file_3, sheet_name='wl', header = None)
            wave_3 = np.array(wl).reshape(-1)
            x_3 = np.array(X)

            self.dashborad.result2.setText(str(x_3))
            files = self.systemconfig.comboBox_3.currentText()

        if(file_4 != ""):
            X = pd.read_excel(file_4, sheet_name='X', header = None)
            wl = pd.read_excel(file_4, sheet_name='wl', header = None)
            wave_3 = np.array(wl).reshape(-1)
            x_4 = np.array(X)
     
            self.dashborad.result2.setText(str(x_4))
            files = self.systemconfig.comboBox_4.currentText()
            
        if(file_5 != ""):
            X = pd.read_excel(file_5, sheet_name='X', header = None)
            wl = pd.read_excel(file_5, sheet_name='wl', header = None)
            wave_5 = np.array(wl).reshape(-1)
            x_5 = np.array(X)
    
            self.dashborad.result2.setText(str(x_5))
            files = self.systemconfig.comboBox_5.currentText()

        self.systemconfig.centralwidget.hide()
        self.dashborad.centralwidget.show()

    def getWave(self ):
        print("[func] : getWave")

        global file_1,file_2,file_3,file_4,file_5,meanC,snv_data,mscval
        global graph 
        global wave,x,s,g

        global wave_1,x_1,s_1,g_1,sd1_1,sd2_1
        global wave_2,x_2,s_2,g_2,sd1_2,sd2_2
        global wave_3,x_3,s_3,g_3,sd1_3,sd2_3
        global wave_4,x_4,s_4,g_4,sd1_4,sd2_4
        global wave_5,x_5,s_5,g_5,sd1_5,sd2_5


        s = 0
        g = 0

        if(file_1 != ""):
            print("pass")
            wave = wave_1
            x = x_1
            steps = [self.prepro.comboBox.currentText(),self.prepro.comboBox_2.currentText(),self.prepro.comboBox_3.currentText()]
            graph = self.dashborad.figure
            for files in steps :
                print(files)
            

                if files == "1st Derivative":
                    s = s_1
                    g = g_1
                    # self.FirstDev()
                    # self.prepro.label_RAW.setText(str(sd1))
                    # self.dashborad.result1.setText(str(sd1))
                    
                elif files == "2nd Derivative":
                    s = s_2
                    g = g_2
                    # self.SecondDev()
                    # self.prepro.label_SNV.setText(str(sd2))
                    # self.dashborad.result1.setText(str(sd2))
                elif files == "RAW":
                    # self.meancen2()
                    # self.prepro.label_MSC.setText(str(meanC))
                    # self.dashborad.result1.setText(str(meanC))

                elif files == "SNV":
                    # self.snv()
                    # self.prepro.label_1stDeri.setText(str(snv_data))
                    # self.dashborad.result1.setText(str(snv_data))

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

                    # //////////////////////////////////////////////
                    
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
                    # self.prepro.label_2ndDeri.setText(str(mscval[1]))
                    # self.dashborad.result1.setText(str(mscval[1]))
                else: 
                    print("other")
                    # self.FirstDev()
                    # self.prepro.label_RAW.setText(str(sd1))
                    # self.dashborad.result1.setText(str(sd1))

            self.dashborad.canvas.draw()
            print("draw succ1")

        if(file_2 != ""):
            wave = wave_2
            x = x_2
           
            files = self.systemconfig.comboBox_2.currentText()
            graph = self.dashborad.figure1
            if files == "FirstDev":
                s = s_1
                g = g_1
                self.FirstDev()
                self.prepro.label_RAW.setText(str(sd1))
                self.dashborad.result2.setText(str(sd1))
            elif files == "SecondDev":
                s = s_2
                g = g_2
                self.SecondDev()
                self.prepro.label_SNV.setText(str(sd2))
                self.dashborad.result2.setText(str(sd2))
            elif files == "meancen2":
                self.meancen2()
                self.prepro.label_MSC.setText(str(meanC))
                self.dashborad.result2.setText(str(meanC))

            elif files == "snv":
                self.snv()
                self.prepro.label_1stDeri.setText(str(snv_data))
                self.dashborad.result2.setText(str(snv_data))

            elif files == "msc":
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
    # //////////////////////////////////////////////
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
                self.prepro.label_2ndDeri.setText(str(mscval[1]))
                self.dashborad.result2.setText(str(mscval[1]))
            else: 
                self.FirstDev()
                self.prepro.label_RAW.setText(str(sd1))
                self.dashborad.result2.setText(str(sd1))
            self.dashborad.canvas1.draw()
            print("draw succ2")

        if(file_3 != ""):
            wave = wave_3
            x = x_3
            files = self.systemconfig.comboBox_3.currentText()
            graph = self.dashborad.figure2
            if files == "FirstDev":
                s = s_1
                g = g_1
                self.FirstDev()
                self.prepro.label_RAW.setText(str(sd1))
                self.dashborad.result3.setText(str(sd1))
            elif files == "SecondDev":
                s = s_2
                g = g_2
                self.SecondDev()
                self.prepro.label_SNV.setText(str(sd2))
                self.dashborad.result3.setText(str(sd2))
            elif files == "meancen2":
                self.meancen2()
                self.prepro.label_MSC.setText(str(meanC))
                self.dashborad.result3.setText(str(meanC))

            elif files == "snv":
                self.snv()
                self.prepro.label_1stDeri.setText(str(snv_data))
                self.dashborad.result3.setText(str(snv_data))

            elif files == "msc":
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
    # //////////////////////////////////////////////
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
                self.prepro.label_2ndDeri.setText(str(mscval[1]))
                self.dashborad.result3.setText(str(mscval[1]))
            else: 
                self.FirstDev()
                self.prepro.label_RAW.setText(str(sd1))
                self.dashborad.result3.setText(str(sd1))
            self.dashborad.canvas2.draw()
            print("draw succ3")

        if(file_4 != ""):
            wave = wave_4
            x = x_4
            files = self.systemconfig.comboBox_4.currentText()
            graph = self.dashborad.figure3
            if files == "FirstDev":
                s = s_1
                g = g_1
                self.FirstDev()
                self.prepro.label_RAW.setText(str(sd1))
                self.dashborad.result4.setText(str(sd1))
            elif files == "SecondDev":
                s = s_2
                g = g_2
                self.SecondDev()
                self.prepro.label_SNV.setText(str(sd2))
                self.dashborad.result4.setText(str(sd2))
            elif files == "meancen2":
                self.meancen2()
                self.prepro.label_MSC.setText(str(meanC))
                self.dashborad.result4.setText(str(meanC))

            elif files == "snv":
                self.snv()
                self.prepro.label_1stDeri.setText(str(snv_data))
                self.dashborad.result4.setText(str(snv_data))

            elif files == "msc":
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
    # //////////////////////////////////////////////
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
                self.prepro.label_2ndDeri.setText(str(mscval[1]))
                self.dashborad.result5.setText(str(mscval[1]))
            else: 
                self.FirstDev()
                self.prepro.label_RAW.setText(str(sd1))
                self.dashborad.result4.setText(str(sd1))
            self.dashborad.canvas3.draw()
            print("draw succ4")

        if(file_5 != ""):
            wave = wave_5
            x = x_5
            files = self.systemconfig.comboBox_5.currentText()
            # graph = self.dashborad.figure
            if files == "FirstDev":
                s = s_1
                g = g_1
                self.FirstDev()
                self.prepro.label_RAW.setText(str(sd1))
                self.dashborad.result5.setText(str(sd1))
            elif files == "SecondDev":
                s = s_2
                g = g_2
                self.SecondDev()
                self.prepro.label_SNV.setText(str(sd2))
                self.dashborad.result5.setText(str(sd2))
            elif files == "meancen2":
                self.meancen2()
                self.prepro.label_MSC.setText(str(meanC))
                self.dashborad.result5.setText(str(meanC))

            elif files == "snv":
                self.snv()
                self.prepro.label_1stDeri.setText(str(snv_data))
                self.dashborad.result5.setText(str(snv_data))

            elif files == "msc":
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
    # //////////////////////////////////////////////
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
                self.prepro.label_2ndDeri.setText(str(mscval[1]))
                self.dashborad.result5.setText(str(mscval[1]))
            else: 
                self.FirstDev()
                self.prepro.label_RAW.setText(str(sd1))
                self.dashborad.result5.setText(str(sd1))

        self.systemconfig.centralwidget.hide()
        self.dashborad.centralwidget.show()
        

        # spmsc = msc(x)

        # print(spmsc)  

        # spmsc,mscval = msc(x,nargout = 2)
        # print(spmsc,mscval)
    def FirstDev(self):
        global wave,x,s,g,sd1
        global graph
        xx = x.shape[0]
        xy = x.shape[1]
        sd1= np.zeros([xx,xy])
        for i in range(int(s + g / 2 + 0.5), int(xy - s - g / 2 + 0.5)):
            sa=np.mean(x[:,int(i - s - g / 2 + 0.5):int(i - g / 2 - 0.5)], axis = 1)
            sc=np.mean(x[:,int(i + g / 2 + 0.5):int(i + g / 2 - 0.5 + s)], axis = 1)
            sd1[:,i]=sc - sa
        # print("pass1")
        graph.clear()
        # print("pass2")
        ax = graph.add_subplot(121)
        for i in range (x.shape[0]):  
            ax.plot(wave.tolist(),x[i].tolist())

        ax.set_xlabel('wavelenght, nm')
        ax.set_ylabel('log 1/R')
        ax.set_xlim(np.min(wave),np.max(wave))

        ax2 = graph.add_subplot(122)
        for i in range (x.shape[0]):  
            ax2.plot(wave.tolist(),sd1[i].tolist())
        ax2.set_xlabel('wavelenght, nm')
        ax2.set_ylabel('Log 1/R')
        ax2.set_xlim(np.min(wave),np.max(wave))

        # self.dashborad.canvas.draw()
        # print("draw succ1")

    def SecondDev(self):
        global wave,x,s,g,sd2
        global graph
        xx = x.shape[0]
        xy = x.shape[1]
        sd2= np.zeros([xx,xy])
        for i in range(int(np.dot(3 / 2,s) + g + 0.5),int(xy - np.dot(3 / 2,s) - g + 0.5)):
            x_c=np.mean(x[:,int(i + s / 2 + g + 0.5):int(i +  np.dot(3 / 2,s) + g - 0.5)],axis = 1)
            x_a=np.mean(x[:,int(i - np.dot(3 / 2,s) - g + 0.5):int(i - s / 2 - g - 0.5)],axis = 1)
            x_b=np.mean(x[:,int(i - s / 2 + 0.5):int(i + s / 2 - 0.5)],axis = 1)
            sd2[:,i]=(x_c) - np.dot(2,(x_b)) + (x_a)

        graph.clear()
        ax = graph.add_subplot(121)
        for i in range (x.shape[0]):  
            ax.plot(wave.tolist(),x[i].tolist())
        ax.set_xlabel('wavelenght, nm')
        ax.set_ylabel('log 1/R')
        ax.set_xlim(np.min(wave),np.max(wave))
        ax2 = graph.add_subplot(122)
        for i in range (x.shape[0]):  
            ax2.plot(wave.tolist() , sd2[i].tolist())
        ax2.set_xlabel('wavelenght, nm')
        ax2.set_ylabel('Log 1/R')
        ax2.set_xlim(np.min(wave),np.max(wave))
        # self.dashborad.canvas1.draw()
        # print("draw succ2")

    def meancen2(self):
        global wave,x,s,g,meanC
        global graph
        xx = x.shape[0]
        xy = x.shape[1]
        mean_x=np.sum(x,axis =0)
        mean_x=mean_x / xx
        meand=np.tile(mean_x,(xx,1))
        meanC=(x - meand)

        graph.clear() 

        ax = graph.add_subplot(121)
        for i in range (x.shape[0]):  
            ax.plot(wave.tolist(),x[i].tolist())
        ax.set_xlabel('wavelenght, nm')
        ax.set_ylabel('log 1/R')
        ax.set_xlim(np.min(wave),np.max(wave))
        
        ax2 = graph.add_subplot(122)
        for i in range (x.shape[0]):  
            ax2.plot(wave,meanC[i])
        ax2.set_xlabel('wavelenght, nm')
        ax2.set_ylabel('Log 1/R')
        ax2.set_xlim(np.min(wave),np.max(wave))

        # self.dashborad.canvas2.draw()
        # print("draw succ3")

    def snv(self):
        global wave,x,s,g,snv_data
        global graph
        xx = x.shape[0]
        xy = x.shape[1]
        mean_x=np.mean(x,axis =1)
        std_d=np.std(x,axis=1)
        meand=np.tile(mean_x,(xy,1)).T
        stdd=np.tile(std_d,(xy,1)).T
        
        snv_data= (x - meand) / stdd
        
        graph.clear()         
        ax = graph.add_subplot(121)
        for i in range (x.shape[0]):  
            ax.plot(wave.tolist(),x[i].tolist())
        ax.set_xlabel('wavelenght, nm')
        ax.set_ylabel('log 1/R')
        ax.set_xlim(np.min(wave),np.max(wave))
        
        ax2 = graph.add_subplot(122)
        for i in range (x.shape[0]):  
            ax2.plot(wave,snv_data[i])
        ax2.set_xlabel('wavelenght, nm')
        ax2.set_ylabel('Log 1/R')
        ax2.set_xlim(np.min(wave),np.max(wave))

        # self.dashborad.canvas3.draw()
        # print("draw succ4")
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())
