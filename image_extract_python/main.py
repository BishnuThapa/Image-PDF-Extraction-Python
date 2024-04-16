from pytesseract import pytesseract
from PIL import Image


path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Open the image file
image = Image.open('image.png')

# Perform OCR using PyTesseract
pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
