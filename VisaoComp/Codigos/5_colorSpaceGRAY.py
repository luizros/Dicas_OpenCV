# -*- coding: utf-8 -*-
"""
Espaço de cores cinza                                         

---------------------------------------------------------------------
Curiosidade

É válido mencionar que a imagem em tons de cinza, após a conversão,
é gerada a partir da soma ponderada dos canais de cor vermelho, ver
de e azul. Nessa soma, os canais vermelho e verde apresentam um peso
(coeficiente de ponderação) maior quando comparado ao canal azul, jus
tamente pelo fato do olho humano ser mais sensível a essas cores.

---------------------------------------------------------------------
"""
import cv2

# Ler imagem. Lembre de colocar o caminho correto da pasta!
imagem = cv2.imread("Imagens/lena.jpg") 

# Converte de RGB para tons de cinza
imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY) 

# Mostra a imagem
cv2.imshow("Lena cinza", imagem) 

cv2.waitKey(0) 

cv2.destroyAllWindows() 





