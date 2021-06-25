# -*- coding: utf-8 -*-
import cv2

# Dilatação

# A operação de dilatação é o oposto da operação de erosão.
#   Nesse procedimento, a área do objeto de interesse será 
#   dilatada, ou seja, o objeto do primeiro plano ficará maior
#   do que era inicialmente.

imagemOriginal = cv2.imread("VisaoComp/Imagens/Circulos.png", 0)

elementoEstruturante1 = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
elementoEstruturante2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
elementoEstruturante3 = cv2.getStructuringElement(cv2.MORPH_CROSS, (7,7))


imagemProcessada_ret = cv2.dilate(imagemOriginal, elementoEstruturante1, iterations = 2)
imagemProcessada_eli = cv2.dilate(imagemOriginal, elementoEstruturante2, iterations = 2)
imagemProcessada_cruz = cv2.dilate(imagemOriginal, elementoEstruturante3, iterations = 2)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Estrutura retangular", imagemProcessada_ret)
cv2.imshow("Estrutura elipse", imagemProcessada_eli)
cv2.imshow("Estrutura cruz", imagemProcessada_cruz)

cv2.waitKey(0)
cv2.destroyAllWindows()
