# -*- coding: utf-8 -*-
"""
Capturando imagens
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

# EXIBINDO IMAGENS NA TELA COM OPENCV E PYPLOT 

# Este comando lê a imagem e retorna uma matriz de pixels em formato BGR
img = cv2.imread('VisaoComp/Imagens/lena.jpg')

# A função imshow mostra a imagem na tela
cv2.imshow("Imagem", img)

# Vamos exibir também a mesma imagem, mas agora com o comando imshow() do plt.
# Como a img está em BGR, precisamos colocar ela em RGB para exibila na
# tela corretamente na tela no plyplot
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# Vamos exibir também utilizando o método show() do pyplot
plt.show()

# Usamos o waitkey(0) para exibir infinitamente o script da imagem na tela
cv2.waitKey(0)

# Fecha corretamente todas as janelas que foram abertas
cv2.destroyAllWindows()

# Podemos ver o tipo de img com o type()
print(type(img)) 

# Agora basta usarmos o shape para vermos as dimensões da img
dimensoes = img.shape
print(dimensoes)
