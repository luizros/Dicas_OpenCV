# -*- coding: utf-8 -*-
"""
Capturando com videos com a webcam
"""

import numpy as np
import cv2

# A função VideoCapture() é bem parecida com a imread(), sendo a única diferença sua 
# forma de exibir o video, que nada é do que imagens sendo exibidas numa determinada
# frequência(quadros per segundos). O método VideoCapture(0) recebe os parâmetros in
# teiros de 0 até n, sendo n o número de dispositivos de captura conectados em ordem
# no seu desktop
captura = cv2.VideoCapture(0)

while True:

    # cap.read() retorna um bool (True / False). Se o quadro for lido corretamente, será
    # True. Portanto, você pode verificar o final do vídeo verificando este valor de retorno.
    ret, frame = captura.read()
     
    # mostra cada frame para o usuário
    cv2.imshow("Imagem", frame) 
    
    # Espera o usuário pressionar a tecla 'q' do teclado
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break # quebra o loop infinito
    
captura.release()

cv2.destroyAllWindows()

