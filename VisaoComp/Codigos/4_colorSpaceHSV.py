# -*- coding: utf-8 -*-
"""
Espaço de cores HSV

**********************Sistema de cores HSV***********************

H(Hue)

É a componente que define a cor. Pode ser vista fisicamente como o com
primento de onda dominante da value

S(Saturation)

É a pureza ou intensidade da cor. Quanto maior o valor da
saturação, mais pura será a cor; quanto menor, mais próxima ao
seu tom e cinza ela será representada

V(Value)

Este valor é referente ao brilho da cor, à luminosidade ou
escala e claridade. 

"""

import cv2

imagem = cv2.imread("VisaoComp/Imagens/lena.jpg")

imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Com a função split conseguimos separar os canais H, S e V.
hue, saturation, value = cv2.split(imagem)  

#Canais de cores
cv2.imshow("Canal hue", hue) 
cv2.imshow("Canal saturation", saturation)
cv2.imshow("Canal value", value)

#Salvando magens os canais separados
cv2.imwrite("Imagens/lena-canal-hue.jpeg", hue)
cv2.imwrite("Imagens/lena-canal-saturation.jpeg", saturation)
cv2.imwrite("Imagens/lena-canal-azul.jpeg",  value)

# Junta os canais
lenajunta = cv2.merge((hue,saturation,value)) 

 # Foi ecessário converter imagem para o espaço RGB antes de exibi-la.
 # É válido lembrar que nossos monitores operam exibindo imagens repre
 # sentadas no espaço e cor RGB , por este motivo, essa conversão se 
 # torna sempre necessária.
lenajunta = cv2.cvtColor(lenajunta, cv2.COLOR_HSV2BGR)

cv2.imshow("Lena combinada HSV",lenajunta)
cv2.waitKey(0)
cv2.destroyAllWindows()