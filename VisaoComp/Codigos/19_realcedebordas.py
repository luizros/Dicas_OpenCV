# -*- coding: utf-8 -*-
"""
Realce de bordas
"""
import cv2

img = cv2.imread('VisaoComp/Imagens/parking.png')

# Operador de sobel
sobelx = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)
sobely = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)

# Operdador laplaciano
laplacian = cv2.Laplacian(img, cv2.CV_8U)



cv2.imshow('Original', img)
cv2.imshow('Sobel X', sobelx)
cv2.imshow('Sobel Y', sobely)
cv2.imshow('Operador Laplaciano', laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()