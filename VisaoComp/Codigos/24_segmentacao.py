# -*- coding: utf-8 -*-
import cv2

img = cv2.imread("VisaoComp/Imagens/cafe.jpeg", 0)

metodo = cv2.THRESH_BINARY_INV

ret, imgBinarizada = cv2.threshold(img, 135, 255, metodo)

cv2.imshow("Imagem Original", img)

cv2.imshow("Imagem Tratada", imgBinarizada)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Caso sua imagem apareça com falhas mesmo apos a segmentação, essas
# falhas podem ser facilmente resolvidas usando abertura e fechamento
