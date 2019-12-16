#Importations nécessaires

import sys
import os
from subprocess import call
#from convert2gry import *
from bs4 import BeautifulSoup
from PIL import Image
import argparse
import requests

VALID_IMAGES = [".jpg",".gif",".png",".tga",".tif",".tiff",".bmp",".jpeg"]
FNULL = open(os.devnull, 'w')

class ArgumentMissingException(Exception):
	def __init__(self):
		print("usage: {} <dirname>".format(sys.argv[0]))
		sys.exit(1)
        
def rgb2gry(_input, _output):
    for file in os.listdir(_input):
        ext = os.path.splitext(file)[1]
        if ext.lower() in VALID_IMAGES:
            name = os.path.splitext(file)[0]
            img = Image.open(_input + "/" + file).convert('LA')
            img.save(_output + "/" + name + '.png')
            print("-> Image " + name + '.png' + " convert success !")
            
def create_directory(path):
	if not os.path.exists(path):
	    os.makedirs(path)

def check_path(path):
	return bool(os.path.exists(path))

def getPage(path):
    page = requests.get(path)
    page.status_code
    
def main(input_path, output_path):
	if call(['which', 'tesseract']):
		print("tesseract-ocr missing, use sudo apt-get install tesseract-ocr to resolve")
	elif check_path(input_path):

		count = 0
		other_files = 0

		for f in os.listdir(input_path):
			ext = os.path.splitext(f)[1]

			if ext.lower() not in VALID_IMAGES:
				other_files += 1
				continue
			else :

				if count == 0:
					create_directory(output_path)
				count += 1
				image_file_name = os.path.join(input_path, f)
				filename = os.path.splitext(f)[0]
				filename = ''.join(e for e in filename if e.isalnum() or e == '-')
				text_file_path = os.path.join(output_path,filename)
				call(["tesseract", image_file_name, text_file_path, "-l eng+fr", "hocr"], stdout=FNULL)

                
				print(str(count) + (" file" if count == 1 else " files") + " completed")
                
                
		if count + other_files == 0:
			print("No files found at your given location")
		else :
			print(str(count) + " / " + str(count + other_files) + " files converted")
			print("Extraction terminé avec succèss " + str(count) + " files")
            
	else :
		print("No directory found at " + format(input_path))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir_rbg", help="Input directory where input images rbg are stored")
    parser.add_argument("input_dir_gry", help="Input directory where output images gry are stored")
    parser.add_argument('output_dir', nargs='?', help="(Optional) Output directory to store converted text (default: {input_path}/converted-text)")
    args = parser.parse_args()
    input_path_rbg = os.path.abspath(args.input_dir_rbg)
    input_path_gry = os.path.abspath(args.input_dir_gry)
    if args.output_dir:
        output_path = os.path.abspath(args.output_dir)
    else:
        output_path = os.path.join(input_path_gry,'converted-text')
    rgb2gry(input_path_rbg, input_path_gry)
    main(input_path_gry, output_path)
