# -*- coding: utf-8 -*-
"""
Histogramas de imagens RGB      

"""
import cv2
import numpy as np 
import matplotlib.pyplot as plt 

imagem = cv2.imread('../Imagens/frutas3.jpg')
img = cv2.imread('../Imagens/frutas2.jpg')

color = ('b','g','r') # Criamos uma tupla para usarmos no nosso programa

for i, col in enumerate(color):
    histr = cv2.calcHist([imagem,img], [i], None, [256], [0,256]) 
    # A função calcHist() calcula o histograma de nossa imagem. Ela recebe como parâ
    # metros: uma ou mais imagens, o canal, a máscara onde será feito o histograma, a
    # quantidade de intensidade e o valor onde ela vai variar. O valor de histr será 
    # uma matriz 256x1 
    
    print(histr)
    plt.plot(histr, color = col) # Plota no gráfico os valores 
    plt.xlim([0,300]) # Delimita os valores o eixo x
    
plt.xlabel('Valores de pixels') # Legenda eixo x 
plt.ylabel('pixels') # Legenda eixo y
plt.show() # Mostra gráfico
cv2.imshow("Imagem Original", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()