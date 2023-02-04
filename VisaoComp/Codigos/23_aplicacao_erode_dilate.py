# -*- coding: utf-8 -*-

import cv2

img = cv2.imread("../Imagens/CirculosRuido.png", 0)

elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))

# Fazendo o erode nas imagens
imgProcessada = cv2.erode(img, elemento_estruturante, iterations=2)

# Dilatando as imagens
imgProcessada = cv2.dilate(imgProcessada, elemento_estruturante, iterations=2)

cv2.imshow("Imagem original",img)
cv2.imshow("Imagem processada",imgProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()


