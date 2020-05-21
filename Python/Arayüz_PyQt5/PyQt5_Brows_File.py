import PyQt5.QtWidgets as ayq
from PyQt5 import QtGui,QtCore

ay = ayq.QApplication([" "])
pn = ayq.QMainWindow()
pn.setGeometry(100,100,600,400)

#fileName,_= ayq.QFileDialog.getOpenFileName(pn, 'Single File', "/home")
fileName=ayq.QFileDialog.getExistingDirectory(pn,"AntiBetik | @BetikSonu","/home")
print(fileName)


pn.show()
ay.exec_()

        