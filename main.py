import pytesseract
from PIL import Image

img = Image.open("phone_number.png")

# you need to download tesseract: https://github.com/UB-Mannheim/tesseract/wiki
# then change the local path to tesseract.exe

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(img)

with open("phone_number.txt", "r+") as text_file:
    text_file.write(text)
