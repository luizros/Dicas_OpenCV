# -*- coding: utf-8 -*-
"""
------------------------------------------------------------------
Titulo: Carregando imagens a partir de arquivos                  -
Compania: Universidade de Brasília                               -
Autor: Unbetables        Update: Luiz Felipe  Date: 20/05        -    
------------------------------------------------------------------

"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

# EXIBINDO IMAGENS NA TELA COM OPENCV E PYPLOT 

# Este comando lê a imagem e retorna uma matriz de pixels em formato BGR
img = cv2.imread('VisaoComp/Imagens/lena.jpg')

# A função imshow mostra a imagem na tela
cv2.imshow("Imagem", img)

# Vamos exibir também a mesma imagem, mas agora com o comando imshow().
# Como a img está em BGR, precisamos colocar ela em RGB para exibila na
# tela corretamente na tela
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# Vamos exibir também utilizando o método show() do pyplot
plt.show()

# A função waitKey quando recebe como parâmetro o inteiro 0, espera o
# usuário digitar uma tecla para encerrar a exibição da figura
cv2.waitKey(0)

# Fecha corretamente todas as janelas que foram abertas
cv2.destroyAllWindows()

# Podemos ver o tipo de img com o seguinte comando type() que já é bem
# conhecido em python
print(type(img)) # Verificamos que uma imagem é uma matriz de pixels

# Agora basta usarmos o método shape do obejeto img para sabermos quais 
# são as dimensoes da imagem
dimensoes = img.shape
print(dimensoes)
