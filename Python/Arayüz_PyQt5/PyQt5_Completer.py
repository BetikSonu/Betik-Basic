import PyQt5.QtWidgets as ayq

class pencere(ayq.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(30,30,400,400)

        self.kodlama()

    def kodlama(self):
        self.line = ayq.QLineEdit(self)
        self.line.setGeometry(100,100,100,100)

        tamamlanacaklar = "@linuxdepo @pngmerkez @kekiksiber @overclick Merhaba".split() # liste | list ( .. .. .. .. Hi)

        tamamla = ayq.QCompleter(tamamlanacaklar) # tamamlanacak listesini tanımla 

        self.line.setCompleter(tamamla) # listeyi input'a tanıt .


uyg = ayq.QApplication([" "])
pen = pencere()
pen.show()

uyg.exec_()

#