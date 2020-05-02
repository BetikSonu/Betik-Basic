import PyQt5.QtWidgets as ayq
import PyQt5.QtGui as gui
import PyQt5.QtCore as core

class pencere(ayq.QMainWindow):
    def __init__(self):
        super().__init__()
        self.kodlama()

    def kodlama(self):
        self.setWindowTitle("Merhaba . Yenim açılıyor !")
        self.setGeometry(100,100,400,500)
        self.other()
        timer=core.QTimer(self)
        timer.singleShot(3000,self.other_close) # 3 saniye bekle , kapatma define istek at


    def other(self):
        self.other = ayq.QDialog(self)
        self.other.setGeometry(100,100,500,300)
        self.other.show()
        

    def other_close(self):
        self.other.close()


app = ayq.QApplication([" "])
penc = pencere()
penc.show()
app.exec_()