# -*- coding: utf-8 -*-
import cv2

captura = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('VisaoComp/Codigos/haarcascade_frontalface_default.xml')

while True:
    
    ret, imagem = captura.read()
    img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    deteccoes = detector.detectMultiScale(img, minSize=(200,200))
    for (x,y,l,h) in deteccoes:
        cv2.rectangle(imagem, (x,y), (x+l, y+h), (255,0,0), 2) # Desenhando uma retngulo facilmente na imagem
        cv2.imshow('imagem',imagem)
        
    if cv2.waitKey(1) & 0xFF in [ord("q"), ord('Q')]: # Espera o usuário pressionar a letra 'q' do teclado
        break # quebra o loop infinito
    
captura.release()
cv2.destroyAllWindows()

