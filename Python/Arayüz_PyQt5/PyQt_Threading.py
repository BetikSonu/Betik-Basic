import PyQt5.QtWidgets as ayq
from threading import Thread
import time

class eleman(ayq.QWidget):
    def __init__(self):
        super().__init__()
        
        self.kodlama()


    def kodlama(self):
        self.setGeometry(100,100,100,100)

        self.grid = ayq.QGridLayout()
        buton = ayq.QPushButton("BUTON",self)
        self.grid.addWidget(buton)
        self.label = ayq.QLabel("BEN LABEL")
        self.grid.addWidget(self.label)
        self.setLayout(self.grid)

        buton.clicked.connect(self.buton)

        #buton.clicked.connect(lambda dongu:self.arkacil()) # Bunu kullanırsak çarpıya bassak dahi program kapanmaz çünkü threading işlemine devam ediyor !
        # O yüzden başka bir def'i threadingi açmak içni kullanıyoruz
        # pngmerkez.org | @pngmerkez | @linuxdepo | @kekikakademi | @overclick
        
        
        # buton.clicked.connect(lambda ... | if we use this code , our widget never close . Why ? Python wait threading job . And threading suspend sys.exit .
        # but if we use " .daemon = True " , Threading allow exit

    def buton(self):
        print("THREADING AÇILIYOR") # Threading opening

        the = Thread(target=self.arkacil)
        the.daemon = True # sys.exit gelince threadingin durması için | threading stop sys.exit
        the.start()


    def arkacil(self):
        while 1:
            print("Merhaba Ben Arkaplanda çlışıyorum :)") # Hi , i work in background
            time.sleep(10)

        
        


UYGULAMA = ayq.QApplication(["PNG"])
pencere = eleman()
pencere.show()
UYGULAMA.exec_()

# @raifpy | 
