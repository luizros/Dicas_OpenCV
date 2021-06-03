# -*- coding: utf-8 -*-
"""
------------------------------------------------------------------
Titulo: Histogramas de imagens RGB usando OPENCV e Pyplot        -
Compania: Universidade de Brasília                               -
Autor: Unbetables        Update: Luiz Felipe  Date: 08/05        -    
------------------------------------------------------------------

"""
import cv2
import numpy as np 
import matplotlib.pyplot as plt 

imagem = cv2.imread('Imagens/frutas3.jpg')
img = cv2.imread('Imagens/frutas2.jpg')
color = ('b','g','r') # Criamos uma tupla para usarmos no nosso programa

for i, col in enumerate(color):
    histr = cv2.calcHist([imagem,img], [i], None, [256], [0,256]) # Esta função calcula o histograma de nossa imagem. Ela recebe como parâmetros a imagem, o canal, a máscara onde será feito o histograma, a quantidade de intensidade e o valor onde ela vai variar. O valor de hist será uma matriz 256x1 
    print(histr)
    plt.plot(histr, color = col) # Plota no gráfico os valores 
    plt.xlim([0,300]) # Delimita os valores o eixo x
    
cv2.imshow("Imagem Original", imagem)
plt.xlabel('Valores de pixels') # Legenda do eixo x 
plt.ylabel('Nº de pixels') # Legenda do eixo y
plt.show() # Mostra o gráfico
cv2.waitKey(0) # Quebra as janelas quando digitar qlq tecla
cv2.destroyAllWindows()