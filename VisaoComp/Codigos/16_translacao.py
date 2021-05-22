"""
------------------------------------------------------------------
Titulo: Operação e translação                                    -
Compania: Universidade de Brasília                               -
Autor: Unbetables        Update: Luiz Felipe  Date: 21/05        -    
------------------------------------------------------------------

Como vimos anteriormete, uma matriz de rotação rotaciona nossa imagem
. Agora para deslocar uma imagem precisamos tb de uma matriz de translação.
Vamos utilizar a mesma função que usamos para rotacionar a nossa imagem, mas
so que agora passando uma matriz de translação

"""

import numpy as np 
import cv2 

import cv2


imagem = cv2.imread("VisaoComp/Imagens/lena.jpg")

# aqui obtemos as dimensões da imagem
linhas, colunas = imagem.shape[:2]

# Criando a matriz de translação. O	último elemento	do primeiro	vetor indica 
# a	quantidade de pixels referente	ao deslocamento	 horizontal.
matriz = np.float32([[1,0,100],[0,1,100]]) 

# Transladamos a imagem com warpAffine
imagemrotacionada = cv2.warpAffine(imagem, matriz, (linhas, colunas))

cv2.imshow('Imagem rotacionada',imagemrotacionada)

cv2.waitKey(0)

cv2.destroyAllWindows()