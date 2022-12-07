from PyQt5 import QtCore, QtWidgets
from brownie import accounts
import sys
class LoadAccount(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Load Account")
        Dialog.resize(271, 131)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(90, 90, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 21, 19))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 19))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 171, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 50, 171, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.account = None
        self.backend(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ID:"))
        self.label_2.setText(_translate("Dialog", "Password:"))

    def backend(self, Dialog):
        self.buttonBox.accepted.connect(lambda: self.load(Dialog))

    def load(self, Dialog):
        accId = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        if accId == "" or pwd =="":
            QtWidgets.QMessageBox.critical(Dialog, "Error: Empty input", "ID or password is empty", defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            try:
                self.account = accounts.load(accId, pwd)
                Dialog.close()
            except Exception as e:
                print("Could not load brownie account", e)
                QtWidgets.QMessageBox.critical(Dialog, "Error: Brownie account", "Could not load account", defaultButton=QtWidgets.QMessageBox.Ok)
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
        


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = LoadAccount()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
