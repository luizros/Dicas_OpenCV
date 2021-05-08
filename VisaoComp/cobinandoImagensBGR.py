import cv2

imagem = cv2.imread("Imagens/lena.jpg") 

azul, verde, vermelho = cv2.split(imagem)

imagem = cv2.merge((azul,verde,vermelho))

cv2.imshow("Imagem combinada", imagem)

cv2.waitKey(0) # A função waitKey quando recebe como parâmetro o inteiro 0, espera o usuário digitar uma tecla para encerrar a exibição da figura 

cv2.destroyAllWindows() # Destroi todas as janelas abertas que ficaram

# Podemos ver o tipo de img com o seguinte comando ja conhecido em python