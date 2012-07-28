#!/usr/bin/python
from PIL import Image
from pydmtx import DataMatrix
import sys
import cv2.cv as cv

#Decoding data OpenCV
img  = cv.LoadImage(sys.argv[1])
dm = DataMatrix()
print dm.decode(img.width, img.height, img.tostring())

sys.exit(0)

#Decoding data
img = Image.open(sys.argv[1])
if img.mode != 'RGB':
   img = img.convert('RGB')
   
  dm = DataMatrix()

print dm.decode(img.size[0], img.size[1], buffer(img.tostring()))



'''
#Encode Data
dm.encode("Hello World")
dm.save("test.jpg","jpeg")
'''