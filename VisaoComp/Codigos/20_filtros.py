"""
Tratamento de imagens com ruídos

Filtro: Filtro Media

O filtro de média é um filtro linear, classificado como passa-baixas,
ou seja, para suavização de imagens. Ele substitui cada pixel da ima
gem pelo valor médio de sua vizinhança. Quanto maior a ordem da matriz
que representa a máscara, maior será o número de pixels vizinhos consi
derados, logo, mais intenso será o efeito de suavização.

Filtro: Filtro Gaussiana

Assim como o filtro de média, o gaussiano também é um filtro li
near, passa-baixas.Três parâmetros são necessários para execução
desse método.O primeiro deles é a imagem a ser tratada; o segun
do, a dimensão da matriz que representa a máscara de filtragem; 
e o último, o grau de suavização.

Filtro: Filtro mediana

Matematicamente, este filtro atua alterando o valor de cada pixel
-alvo pela mediana estatística dos valores dos pixels vizinhos. O
método medianBlur da biblioteca OpenCV nos permite aplicá-lo a ima
gens. Apenas dois parâmetros são necessários para utilizá-lo. O pri
meiro deles é a imagem que receberá o tratamento, e o segundo é um 
valor inteiro, ímpar e positivo, que indicará a sua intensidade.
"""

import cv2

img_ruido = cv2.imread('VisaoComp/Imagens/lena_ruido.png')

# Aplicando o filtro média
img_blur = cv2.blur(img_ruido, (5,5))

# Aplicando o filtro Gaussiano
img_gaussian = cv2.GaussianBlur(img_ruido, (5,5),0)

# Aplicando o filtro Mediana
img_median = cv2.medianBlur(img_ruido, 5)

# Aplicando o filtro Bilateral
img_bilateral = cv2.bilateralFilter(img_ruido, 9, 75,75)

cv2.imshow('Imagem original', img_ruido)
cv2.imshow('Imagem filtrada: Filtro Media', img_blur)
cv2.imshow('Imagem filtrada: Filtro Gaussiano', img_gaussian)
cv2.imshow('Imagem filtrada: Filtro Mediana', img_median)
cv2.imshow('Imagem filtrada: Filtro Bilateral', img_bilateral)


cv2.waitKey(0)
cv2.destroyAllWindows()


