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
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

from dashborad import Ui_MainWindow as Ui_Dashborad
from prepro import Ui_MainWindow as Ui_Prepro
from SystemConfig import Ui_MainWindow as Ui_SystemConfig
from calculateprogram.code_python import FirstDev,SecondDev,meancen2,snv,msc 
file = ""

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
        global file
        print(file)

        X = pd.read_excel(file, sheet_name='X', header = None)
        wl = pd.read_excel(file, sheet_name='wl', header = None)
        wave = np.array(wl).reshape(-1)
        x = np.array(X)
        s =5
        g= 5

        FirstDev(wave,x,s,g)[0].show()
        SecondDev(wave,x,s,g)[0].show()
        meancen2(wave,x)[0].show()
        snv(wave,x)[0].show()

        # spmsc = msc(x)

        # print(spmsc)

        # spmsc,mscval = msc(x,nargout = 2)
        # print(spmsc,mscval)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())
