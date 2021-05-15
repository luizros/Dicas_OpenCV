"""
------------------------------------------------------------------
Titulo: Trabalhando com imagens em tons de cinza                 -
Compania: Universidade de Brasília                               -
Autor: Unbetables        Update: Luiz Felipe  Date: 08/05c       -    
------------------------------------------------------------------

É válido mencionar que a imagem em tons de cinza, após a conversão, é gerada a partir da soma ponderada dos canais de cor vermelho, verde e azul. Nessa soma, os canais vermelho e verde apresentam um peso (coeficiente de ponderação) maior quando comparado ao canal azul, justamente pelo fato do olho humano ser mais sensível a essas cores.

"""
import cv2

imagem = cv2.imread("VisaoComp/Imagens/lena.jpg") # Ler imagem. Lembre de colocar o caminho correto da pasta!

imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY) # Converte de RGB para tons de cinza

cv2.imshow("Lena cinza", imagem) # Mostra a imagem

cv2.waitKey(0) # Fecha a imagem após digitar qualquer tecla 

cv2.destroyAllWindows() 





