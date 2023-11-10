"""

@author: mehdi


"""


import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import Scripts.ButtonThreades as Bt
import Scripts.res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 366)
        MainWindow.setWindowTitle("زیرنویس یاب")
        MainWindow.setWindowIcon(QtGui.QIcon(':/icons/index.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText("زیرنویس درکنار فیلم های شما قرار خواهد گرفت")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pbf = QtWidgets.QPushButton(self.centralwidget)
        self.pbf.setObjectName("pbf")
        self.verticalLayout.addWidget(self.pbf)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.pbmul = QtWidgets.QPushButton(self.centralwidget)
        self.pbmul.setObjectName("pbmul")
        self.verticalLayout.addWidget(self.pbmul)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.pbpa = QtWidgets.QPushButton(self.centralwidget)
        self.pbpa.setObjectName("pbpa")
        self.verticalLayout.addWidget(self.pbpa)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.pbf.clicked.connect(self.open_single_file)
        self.pbmul.clicked.connect(self.open_multiy_files)
        self.pbpa.clicked.connect(self.open_path_of_file)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "subtodl"))
        self.label.setText(_translate("MainWindow", "  یک فیلم را انتخاب کنید   "))
        self.pbf.setText(_translate("MainWindow", "بزن بریم"))
        self.label_2.setText(_translate("MainWindow", "چند فیلم رو انتخاب کنید "))
        self.pbmul.setText(_translate("MainWindow", "بزن بریم "))
        self.label_3.setText(_translate("MainWindow", "  ادرس یه پوشه را بدهید "))
        self.pbpa.setText(_translate("MainWindow", "بزن بریم"))

    def open_single_file(self):
        filename = QFileDialog.getOpenFileName()
        self.hi = Bt.ProcessThread(self, filename, 1)
        self.hi.start()
        self.hi.sending_mss.connect(self.textBrowser.append)
        self.hi.sending_bool.connect(self.pbf.setEnabled)
        self.hi.sending_bool.connect(self.pbmul.setEnabled)
        self.hi.sending_bool.connect(self.pbpa.setEnabled)
        
    def open_multiy_files(self):
        self.textBrowser.clearHistory()
        filename = QFileDialog.getOpenFileNames()
        self.hi = Bt.ProcessThread(self, filename, 2)
        self.hi.start()
        self.hi.sending_mss.connect(self.textBrowser.append)
        self.hi.sending_bool.connect(self.pbf.setEnabled)
        self.hi.sending_bool.connect(self.pbmul.setEnabled)
        self.hi.sending_bool.connect(self.pbpa.setEnabled)

    def open_path_of_file(self):
        try:
            filename = QFileDialog.getExistingDirectory()
            b_input_name = os.listdir(filename)
            pathoffolder = filename
            self.hi =Bt.ProcessThread(self, b_input_name, 3, pathoffolder)
            self.hi.start()
            self.hi.sending_mss.connect(self.textBrowser.append)
            self.hi.sending_bool.connect(self.pbf.setEnabled)
            self.hi.sending_bool.connect(self.pbmul.setEnabled)
            self.hi.sending_bool.connect(self.pbpa.setEnabled)
        except FileNotFoundError:
            pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    
    main()
