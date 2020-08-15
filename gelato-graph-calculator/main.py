import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QFileDialog, QLabel
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib.figure import Figure
# from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from dashborad import Ui_MainWindow as Ui_Dashborad
from prepro import Ui_MainWindow as Ui_Prepro
from SystemConfig import Ui_MainWindow as Ui_SystemConfig
from calculateprogram.code_python import FirstDev,SecondDev,meancen2,snv,msc 

file = ""
global wave,x,s,g 


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

    def getImage(self):
        global file
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:/', "files (*.xlsx)")
        imagePath = fname[0]

        file = fname[0]

        file_tmp = imagePath.split("/")
        self.systemconfig.label_1_.setText(file_tmp[len(file_tmp)-1])

    def getWave(self):
        global file,wave,x,s,g 
        print(file)
        X = pd.read_excel(file, sheet_name='X', header = None)
        wl = pd.read_excel(file, sheet_name='wl', header = None)
        # print("pastmp")
        wave = np.array(wl).reshape(-1)
        x = np.array(X)
        s =5
        g= 5

        self.FirstDev()
        self.SecondDev()
        self.meancen2()
        self.snv()
        

        # spmsc = msc(x)

        # print(spmsc)  

        # spmsc,mscval = msc(x,nargout = 2)
        # print(spmsc,mscval)
    def FirstDev(self):
        global file,wave,x,s,g 
    
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
        global file,wave,x,s,g 
       
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
        global file,wave,x,s,g 

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
        global file,wave,x,s,g 

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
