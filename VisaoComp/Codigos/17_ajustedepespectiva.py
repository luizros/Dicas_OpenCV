"""
------------------------------------------------------------------
Titulo: Transformações geométricas                               -
Compania: Universidade de Brasília                               -
Autor: Unbetables        Update: Luiz Felipe  Date: 21/05        -    
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

import numpy as np 
import cv2 
import matplotlib.pyplot as plt


imagem = cv2.imread("VisaoComp/Imagens/sudoku.jpg")

img = plt.imread(imagem)

plt.imshow(img)

plt.show()

cv2.waitKey(0)

cv2.destroyAllWindows()