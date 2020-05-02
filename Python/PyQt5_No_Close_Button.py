import PyQt5.QtWidgets as ayq
import PyQt5.QtCore as core

app = ayq.QApplication([" "])
pencere = ayq.QWidget()

pencere.setWindowFlags(core.Qt.CustomizeWindowHint)

# Kapatma tuşunu yok ettik :)
# Destroyed the X button :)


pencere.setGeometry(100,100,200,200)

pencere.show()

app.exec_()