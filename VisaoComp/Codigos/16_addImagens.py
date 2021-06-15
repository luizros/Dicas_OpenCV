# -*- coding: utf-8 -*-
"""
Vamos trabalhar agora com a operação de adição. ELa consiste 
em somar os valores dos pixels de uma imagem com outra(s), o
no final resultará em uma nova imagem. 
"""

import cv2


imagem1 = cv2.imread("VisaoComp/Imagens/desenho1.png")
imagem2 = cv2.imread("VisaoComp/Imagens/desenho2.png")

# Somando as duas imagens. Utilizamos a função add que recebe
# dois parâmetro que são as nossas duas imagens
imagem = cv2.add(imagem1,imagem2)

# Salvando nossa nova imagem
cv2.imwrite("VisaoComp/Imgens/desenho3",imagem)

# Exibindo nossa imagem
cv2.imshow("Imagem Nova", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
