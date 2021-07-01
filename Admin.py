
from PyQt5 import QtCore, QtGui, QtWidgets
from Training import Ui_Training
from Testing import Ui_Testing
from SelectDistrict import Ui_district


class Ui_Admin(object):
    def training(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Training()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
    def testing(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Testing()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1100, 750)
        Dialog.setStyleSheet("QDialog{background-image: url(../OlivePrediction/Images//admbck.jpg);}")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(390, 280, 311, 391))
        self.frame.setStyleSheet("QFrame{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(179, 179, 179, 213));}")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(44, 50, 231, 41))
        self.label.setStyleSheet("font: 75 20pt \"Verdana\";")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(70, 190, 181, 44))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(179, 62, 87);\n"
"font: 16pt \"Britannic Bold\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 280, 181, 44))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(179, 62, 87);\n"
"font: 16pt \"Britannic Bold\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.training)
        self.pushButton_2.clicked.connect(self.testing)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Admin"))
        self.pushButton.setText(_translate("Dialog", "Training"))
        self.pushButton_2.setText(_translate("Dialog", "Testing"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Admin()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
