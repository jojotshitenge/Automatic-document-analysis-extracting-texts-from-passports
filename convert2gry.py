#To convert all the passport to level gry color

from PIL import Image
import os

VALID_IMAGES = [".jpg",".gif",".png",".tga",".tif",".tiff",".bmp",".jpeg"]

def rgb2gry(_input, _output):
    for file in os.listdir(_input):
        ext = os.path.splitext(file)[1]
        if ext.lower() in VALID_IMAGES:
            name = os.path.splitext(file)[0]
            img = Image.open(_input + file).convert('LA')
            img.save(_output + name + '.png')
            print("-> Image " + name + '.png' + " convert success !")

