from PyQt5 import QtCore, QtGui, QtWidgets 
from loadAccount import *
from createAccount import *
from constructImage import *
import sys as s
from generate_metadata import *
import json, requests, platform
import ipfshttpclient

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 576)
        self.account = None
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 741, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        #self.graphicsView = QtWidgets.QGraphicsView(self.tab)
        #self.graphicsView.setGeometry(QtCore.QRect(380, 10, 350, 350))
        #self.graphicsView.setObjectName("graphicsView")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 40, 151, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(150, 70, 221, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(10, 220, 161, 18))
        self.label_image = QtWidgets.QLabel(self.tab)
        self.label_image.setEnabled(True)
        self.label_image.setGeometry(QtCore.QRect(380, 10, 350, 350))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 91, 16))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(150, 100, 221, 101))
        self.textEdit.setObjectName("textEdit")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 141, 16))
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(10, 280, 151, 18))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(10, 10, 185, 18))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 41, 16))
        self.label_4.setObjectName("label_4")
        self.signBtn = QtWidgets.QPushButton(self.tab)
        self.signBtn.setEnabled(True)
        self.signBtn.setGeometry(QtCore.QRect(200, 220, 80, 23))
        self.signBtn.setObjectName("signBtn")
        self.mintBtn = QtWidgets.QPushButton(self.tab)
        self.mintBtn.setEnabled(True)
        self.mintBtn.setGeometry(QtCore.QRect(200, 280, 80, 23))
        self.mintBtn.setObjectName("mintBtn")
        self.generateBtn = QtWidgets.QPushButton(self.tab)
        self.generateBtn.setEnabled(True)
        self.generateBtn.setGeometry(QtCore.QRect(200, 10, 80, 23))
        self.generateBtn.setObjectName("generateBtn")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        #self.graphicsView_2 = QtWidgets.QGraphicsView(self.tab_2)
        #self.graphicsView_2.setGeometry(QtCore.QRect(380, 10, 350, 350))
        #self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_image_1 = QtWidgets.QLabel(self.tab_2)
        self.label_image_1.setEnabled(True)
        self.label_image_1.setGeometry(QtCore.QRect(380, 10, 350, 350))
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 61, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 28, 101, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(210, 28, 80, 24))
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(20, 110, 41, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setEnabled(True)
        self.label_9.setGeometry(QtCore.QRect(20, 140, 121, 18))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setEnabled(True)
        self.label_10.setGeometry(QtCore.QRect(20, 80, 61, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(110, 80, 161, 16))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setEnabled(True)
        self.label_12.setGeometry(QtCore.QRect(110, 110, 261, 16))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setEnabled(True)
        self.label_13.setGeometry(QtCore.QRect(110, 140, 261, 191))
        self.label_13.setText("")
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 710, 21))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCreate_Account = QtWidgets.QAction(MainWindow)
        self.actionCreate_Account.setObjectName("actionCreate_Account")
        self.actionLoad_Account = QtWidgets.QAction(MainWindow)
        self.actionLoad_Account.setObjectName("actionLoad_Account")
        self.actionGet_NFT_by_Creator = QtWidgets.QAction(MainWindow)
        self.actionGet_NFT_by_Creator.setObjectName("actionGet_NFT_by_Creator")
        self.actionCreate_Account_2 = QtWidgets.QAction(MainWindow)
        self.actionCreate_Account_2.setObjectName("actionCreate_Account_2")
        self.actionLoad_Account_2 = QtWidgets.QAction(MainWindow)
        self.actionLoad_Account_2.setObjectName("actionLoad_Account_2")
        self.actionVerify_NFT = QtWidgets.QAction(MainWindow)
        self.actionVerify_NFT.setObjectName("actionVerify_NFT")
        self.menuSettings.addAction(self.actionCreate_Account_2)
        self.menuSettings.addAction(self.actionLoad_Account_2)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.api = None
        self.smartContract = None
        
        #print(self.api.id())
        try:
            #self.api = ipfsApi.Client('127.0.0.1', 5001)
            self.api = ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5001")
        except Exception as e:
            print('Couldn\'t connect to ipfs node', e)
            s.exit()
        try:
            self.smartContract = smartContract('settings.ini')
        except:
            #print('here1')
            s.exit()
        #smartContract.transferEther(20, "0x1d939efF66e4120C69434e89a95C19c0d4FE21c7")
        self.backend()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "2.) Sign:"))
        self.label_5.setText(_translate("MainWindow", "Description:"))
        self.label_6.setText(_translate("MainWindow", "Creator\'s nickname:"))
        self.label_3.setText(_translate("MainWindow", "3.) Mint NFT image:"))
        self.label.setText(_translate("MainWindow", "1.) Generate random image:"))
        self.label_4.setText(_translate("MainWindow", "Title:"))
        self.signBtn.setText(_translate("MainWindow", "Sign"))
        self.mintBtn.setText(_translate("MainWindow", "Mint"))
        self.generateBtn.setText(_translate("MainWindow", "Generate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Generate NFT"))
        self.label_7.setText(_translate("MainWindow", "Insert ID:"))
        self.pushButton.setText(_translate("MainWindow", "Get NFT"))
        self.label_8.setText(_translate("MainWindow", "Title:"))
        self.label_9.setText(_translate("MainWindow", "Description:"))
        self.label_10.setText(_translate("MainWindow", "Creator:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Get NFT by ID"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionCreate_Account.setText(_translate("MainWindow", "Create NFT"))
        self.actionLoad_Account.setText(_translate("MainWindow", "Get NFT by ID"))
        self.actionGet_NFT_by_Creator.setText(_translate("MainWindow", "Get NFT by Creator"))
        self.actionCreate_Account_2.setText(_translate("MainWindow", "Create Account"))
        self.actionLoad_Account_2.setText(_translate("MainWindow", "Load Account"))
        

    def backend(self):
        self.generateBtn.clicked.connect(self.generateImage)
        self.actionLoad_Account_2.triggered.connect(self.loadAccountWindow)
        self.actionCreate_Account_2.triggered.connect(self.createAccountWindow)
        self.signBtn.clicked.connect(self.sign)
        self.mintBtn.clicked.connect(self.mint)
        self.pushButton.clicked.connect(self.getNftById)

    def loadAccountWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = LoadAccount()
        self.ui.setupUi(self.window)
        self.window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.window.show()
        loop = QtCore.QEventLoop()
        self.window.destroyed.connect(loop.quit)
        loop.exec() 
        self.account = self.ui.account

    def createAccountWindow(self):
        self.ui = CreateAccount()
        self.Dialog = QtWidgets.QDialog()
        self.ui.setupUi(self.Dialog, self.smartContract)
        self.Dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.Dialog.show()
        loop = QtCore.QEventLoop()
        self.Dialog.destroyed.connect(loop.quit)
        loop.exec() 
        self.account = self.ui.account
        #print(self.account.address)
        
    def generateImage(self):
        self.img_ch = create_new_image()
        self.image = generate_image(self.img_ch)
        #self.image.show()
        self.loadImage(self.image.toqimage(), self.label_image)

    def sign(self):
        file_name = save_image(self.image)
        #print(file_name)
        self.img_ch['Creator'] = self.lineEdit_2.text()
        self.img_ch['Title'] = self.lineEdit.text()
        self.img_ch['Description'] = self.textEdit.toPlainText()
        if platform.system() == "Windows":
            res = self.api.add(f'.\\images\\{file_name}.png', pin=True)
        else:
            res = self.api.add(f'./images/{file_name}.png', pin=True)
        #print(res)
        #url = f"http://ipfs.io/ipfs/{res['Hash']}?filename={file_name}.png"
        url = f"http://127.0.0.1:8080/ipfs/{res['Hash']}?filename={res['Hash']}"
        self.img_ch['external_link'] = url
        tid = self.smartContract.getCurrentId()
        #print(tid)
        self.img_ch['tokenId'] = tid+1
        createMetadata(self.img_ch, file_name+".json")
        self.metadata = json.dumps(self.img_ch, indent=4)
        if platform.system() == "Windows":
            res = self.api.add(f'.\\metadata\\{file_name}.json')
        else:
            res = self.api.add(f'./metadata/{file_name}.json')
        mes = self.smartContract.getEthHash(self.metadata)
        self.signature = w3.eth.account.signHash(mes, self.account.private_key)
        

    def mint(self):
        tx = self.smartContract.mint(self.account.address, self.signature.signature, self.img_ch['Creator'], self.metadata)
        print(tx)

    def getNftById(self):
        tx1 = self.smartContract.getNFT(int(self.lineEdit_3.text()))
        #print(tx1)
        self.metadata = json.loads(tx1[0])
        print(self.metadata['external_link'])
        response = requests.get(self.metadata['external_link'],timeout=600)
        img = Image.open(BytesIO(response.content))
        self.loadImage(img.toqimage(), self.label_image_1)
        self.label_11.setText(self.metadata['Creator'])
        self.label_12.setText(self.metadata['Title'])
        self.label_13.setText(self.metadata['Description'])

    def loadImage(self, image, qlabel):
            self.scene = QtWidgets.QGraphicsScene(MainWindow)
            
            image_profile = image
            image_profile = image_profile.scaled(350,350, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
            qlabel.setPixmap(QtGui.QPixmap.fromImage(image_profile))
            
            #pixmap = image.scaled(340,340)
            #self.item = QtWidgets.QGraphicsPixmapItem(image)
            #self.scene.addItem(self.item)
            #self.graphicsView.setScene(self.scene)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
