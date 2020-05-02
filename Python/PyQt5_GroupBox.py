import PyQt5.QtWidgets as ayq
import sys


class pencere(ayq.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(20,100,600,400)

        self.grup= ayq.QGroupBox("Merhaba ben Grup !",self)
        self.grup.setGeometry(10,10,300,200)
        
        self.layout = ayq.QGridLayout()  # gridlayout'unu ekledik !
        self.grup.setLayout(self.layout) # grup elemanına eleman eklemek için layout kullanmamız gerekiyor !

        self.buton = ayq.QPushButton("Ben Buton !") # SELF'i eklemedik !

        self.layout.addWidget(self.buton)

        self.radio = ayq.QRadioButton("Ben Radio")

        self.layout.addWidget(self.radio)




uyg = ayq.QApplication(sys.argv)
penc = pencere()
penc.show()
uyg.exec_()
