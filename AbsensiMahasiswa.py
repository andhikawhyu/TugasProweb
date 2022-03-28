from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


con = pymysql.connect(
    database='absensi_mahasiswa', 
    user='root', password='', 
    host='localhost', 
    port=3306, autocommit=True)
cur = con.cursor()

class Ui_MainWindow(object): 
   
    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    
    def Konfirmasi(self):
        Nama_Lengkap = self.lineEditNamaLengkap.text()
        NIM = self.lineEditNIM.text()
        Mata_Kuliah = self.lineEditMataKuliah.text()
        Tanggal = self.Tanggal.text()
        insert = (Nama_Lengkap, NIM, Mata_Kuliah, Tanggal)
        print(insert)
        sql = """INSERT INTO absensi (Nama_Lengkap, NIM, Mata_Kuliah, Tanggal) VALUES (%s,%s,%s,%s)"""
        data = cur.execute(sql,insert)
        if(data):
            self.messagebox("Berhasil", "Absensi telah berhasil")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(486, 360)
        MainWindow.setStyleSheet("background-color: rgb(108, 255, 157);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 0, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setObjectName("label_5")

        self.lineEditNamaLengkap = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNamaLengkap.setGeometry(QtCore.QRect(130, 80, 231, 20))
        self.lineEditNamaLengkap.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.lineEditNIM = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNIM.setGeometry(QtCore.QRect(130, 110, 231, 20))
        self.lineEditNIM.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.lineEditMataKuliah = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditMataKuliah.setGeometry(QtCore.QRect(130, 140, 231, 20))
        self.lineEditMataKuliah.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.Tanggal = QtWidgets.QDateEdit(self.centralwidget)
        self.Tanggal.setGeometry(QtCore.QRect(130, 170, 110, 22))
        self.Tanggal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tanggal.setDisplayFormat("yyyy-MM-dd")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 220, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Konfirmasi)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 486, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nama Lengkap"))
        self.label_2.setText(_translate("MainWindow", "NIM"))
        self.label_3.setText(_translate("MainWindow", "Mata Kuliah"))
        self.label_4.setText(_translate("MainWindow", "Tanggal"))
        self.label_5.setText(_translate("MainWindow", "Absensi Mahasiswa"))
        self.pushButton.setText(_translate("MainWindow", "Konfirmasi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())