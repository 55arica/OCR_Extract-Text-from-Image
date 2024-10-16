pip install pytesseract
pip install pillow


# ----------------------------------------------------------------------------------


import pytesseract
from PIL import Image

img_path = " "

image = Image.open(imh_path)
extraction = pytesseract.text_to_string(image)

cleaned_txt = extraction.strip()



https://medium.com/@pawan329/ocr-extract-text-from-image-in-8-easy-steps-3113a1141c34
