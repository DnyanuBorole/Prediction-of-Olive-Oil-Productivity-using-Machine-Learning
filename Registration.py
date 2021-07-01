from PyQt5 import QtCore, QtGui, QtWidgets
from DBconn import DBConnection
import sys

class Ui_Reg(object):
    def __init__(self, dialog):
        self.Dialog = dialog

    def alertmsg(self, title, Message):
        self.warn = QtWidgets.QMessageBox()
        self.warn.setIcon(QtWidgets.QMessageBox.Information)
        self.warn.setWindowTitle(title)
        self.warn.setText(Message)
        self.warn.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.warn.exec_()



    def registration(self):

        try:
            name = self.lineEdit.text()
            uid = self.lineEdit_2.text()
            pwd = self.lineEdit_3.text()
            mno = self.lineEdit_4.text()
            self.lineEdit_4.setValidator(QtGui.QIntValidator())

            mydb = DBConnection.getConnection()
            cursor = mydb.cursor()
            query = "INSERT INTO  userdetails (Name,UserId,Password,MobNo) VALUES (%s,%s,%s,%s)"
            val = (name, uid, pwd,mno)
            if name == '' or name == "null" or uid == '' or uid == "null" or pwd == '' or pwd == "null" or mno=="null" or mno=="":
                self.alertmsg("failed", "Please fill the All Details")
            else:
                cursor.execute(query, val, )
                mydb.commit()
                cursor.close()
                mydb.close()
                self.alertmsg("Successfull", "Registered")
                self.Dialog.hide()
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(487, 649)
        Dialog.setStyleSheet("QDialog{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(39, 127, 179, 252));}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(103, 160, 91, 41))
        self.label.setStyleSheet("font: 75 13pt \"Arial\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(57, 220, 161, 41))
        self.label_2.setStyleSheet("font: 75 13pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(62, 280, 161, 41))
        self.label_3.setStyleSheet("font: 75 13pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 340, 161, 41))
        self.label_4.setStyleSheet("font: 75 13pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(201, 159, 221, 34))
        self.lineEdit.setStyleSheet("font: 12pt \"Arial\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 217, 221, 34))
        self.lineEdit_2.setStyleSheet("font: 12pt \"Arial\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 280, 221, 34))
        self.lineEdit_3.setStyleSheet("font: 12pt \"Arial\";")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 340, 221, 34))
        self.lineEdit_4.setStyleSheet("font: 12pt \"Arial\";")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 430, 151, 41))
        self.pushButton.setStyleSheet("font: 75 16pt \"Arial\";\n"
"background-color: rgb(203, 58, 104);")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(120, 50, 241, 51))
        self.label_5.setStyleSheet("font: 75 22pt \"Tahoma\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(218, 218, 218, 222), stop:1 rgba(255, 255, 255, 255));")
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setLineWidth(2)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.registration)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Name "))
        self.label_2.setText(_translate("Dialog", "UserName"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.label_4.setText(_translate("Dialog", "Mobile No."))
        self.pushButton.setText(_translate("Dialog", "Submit"))
        self.label_5.setText(_translate("Dialog", "Registration"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Reg(Dialog)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
