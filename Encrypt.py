import cv2 as cv
import numpy as np


org_img = cv.imread('stag.png')
img = org_img.copy()

x = raw_input("Enter text: ")

lst = []
ord_lst = []
enc_ord_lst = []

for i in range(len(x)):
    lst.append(x[i])
    
for i in range(len(x)):
    ord_lst.append(ord(lst[i]))
    
    
length = len(ord_lst)
enc = []
enc = ord_lst


for i in range(length ,img.shape[1]):
    enc.append(0)
    
enc = np.array(enc)
enc = np.reshape(enc,(1,len(enc)))


enc = np.concatenate((enc,enc,enc),axis = 0)
img = img[1 : , : ]



enc = np.reshape(enc,(1,enc.shape[1],enc.shape[0]))

encoded = np.concatenate((enc,img),axis = 0)

cv.imwrite("Encoded.png",encoded)


print("Text is sucessfully encrypted in the image.")