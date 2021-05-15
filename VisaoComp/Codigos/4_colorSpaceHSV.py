"""
------------------------------------------------------------------
Titulo: Trabalhando com imagens no espaço HSV                     -
Compania: Universidade de Brasília                                 -
Autor: Unbetables        Update: Luiz Felipe  Date: 08/05       -    
------------------------------------------------------------------

***********************Sistema de cores HSV***********************

H(Hue)

É a componente que define a cor. Pode ser vista fisicamente como o comprimento de onda dominante da value.

S(Saturation)

É a pureza ou intensidade da cor. Quanto maior o valor da
saturação, ais pura será a cor; quanto enor, ais próxima ao
seu om e inza la erá epresentada.

V(Value)

Este valor é referente ao brilho da cor, à luminosidade ou
escala e laridade. uanto aior uminosidade, u alor este
componente, mais próximo ao branco a cor será representada;
quanto menor, mais próxima ao preto.

"""

import cv2

imagem = cv2.imread("VisaoComp/Imagens/lena.jpg")

imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

hue, saturation, value = cv2.split(imagem) # Com a função split conseguimos separar os canais H, S e V. 

#Canais de cores
cv2.imshow("Canal hue", hue) 
cv2.imshow("Canal saturation", saturation)
cv2.imshow("Canal value", value)

#Salvando magens os anais eparados
cv2.imwrite("Imagens/lena-canal-hue.jpeg", hue)
cv2.imwrite("Imagens/lena-canal-saturation.jpeg", saturation)
cv2.imwrite("Imagens/lena-canal-azul.jpeg",  value)

lenajunta = cv2.merge((hue,saturation,value)) # Junta os canais
lenajunta = cv2.cvtColor(lenajunta, cv2.COLOR_HSV2BGR) # foi ecessário converter magem para o espaço RGB antes de exibi-la. É válido lembrar que nossos monitores  operam exibindo imagens representadas no spaço e cor GB , por este motivo, essa onversão é necessária.

cv2.imshow("Lena combinada HSV",lenajunta)
cv2.waitKey(0)
cv2.destroyAllWindows()