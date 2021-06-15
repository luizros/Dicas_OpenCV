# -*- coding: utf-8 -*-
"""
------------------------------------------------------------------
Titulo: Transformações geométricas                               -                           -
Autor: UnBetables        Update: Luiz Felipe  Date: 21/05        -    
------------------------------------------------------------------

O posicionamento incorreto da lente ou até mesmo o balanço da câmera 
podem interferir na perspectiva da fotografia, causando inclinação ou
distorção do objeto representado na imagem. Em fotografias que possuem
linhas horizontais, verticais ou formas geométricas, as distorções tor
nam-se ainda mais perceptíveis. Para corrigir as distorções de perspecti
va, podemos usar a função  warpPerspective  da biblioteca OpenCV. Ela 
ajusta a perspectiva de uma imagem tendo como referência uma matriz
predefinida de pontos, gerada pela função getPerspectiveTransform.
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

imagem = cv2.imread("VisaoComp/Imagens/sudoku.jpg")

#use o imshow do matplotlib para saber os pontos de interesse
#plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))


# nº ---------local---------   x   y
# 1º ponto(superior esquerdo) 167 214
# 2º ponto(inferior esquerdo) 109 810
# 3º ponto(superior direito)  810 183
# 4º ponto(inferior direito)  879 782


pontosIniciais = np.float32([[167,214], [810,183], [109,810], [879,782]])

pontosFinais = np.float32([[0,0], [600,0], [0,600], [600,600]])

matriz = cv2.getPerspectiveTransform(pontosIniciais, pontosFinais)

Imagemnova = cv2.warpPerspective(imagem, matriz, (600, 600))

cv2.imshow("Imagem Original", imagem)
cv2.imshow("Imagem Nova", Imagemnova)

cv2.waitKey(0)
cv2.destroyAllWindows()

plt.show()

