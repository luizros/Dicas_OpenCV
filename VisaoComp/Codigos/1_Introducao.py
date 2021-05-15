"""
------------------------------------------------------------------
Theme: Carregando imagens a partir de arquivos                   -
Company: Universidy of Brasília                                  -
Author: Unbetables        Update: Luiz Felipe  Date: 08/05      -    
------------------------------------------------------------------

"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

# EXIBINDO IMAGENS NA TELA COM OPENCV E PYPLOT 

img = cv2.imread('VisaoComp/Imagens/lena.jpg') # Este comando lê a imagem e retorna uma matriz de pixels em formato BGR

cv2.imshow("Imagem", img) # A função imshow mostra a imagem na tela

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # Vamos exibir também a mesma imagem mas agora com o comando imshow(). Como a img está em BGR, precisamos colocar em em RGB para exibila na tela corretamente

plt.show()

cv2.waitKey(0) # A função waitKey quando recebe como parâmetro o inteiro 0, espera o usuário digitar uma tecla para encerrar a exibição da figura 

cv2.destroyAllWindows() # Destroi todas as janelas abertas que ficaram

# Podemos ver o tipo de img com o seguinte comando ja conhecido em python

print(type(img)) # Com esse comando veremos que a essa imagem é um vetor de bits

# Agora basta usarmos acessarmos método shape de img para sabermos qual é a dimensoes da imagem. Vamos utilizar o método shape 

dimensoes = img.shape
print(dimensoes)
