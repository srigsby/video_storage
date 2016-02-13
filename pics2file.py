#!/usr/bin/python
from sys import argv
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

f = open("reconstruct.mp4","wb")

for x in xrange(98):
	g = open("out"+str(x+1)+".jpg")
	data = g.read()
	g.close()
	f.write(data)
	

f.close()