# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QT\Olive Oil Prediction\Testing.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Performance import evaluation
from DBconn import DBConnection
from PerformanceTable import view_data


class Ui_Testing(object):
    def accuracy(self):
        evaluation()
    def performance(self):
        try:
            self.Dialog = QtWidgets.QDialog()
            self.ui = view_data()
            self.ui.setupUi(self.Dialog)
            self.ui.performance()
            self.Dialog.show()
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[1]
            print(tb.tb_lineno)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(929, 612)
        Dialog.setStyleSheet("QDialog{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(15, 134, 201, 180));}")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(310, 180, 311, 361))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(218, 218, 218, 222), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(70, 130, 181, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(189, 45, 105);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 230, 181, 51))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(189, 45, 105);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Arial\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 30, 163, 45))
        self.label.setStyleSheet("font: 75 18pt \"Tahoma\";")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.accuracy)
        self.pushButton_2.clicked.connect(self.performance)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Accuracy"))
        self.pushButton_2.setText(_translate("Dialog", "Performance"))
        self.label.setText(_translate("Dialog", "Testing"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Testing()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
