import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from calculateprogram.code_python import FirstDev,SecondDev,meancen2,snv,msc 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import random

global wave,x,s,g 
X = pd.read_excel("gelato-graph-calculator\TEST_S5G5.xlsx", sheet_name='X', header = None)
wl = pd.read_excel("gelato-graph-calculator\TEST_S5G5.xlsx", sheet_name='wl', header = None)

wave = np.array(wl).reshape(-1)
x = np.array(X)
s =5
g = 5 
  

class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        # self.toolbar =  
       
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.button = QPushButton('Plot')

        

        self.button.clicked.connect(self.FirstDev)
        layout = QVBoxLayout()
        # layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def FirstDev(self):
        global wave,x,s,g
        xx = x.shape[0]
        xy = x.shape[1]
        sd1= np.zeros([xx,xy])
        for i in range(int(s + g / 2 + 0.5), int(xy - s - g / 2 + 0.5)):
            sa=np.mean(x[:,int(i - s - g / 2 + 0.5):int(i - g / 2 - 0.5)], axis = 1)
            sc=np.mean(x[:,int(i + g / 2 + 0.5):int(i + g / 2 - 0.5 + s)], axis = 1)
            sd1[:,i]=sc - sa
     
        self.figure.clear()
        ax = self.figure.add_subplot(121)
        for i in range (x.shape[0]):  
            ax.plot(wave.tolist(),x[i].tolist())

        ax.set_xlabel('wavelenght, nm')
        ax.set_ylabel('log 1/R')
        ax.set_xlim(np.min(wave),np.max(wave))

        ax2 = self.figure.add_subplot(122)
        for i in range (x.shape[0]):  
            ax2.plot(wave.tolist(),sd1[i].tolist())
        ax2.set_xlabel('wavelenght, nm')
        ax2.set_ylabel('Log 1/R')
        ax2.set_xlim(np.min(wave),np.max(wave))

        self.canvas.draw()
        

    # def getWave(self):
    #     X = pd.read_excel("TEST_S5G5.xlsx", sheet_name='X', header = None)
    #     wl = pd.read_excel("TEST_S5G5.xlsx", sheet_name='wl', header = None)
    #     wave = np.array(wl).reshape(-1)
    #     x = np.array(X)
    #     s =5
    #     g= 5

        # FirstDev(wave,x,s,g)[0].show()
        # SecondDev(wave,x,s,g)[0].show()
        # meancen2(wave,x)[0].show()
        # snv(wave,x)[0].show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())