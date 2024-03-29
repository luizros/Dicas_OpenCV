# -*- coding: utf-8 -*-
"""
Com a função add também podemos somar a intensidade de cor
para cada pixel da nossa imagem 

"""

import cv2
import numpy as np 
from matplotlib import pyplot as plt


imagem = cv2.imread("../Imagens/valvula.jpg")

imagemClara = cv2.add(imagem, 30)
imagemEscura = cv2.add(imagem,-30)


cv2.imshow("Imagem Original", imagem)
cv2.imshow("Imagem Clara", imagemClara)
cv2.imshow("Imagem Escura", imagemEscura)

# Vamos fazer os histogramas para visualizar essas imagens
cv2.waitKey(0)

plt.figure("Histograma Imagem Original")
plt.hist(imagem.ravel(),256,[0,256])

plt.figure("Histograma Imagem Clara")
plt.hist(imagemClara.ravel(),256,[0,256])

plt.figure("Histograma Imagem Escura")
plt.hist(imagemEscura.ravel(),256,[0,256])

plt.show()
cv2.waitKey(0)

