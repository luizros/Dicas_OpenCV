""""

------------------------------------------------------------------
Titulo: Histogramas de imagens                                   -
Compania: Universidade de Brasília                               -
Autor: Unbetables        Update: Luiz Felipe  Date: 08/05        -    
------------------------------------------------------------------


Histograma de imagens

O histograma de cores de uma imagem é a distribuição de frequência dos níveis de cinza em relação ao número de amostras. Essa distribuição nos fornece informações sobre a qualidade da
imagem, principalmente no que diz respeito à intensidade luminosa e ao contraste.

Vamos fazer alguns exemplos de histogramas usando imagens binárias, em tons de cinza e no formato RGB
"""

import cv2

imagem = cv2.imread("VisaoComp/Imagens/banana_binaria.bmp",0) #  O parâmetro 0 foi utilizado na função imread. Ele indica a leitura da imagem em tons de cinza; por esse motivo, os pixels brancos são representados pelo valor 255 e os pretos por 0.

x, y = imagem.shape
totalpixelsBranco = 0
totalpixelsPreto = 0

for linha in range(0,x):
    for coluna in range(0,y):
        if imagem[linha][coluna] == 255:
            totalpixelsBranco += 1
        if imagem[linha][coluna] == 0:
            totalpixelsPreto += 1
 
print("O total de pixels pretos é: {}\nO total de pixels brancos é: {}".format(totalpixelsPreto,totalpixelsBranco)) 

# Plotando histrograma facilmente utilizando matplolib

import numpy as	np
from time import sleep
from matplotlib	import pyplot as grafico

print("Digite 1 para ver o histograma da imagem binária\nDigite 2 para ver o histrograma da imagem em tons de cinza\nOpcao: ")
opcao = int(input())

if opcao == 1:
    imagem = cv2.imread("VisaoComp/Imagens/banana_binaria.bmp", 0)
    cv2.imshow('Banana - Digite qualquer tecla para continuar', imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    grafico.hist(imagem.ravel(), 256, [0,256]) # Observe que a função hist possui 3 parâmetros fundamentais: o primeiro é a imagem com a qual desejamos trabalhar, o segundo é o número de elementos distintos que podem ser representados, e o terceiro	indica o	intervalo entre os elementos
    grafico.show()
elif opcao == 2:
    # Histograma para imagens cinza
    imgGray = cv2.imread("VisaoComp/Imagens/frutas3.jpg")
    imgGray = cv2.cvtColor(imgGray, cv2.COLOR_RGB2GRAY)
    cv2.imshow('Frutas em cinza', imgGray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    grafico.hist(imgGray.ravel(), 256, [0,256])
    grafico.show()
else:
    print("Saindo", end="")
    for i in range(3):
        print('.', end="")
        sleep(1)




 