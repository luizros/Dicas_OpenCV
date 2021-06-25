# -*- coding: utf-8 -*-

""""
Elementos estruturantes

Esse elemento pode ser visto como uma imagem binária, menor 
que a imagem original, armazenado geralmente em uma matriz 
quadrada

Assim como os filtros espaciais, a matriz que representa o 
elemento estruturante que percorrerá toda a imagem a ser tra
tada. Nesse processo, uma determinada operação morfológica se
rá realizada pixel a pixel na imagem, alterando o valor de ca
da um deles para seguir o padrão definido por esse elemento

Temos três elementos estruturantes principais

# Retangular
[[1, 1, 1, 1, 1,
[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1]]


# Elipse

[[0, 0, 1, 0, 0,
[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1],
[0, 0, 1, 0, 0]]

# Cruz

[[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0]]


Podem ser utilizador para:
    - Realce de bordas
    - Eliminação das linhas verticais e horizontais com elementos
estruturantes no formato de linhas e colunas.

"""

import cv2
import numpy as np

# Vamos trabalhar com a operação morfológica de erosão
#   A operação de erosão é caracterizada pela corrosão das arestas
#   do objeto de interesse, resultando em uma imagem "encolhida" do
#   objeto.

imagemOriginal = cv2.imread("VisaoComp/Imagens/Circulos.png", 0)

elementoEstruturante1 = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
elementoEstruturante2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
elementoEstruturante3 = cv2.getStructuringElement(cv2.MORPH_CROSS, (7,7))


imagemProcessada_ret = cv2.erode(imagemOriginal, elementoEstruturante1, iterations = 2)
imagemProcessada_eli = cv2.erode(imagemOriginal, elementoEstruturante2, iterations = 2)
imagemProcessada_cruz = cv2.erode(imagemOriginal, elementoEstruturante3, iterations = 2)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Estrutura retangular", imagemProcessada_ret)
cv2.imshow("Estrutura elipse", imagemProcessada_eli)
cv2.imshow("Estrutura cruz", imagemProcessada_cruz)

cv2.waitKey(0)
cv2.destroyAllWindows()

