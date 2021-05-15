"""
------------------------------------------------------------------
Titulo: Trabalhando com imagens no espaço RGB                    -
Compania: Universidade de Brasília                               -
Autor: Unbetables        Update: Luiz Felipe  Date: 08/05        -    
------------------------------------------------------------------

"""
import cv2
import numpy as np 
import matplotlib.pyplot as plt

imagem = cv2.imread("VisaoComp/Imagens/lena.jpg")

azul, verde, vermelho = cv2.split(imagem) # Geralmente, a biblioteca OpenCV trata o espaço de cor RGB (red, green, blue) como BGR (blue, green, red), invertendo a ordem dos canais. Por este motivo, quando utilizamos a função split , conforme demonstrado no código, declaramos as variáveis na sequência azul, verde, vermelho.

#Canais de cores
cv2.imshow("Canal Azul", azul) 
cv2.imshow("Canal Verde", verde)
cv2.imshow("Canal Vermelho", vermelho)

#Salvando	imagens	dos	canais	separados
cv2.imwrite("VisaoComp/Imagens/frutas-canal-vermelho.jpeg",	vermelho)
cv2.imwrite("VisaoComp/Imagens/frutas-canal-verde.jpeg",	verde)
cv2.imwrite("VisaoComp/Imagens/frutas-canal-azul.jpeg", azul)

imagem = cv2.merge((azul,verde,vermelho))
cv2.imshow("Imagem combinada", imagem)

cv2.waitKey(0) # A função waitKey quando recebe como parâmetro o inteiro 0, espera o usuário digitar uma tecla para encerrar a exibição da figura 

cv2.destroyAllWindows() # Destroi todas as janelas abertas que ficaram

# Podemos ver o tipo de img com o seguinte comando ja conhecido em python


