# -*- coding: utf-8 -*-
"""
------------------------------------------------------------------
Titulo: Transformações geométricas                               -
Compania: Universidade de Brasília                               -
Autor: Unbetables        Update: Luiz Felipe  Date: 21/05        -    
------------------------------------------------------------------

Muitas vezes precisamos aplicar transformações geométricas em imagens.
Estas transformações consistem em invertê-la horizontalmente ou ver
ticalmente, rotacioná-la, ajustar sua escala ou pespectiva

A opereção de rotação consite em girar a imagem em um ângulo predeterminado.
Para realizar essa operação, duas funções da biblioteca OpenCV são necessá
rias: a getRotationMatrix2D e a warAffine. Sendo a primeira utilizada para 
obter a matriz de rotação e a segunda para receber essa matriz como parâme
tro. A função getRotationMatrix2D tem os como parâmetros: center, angle e 
scale

O parâmetro center da função getRotationMatrix2D indica o centro da imagem, 
ou seja, uma coordenada definida por dois pontos. O primeiro deles é o total
de colunas dividido por 2; o segundo, o total de linhas dividido por 2. O se
gundo parâmetro, angle , define o ângulo no qual desejamos rotacionar a imagem,
que pode variar de 0° até 360°. O último parâmetro, scale , é o fator de escala.
Para manter a imagem com a mesma dimensão, basta atribuir o valor 1.
"""

import cv2


imagem = cv2.imread("VisaoComp/Imagens/lena.jpg")

# aqui obtemos as dimensões da imagem
linhas, colunas, p = imagem.shape

# Criando a matriz de rotação
matriz = cv2.getRotationMatrix2D((linhas/2,colunas/2), 60, 1) 

# Rotacionamos a imagem com warpAffine
imagemrotacionada = cv2.warpAffine(imagem, matriz, (linhas, colunas))

cv2.imshow('Imagem rotacionada',imagemrotacionada)

cv2.waitKey(0)

cv2.destroyAllWindows()