import cv2 as cv
import numpy as np

img = cv.imread('Encoded.png')

img = np.reshape(img[0], (img[0].shape[0]*img[0].shape[1]))


enc = []
for i in img:
    if (i != 0):
        enc.append(i)
    else:
        break
        
final_txt = ''

for i in enc:
    final_txt += (chr(i))
    
print(final_txt)