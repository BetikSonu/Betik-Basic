# pip3 install tesseract
# pip3 install pytesseract

import pytesseract as test
from PIL import Image

image = Image.open("rm.png")

abc = test.image_to_string(image) # Fena değil ginede :)
print(abc) # 

# HATA : https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i

# @BetikSonu