#!/usr/bin/env python
# coding: utf-8

import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract


img1  = cv2.imread('captchas/captcha004.png',0)
img2 = cv2.imread('captchas/captcha015.png',0)


def showImage(img):
    cv2.imshow('something',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   

croppedImg1 = img1[11:67,42:178]
croppedImg2 = img2[11:67,42:178]


blurImg1 = cv2.medianBlur(croppedImg1,3)
blurImg2 = cv2.medianBlur(croppedImg2,3)

def removeLineNoise(inputImg):
    img = inputImg
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            flag = False
            if(img[i,j]!=50 and img[i,j]!=255):
                for k in range(img.shape[0]):
                    if(img[k,j]==50):
                        flag = True

                if(flag):
                    img[i,j]=50
                else:
                    img[i,j]=255
    return img

outputImg1 = removeLineNoise(blurImg1)
outputImg2 = removeLineNoise(blurImg2)

blurOutput1  = cv2.medianBlur(outputImg1,3)
blurOutput2 = cv2.medianBlur(outputImg2,3)

textOutput1 = pytesseract.image_to_string(blurOutput1)
print(textOutput1)


textOutput2 = pytesseract.image_to_string(blurOutput2)
print(textOutput2)
