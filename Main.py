from PyQt5 import QtCore, QtGui, QtWidgets
from Admin import Ui_Admin
from Registration import Ui_Reg
from DBconn import DBConnection
from SelectDistrict import Ui_district



class Ui_Main(object):
    def alertmsg(self, title, Message):
        self.warn = QtWidgets.QMessageBox()
        self.warn.setIcon(QtWidgets.QMessageBox.Information)
        self.warn.setWindowTitle(title)
        self.warn.setText(Message)
        self.warn.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.warn.exec_()
    def clear(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
    def reg(self):
        try:
            self.regi = QtWidgets.QDialog()
            self.ui = Ui_Reg(self.regi)
            self.ui.setupUi(self.regi)
            self.regi.show()
        except Exception as e:
            print("Error"+e.args[1])
            tb = sys.exc_info()[2]
            print("Line no",tb.tb_lineno)
    def admlog(self):
        try:
            unm = self.lineEdit.text()
            pwd = self.lineEdit_2.text()
            mydb = DBConnection.getConnection()
            cursor = mydb.cursor()
            cursor.execute("SELECT UserId,Password from userdetails where UserId like '" + unm + "'and Password like '" + pwd + "'")
            if unm=="null" or unm=="" or pwd == "null" or pwd == "":
                self.alertmsg("Error","Please Enter UserName and Password")
            elif unm=="admin" and pwd=="admin":
                self.Dialog = QtWidgets.QDialog()
                self.ui = Ui_Admin()
                self.ui.setupUi(self.Dialog)
                self.Dialog.show()
            elif (len(cursor.fetchall()) > 0):
                self.Dialog = QtWidgets.QDialog()
                self.ui = Ui_district()
                self.ui.setupUi(self.Dialog)
                self.Dialog.show()
            else:
                self.alertmsg("Failed","Invalid Username and Password")
        except Exception as e:
            print("Error" + e.args[0])
            tb = sys.exc_info()[2]
            print("Line no", tb.tb_lineno)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1100, 750)
        Dialog.setStyleSheet("QDialog{background-image: url(../OlivePrediction/Images/99305.jpg);}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 20, 971, 81))
        self.label.setStyleSheet("font: 63 24pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(208, 255, 205);\n"
"")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(410, 230, 371, 451))
        self.frame.setStyleSheet("QFrame{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(165, 165, 165, 138));}")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(60, 160, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(172, 234, 227);\n"
"font: 14pt \"Arial\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 250, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(172, 234, 227);\n"
"font: 14pt \"Arial\";")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(110, 310, 151, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("font: 87 16pt \"Arial\";\n"
"background-color: rgb(179, 62, 87);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 370, 301, 21))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("font: 75 italic 11pt \"Arial\";\n"
"text-decoration: underline;\n"
"color: rgb(255, 255, 0);")
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.admlog)
        self.pushButton_2.clicked.connect(self.reg)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Prediction of Olive Oil Productivity using Machine Learning"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "UserName"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "PassWord"))
        self.pushButton.setText(_translate("Dialog", "Login"))
        self.pushButton_2.setText(_translate("Dialog", "Click Here for Create New Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Main()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
