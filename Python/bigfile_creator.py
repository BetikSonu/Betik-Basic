import os

_1gb = 1024**3 

veri = os.urandom(_1gb)

with open("1gb_veri","wb") as yaz:
    yaz.write(veri)
 
 
#PNG Notları
