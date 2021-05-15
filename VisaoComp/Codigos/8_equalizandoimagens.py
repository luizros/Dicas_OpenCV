"""
------------------------------------------------------------------
Theme: Carregando imagens a partir de arquivos                   -
Company: Universidy of Brasília                                  -
Author: Unbetables        Update: Luiz Felipe  Date: 08/05       -    
------------------------------------------------------------------
"""

import cv2
import numpy as np
from matplotlib import pyplot as grafico

imagemOriginal = cv2.imread("Imagens/valvula.jpg", 0)
imagemEqualizada = cv2.equalizeHist(imagemOriginal)

cv2.imshow("Imagem Original", imagemOriginal)
cv2.imshow("Imagem Equalizada", imagemEqualizada)

grafico.hist(imagemOriginal.ravel(), 256, [0,256])
grafico.figure();
grafico.hist(imagemEqualizada.ravel(), 256, [0,256])
grafico.show()