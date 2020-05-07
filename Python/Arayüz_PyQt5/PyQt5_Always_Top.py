import PyQt5.QtWidgets as ayq
import PyQt5.QtCore as core

app = ayq.QApplication([" "])
pencere = ayq.QWidget()

pencere.setWindowFlag(core.Qt.WindowStaysOnTopHint)

# HER ZAMAN USTTE AYARI !

pencere.setGeometry(100,100,200,200)

pencere.show()

app.exec_()