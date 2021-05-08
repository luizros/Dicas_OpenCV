import numpy as np
import cv2

captura = cv2.VideoCapture(0) # A função VideoCapture() é bem parecida com a imread(), sendo a única diferença sua forma de capturar, que neste caso, são vídeos. Dessa forma essa função captura videos da webcam quando recebe os parâmetros inteiros de 0 até n, sendo n o número de de webcans do seu desktop

while True:

    ret, frame = captura.read() # cap.read () retorna um bool (True / False). Se o quadro for lido corretamente, será True. Portanto, você pode verificar o final do vídeo verificando este valor de retorno.
    cv2.imshow("Imagem", frame) # mostra cada frame para o usuário
    
    if cv2.waitKey(1) & 0xFF == ord("q"): # Espera o usuário pressionar a letra 'q' do teclado
        break # quebra o loop infinito
    
captura.release()

cv2.destroyAllWindows()

