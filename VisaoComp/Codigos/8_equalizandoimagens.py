# -*- coding: utf-8 -*-
"""
------------------------------------------------------------------
Titulo: Equalizando imagens                                      -
Compania: Universidade de Brasília                               -
Autor: Unbetables        Update: Luiz Felipe  Date: 21/05        -    
------------------------------------------------------------------
Equalizando imagens

Digamos que você possui uma imagem em baixa qualidade e deseja melhorar
sua vizualização. Um dos métodos mais utilzados para tratar esse tipo de
problema é a equalização de imagens por histograms, que consiste em aumen
tar o contraste da imagem. 

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