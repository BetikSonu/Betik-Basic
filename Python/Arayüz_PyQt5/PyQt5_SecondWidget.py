import PyQt5.QtWidgets as ayq

class pencere(ayq.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(30,30,400,400)

        self.kodlama()

    def kodlama(self):
        buton = ayq.QPushButton("Press me",self)
        buton.clicked.connect(self.second)

    
    # SECOND WIDGET * (dialog but not problem :D)
    def second(self):
        widget = ayq.QDialog(self)
        widget.setWindowTitle("Hi :D")
        widget.setGeometry(100,100,300,200)

        buton2 = ayq.QPushButton("DONT PRESS ME",widget)
        buton2.move(100,100)

        widget.show()


uyg = ayq.QApplication([" "])
pen = pencere()
pen.show()

uyg.exec_()
