# -*- coding: utf-8 -*-
"""
Detector de face usando Haarcascade em imagens
"""
import cv2

imagem = cv2.imread("VisaoComp/Imagens/lena.jpg")

detector = cv2.CascadeClassifier('VisaoComp/Codigos/haarcascade_frontalface_default.xml')

img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

deteccoes = detector.detectMultiScale(img)

print(deteccoes) # O primeiro elemento do vetor indica a posição x que inicia e o segundo a posição y

print(len(deteccoes)) # Mostra a quantidade de faces, nessa caso so teremos uma, mas o detector posso indicar falsos positivos que podem ser removidos com a alteração de fatores de escala


# Criando o bolding-box

for (x,y,l,h) in deteccoes:
    cv2.rectangle(imagem, (x,y), (x+l, y+h), (0,255,0), 2) # Desenhando uma retngulo facilmente na imagem
    cv2.imshow('Lena',imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()