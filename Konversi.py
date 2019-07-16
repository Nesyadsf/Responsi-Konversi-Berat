import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Konversi(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 150)
        self.move(300, 300)
        self.setWindowTitle('Konversi Kg')#Nama Window

        self.label1 = QLabel()
        self.label1.setText('<b><font size=6 color=brown> Konversi KG! </font></b>')
        self.label2 = QLabel()
        self.label2.setText('Masukkan Berat (dalam Kg) : ')
        self.berat = QLineEdit()
        self.berat.setValidator(QIntValidator())#agar angka yang diketikkan menjadi Integer
        self.cekOns = QRadioButton()
        self.cekOns.setText('&ons')
        self.cekOns.setChecked(True)
        self.cekTon = QRadioButton()
        self.cekTon.setText('&ton')
        self.cekG = QRadioButton()
        self.cekG.setText('&g')
        self.cekKuintal = QRadioButton()
        self.cekKuintal.setText('&kuintal')

        self.resultLabel = QLabel('<b>Hasil: </b>')#menambilkan hasil dengan tampilan label
        self.checkButton = QPushButton('Konversi!')#nama PushButton

        Layout = QGridLayout()#layout pada label 1 dan 2
        Layout.addWidget(self.label1,0,0)
        Layout.addWidget(self.label2,1,0)
        Layout.addWidget(self.berat,1,1)

        hbox = QHBoxLayout()#layout horizontal untuk RadioButton
        hbox.addWidget(self.cekOns)
        hbox.addWidget(self.cekTon)
        hbox.addWidget(self.cekG)
        hbox.addWidget(self.cekKuintal)

        layout = QVBoxLayout()#layout vertikal untuk layout,horizontal,result label dan check button
        layout.addLayout(Layout)
        layout.addLayout(hbox)
        layout.addWidget(self.resultLabel)
        layout.addWidget(self.checkButton)
        layout.addStretch()

        self.setLayout(layout)
        self.checkButton.clicked.connect(self.checkButtonClick)#memanggil/membuat koneksi

    def checkButtonClick(self): #method
        berat = float(self.berat.text())
        if self.cekOns.isChecked():
            hasil = berat*10
            self.resultLabel.setText('<b><font color=green> Hasil Ons : </font></b>'+str(hasil))
        elif self.cekTon.isChecked():
            hasil = berat/1000
            self.resultLabel.setText('<b><font color=red> Hasil Ton : </font></b>'+str(hasil))
        elif self.cekG.isChecked():
            hasil = berat*1000
            self.resultLabel.setText('<b><font color=blue> Hasil Gram : </font></b>'+str(hasil))
        else:
            hasil = berat/100
            self.resultLabel.setText('<b><font color=orange> Hasil Kuintal : </font></b>'+str(hasil))

if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = Konversi()
    form.show()

    a.exec_()
