# -*- coding: utf-8 -*-
"""
Limiarização 
"""
import cv2 as cv

img = cv.imread('VisaoComp/Imagens/limiar.png') # Carregando em tons de cinza

limiar, imgLimiar = cv.threshold(img, 180, 255, cv.THRESH_BINARY) 

cv.imshow("Limiar", imgLimiar)
cv.waitKey(0)
cv.destroyAllWindows()
