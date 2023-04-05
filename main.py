#### first install tessaract library from this link for windows
#### https://github.com/UB-Mannheim/tesseract/wiki
#### now import these two packages using pip
#### pip install pytesseract
#### pip install pillow


from PIL import Image
from pytesseract import pytesseract
import os
import time

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Define path to images folder, place your images in images folder then run this program
path_to_images = r'images/'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

# starting time
start = time.time()

#Get the file names in the directory
for root, dirs, file_names in os.walk(path_to_images):
    #Iterate over each file name in the folder
    for file_name in file_names:
        #Open image with PIL
        img = Image.open(path_to_images + file_name)

        #Extract text from image
        text = pytesseract.image_to_string(img)

        print(text)
        # below code just create a new text file for every image and extracted code in that file
        result = file_name.split(".", 1)[0]
        with open(result+".txt", 'w') as f:
            f.write(text)

# end time
end = time.time()

# total time taken
print(f"Runtime of the program is {end - start}")