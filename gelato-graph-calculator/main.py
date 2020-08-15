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

file = ""
global wave,x,s,g,sd1,sd2,meanC,snv_data,mscval



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

        self.systemconfig.btn1.clicked.connect(self.getImage)
        self.systemconfig.btnApply.clicked.connect(self.getWave)
        self.prepro.btnApply.clicked.connect(self.getPDF)
    def getImage(self):
        global file
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:/', "files (*.xlsx)")
        imagePath = fname[0]

        file = fname[0]

        file_tmp = imagePath.split("/")
        self.systemconfig.label_1_.setText(file_tmp[len(file_tmp)-1])

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
                    # self.dashborad.figure.title("RAW")
                    pdf.savefig(self.dashborad.figure)

                elif files == "SNV":
                    # self.dashborad.figure1.title("SNV")
                    pdf.savefig(self.dashborad.figure1)

                elif files == "MSC":
                    # self.dashborad.figure2.title("MSC")
                    pdf.savefig(self.dashborad.figure2)

                elif files == "1st Derivative":
                    # self.dashborad.figure3.title("1st Derivative")
                    pdf.savefig(self.dashborad.figure3)

                elif files == "2nd Derivative":
                    print("2nd Derivative")
                else: 
                    pdf.savefig()
        self.prepro.centralwidget.hide()
        self.dashborad.centralwidget.show()
                
        

    
    def clickMethod(self):
        QMessageBox.about(self, "Title", "Message")

    def getWave(self):
        global file,wave,x,s,g,sd1,sd2,meanC,snv_data,mscval
        print(file)
        if(file != ""):

            X = pd.read_excel(file, sheet_name='X', header = None)
            wl = pd.read_excel(file, sheet_name='wl', header = None)
            wave = np.array(wl).reshape(-1)
            x = np.array(X)
            s =5
            g= 5

            self.FirstDev()
            self.SecondDev()
            self.meancen2()
            self.snv()

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

            # print("raw =",wl)
            # print("snv =",snv_data)
            # print("msc =",mscval[1])

            self.prepro.label_RAW.setText("0")
            self.prepro.label_SNV.setText("1")
            self.prepro.label_MSC.setText(str(mscval[1]))
            
            self.systemconfig.centralwidget.hide()
            self.dashborad.centralwidget.show()
        

        # spmsc = msc(x)

        # print(spmsc)  

        # spmsc,mscval = msc(x,nargout = 2)
        # print(spmsc,mscval)
    def FirstDev(self):
        global file,wave,x,s,g,sd1
    
        xx = x.shape[0]
        xy = x.shape[1]
        sd1= np.zeros([xx,xy])
        for i in range(int(s + g / 2 + 0.5), int(xy - s - g / 2 + 0.5)):
            sa=np.mean(x[:,int(i - s - g / 2 + 0.5):int(i - g / 2 - 0.5)], axis = 1)
            sc=np.mean(x[:,int(i + g / 2 + 0.5):int(i + g / 2 - 0.5 + s)], axis = 1)
            sd1[:,i]=sc - sa
        # print("pass1")
        self.dashborad.figure.clear()
        # print("pass2")
        ax = self.dashborad.figure.add_subplot(121)
        for i in range (x.shape[0]):  
            ax.plot(wave.tolist(),x[i].tolist())

        ax.set_xlabel('wavelenght, nm')
        ax.set_ylabel('log 1/R')
        ax.set_xlim(np.min(wave),np.max(wave))

        ax2 = self.dashborad.figure.add_subplot(122)
        for i in range (x.shape[0]):  
            ax2.plot(wave.tolist(),sd1[i].tolist())
        ax2.set_xlabel('wavelenght, nm')
        ax2.set_ylabel('Log 1/R')
        ax2.set_xlim(np.min(wave),np.max(wave))

        self.dashborad.canvas.draw()
        print("draw succ1")

    def SecondDev(self):
        global file,wave,x,s,g,sd2
       
        xx = x.shape[0]
        xy = x.shape[1]
        sd2= np.zeros([xx,xy])
        for i in range(int(np.dot(3 / 2,s) + g + 0.5),int(xy - np.dot(3 / 2,s) - g + 0.5)):
            x_c=np.mean(x[:,int(i + s / 2 + g + 0.5):int(i +  np.dot(3 / 2,s) + g - 0.5)],axis = 1)
            x_a=np.mean(x[:,int(i - np.dot(3 / 2,s) - g + 0.5):int(i - s / 2 - g - 0.5)],axis = 1)
            x_b=np.mean(x[:,int(i - s / 2 + 0.5):int(i + s / 2 - 0.5)],axis = 1)
            sd2[:,i]=(x_c) - np.dot(2,(x_b)) + (x_a)

        self.dashborad.figure1.clear()
        ax = self.dashborad.figure1.add_subplot(121)
        for i in range (x.shape[0]):  
            ax.plot(wave.tolist(),x[i].tolist())
        ax.set_xlabel('wavelenght, nm')
        ax.set_ylabel('log 1/R')
        ax.set_xlim(np.min(wave),np.max(wave))
        ax2 = self.dashborad.figure1.add_subplot(122)
        for i in range (x.shape[0]):  
            ax2.plot(wave.tolist() , sd2[i].tolist())
        ax2.set_xlabel('wavelenght, nm')
        ax2.set_ylabel('Log 1/R')
        ax2.set_xlim(np.min(wave),np.max(wave))
        self.dashborad.canvas1.draw()
        print("draw succ2")

    def meancen2(self):
        global file,wave,x,s,g,meanC

        xx = x.shape[0]
        xy = x.shape[1]
        mean_x=np.sum(x,axis =0)
        mean_x=mean_x / xx
        meand=np.tile(mean_x,(xx,1))
        meanC=(x - meand)

        self.dashborad.figure2.clear() 

        ax = self.dashborad.figure2.add_subplot(121)
        for i in range (x.shape[0]):  
            ax.plot(wave.tolist(),x[i].tolist())
        ax.set_xlabel('wavelenght, nm')
        ax.set_ylabel('log 1/R')
        ax.set_xlim(np.min(wave),np.max(wave))
        
        ax2 = self.dashborad.figure2.add_subplot(122)
        for i in range (x.shape[0]):  
            ax2.plot(wave,meanC[i])
        ax2.set_xlabel('wavelenght, nm')
        ax2.set_ylabel('Log 1/R')
        ax2.set_xlim(np.min(wave),np.max(wave))

        self.dashborad.canvas2.draw()
        print("draw succ3")

    def snv(self):
        global file,wave,x,s,g,snv_data

        xx = x.shape[0]
        xy = x.shape[1]
        mean_x=np.mean(x,axis =1)
        std_d=np.std(x,axis=1)
        meand=np.tile(mean_x,(xy,1)).T
        stdd=np.tile(std_d,(xy,1)).T
        
        snv_data= (x - meand) / stdd
        
        self.dashborad.figure3.clear()         
        ax = self.dashborad.figure3.add_subplot(121)
        for i in range (x.shape[0]):  
            ax.plot(wave.tolist(),x[i].tolist())
        ax.set_xlabel('wavelenght, nm')
        ax.set_ylabel('log 1/R')
        ax.set_xlim(np.min(wave),np.max(wave))
        
        ax2 = self.dashborad.figure3.add_subplot(122)
        for i in range (x.shape[0]):  
            ax2.plot(wave,snv_data[i])
        ax2.set_xlabel('wavelenght, nm')
        ax2.set_ylabel('Log 1/R')
        ax2.set_xlim(np.min(wave),np.max(wave))

        self.dashborad.canvas3.draw()
        print("draw succ4")
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())
