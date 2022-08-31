import pytesseract
from PIL import Image

# Specify the title + extension of the picture you are translating into text:

#picture_name = 'phone_number.png'
#picture_name = 'ru_text.jpg'
picture_name = 'eng_text.jpg'
img = Image.open(picture_name)

# You need to download tesseract: https://github.com/UB-Mannheim/tesseract/wiki  During the installation, 
# you need to select the Additional language data option and select the desired languages

# Then change the local path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
file_name = img.filename.split('.')[0]
text = pytesseract.image_to_string(img, lang='rus')

with open(f'{file_name}.txt', 'w') as text_file:
    text_file.write(text)
