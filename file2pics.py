#!/usr/bin/python
from sys import argv
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# reads first arg as file location of file to be chopped
width, height = 1280, 720
script, first = argv
def bytes_for(m,n): return m*n*3
f = open(first,"rb")
x=0
chunk_read="initialize"
try:
	while chunk_read != "":
		chunk_size = bytes_for(width,height)
		chunk_read = f.read(chunk_size)
		try:
			img = Image.frombuffer('RGB', (width,height), chunk_read, 'raw', 'RGB', 0, 1)
			draw = ImageDraw.Draw(img)
			img.save("test"+str(x)+".jpg")
		except ValueError:
			chunk_read = chunk_read.ljust(chunk_size, '\0')
			img = Image.frombuffer('RGB', (width,height), chunk_read, 'raw', 'RGB', 0, 1)
			draw = ImageDraw.Draw(img)
			img.save("test"+str(x)+".jpg")
			chunk_read = ""
		x+=1
finally:
	f.close()

print chunk_read