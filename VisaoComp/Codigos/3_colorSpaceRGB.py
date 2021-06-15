# -*- coding: utf-8 -*-
"""
Espaço de cores RGB

"""
import cv2
import numpy as np 
import matplotlib.pyplot as plt

imagem = cv2.imread("VisaoComp/Imagens/lena.jpg")

# Geralmente, o OpenCV trata o espaço de cor RGB (red, green, blue) como
# BGR (blue, green, red), invertendo a ordem dos canais. Por este motivo,
# quando utilizamos a função split, conforme demonstrado abaixo no código,
# declaramos as variáveis na sequência azul, verde, vermelho
azul, verde, vermelho = cv2.split(imagem) 

#Canais de cores
cv2.imshow("Canal Azul", azul) 
cv2.imshow("Canal Verde", verde)
cv2.imshow("Canal Vermelho", vermelho)

#Salvando as imagens dos canais separadamente
cv2.imwrite("VisaoComp/Imagens/lena-canal-vermelho.jpeg",	vermelho)
cv2.imwrite("VisaoComp/Imagens/lena-canal-verde.jpeg", verde)
cv2.imwrite("VisaoComp/Imagens/lena-canal-azul.jpeg", azul)

imagem = cv2.merge((azul,verde,vermelho))
cv2.imshow("Imagem combinada", imagem)

# A função waitKey quando recebe como parâmetro o inteiro 0, espera o usuário
# digitar uma tecla para encerrar a exibição da figura
cv2.waitKey(0) 

# Fecha corretamente todas as janelas
cv2.destroyAllWindows() 


