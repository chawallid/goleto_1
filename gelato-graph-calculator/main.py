import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QFileDialog, QLabel
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from dashborad import Ui_MainWindow as Ui_Dashborad
from prepro import Ui_MainWindow as Ui_Prepro
from SystemConfig import Ui_MainWindow as Ui_SystemConfig

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
    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:/', "files (*.xlsx)")
        imagePath = fname[0]
        file = imagePath.split("/")
        
        self.systemconfig.label_1_.setText(file[len(file)-1])
    
        # print(file[len(file)-1])
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())