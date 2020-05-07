import PyQt5.QtWidgets as ayq
import PyQt5.QtGui as gui
import PyQt5.QtCore as core
app = ayq.QApplication([" "])
pencere = ayq.QWidget()


loy = ayq.QVBoxLayout(pencere)

label = ayq.QLabel()
movi = gui.QMovie("loading.gif") # gif konum
label.setMovie(movi)
loy.addWidget(label)

movi.start()




pencere.show()
app.exec_()