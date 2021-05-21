"""
------------------------------------------------------------------
Titulo: Carregando imagens a partir de arquivos                  -
Compania: Universidade de Brasília                               -
Autor: Unbetables        Update: Luiz Felipe  Date: 08/05        -    
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
# tela corretamente

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# Vamos exibis também utilizando o método show() do pyplot
plt.show()

# A função waitKey quando recebe como parâmetro o inteiro 0, espera o
# usuário digitar uma tecla para encerrar a exibição da figura
cv2.waitKey(0)

# Destroi todas as janelas abertas que ficaram
cv2.destroyAllWindows()

# Podemos ver o tipo de img com o seguinte comando ja conhecido em python
print(type(img)) # Verificamos que uma imagem é uma matriz de pixels

# Agora basta usarmos acessarmos método shape de img para sabermos qual é
# a dimensoes da imagem. Vamos utilizar o método shape
dimensoes = img.shape
print(dimensoes)
