"""Em um sistema baseado em Visão Computacional, a etapa de
pré-processamento consiste em realçar objetos de interesse em imagens, facilitando segmentá-los posteriormente. Para realçar esses objetos, existem inúmeros procedimentos que podem ser realizados, como operações aritméticas, operações geométricas, métodos para ajuste de contraste e tratamento de ruído. Neste capítulo, vamos apresentá-los e exemplificá-los, bem como abordar os conceitos e os diferentes tipos de ruído em imagens"""

"Para alterar o valor de um determinado pixel da imagem, basta realizar a operação inversa: atribuir novos valores a um determinado elemento da matriz. Veja o exemplo:"

lista = ['a','b','c','d','e']


print(enumerate(lista))
for i, l in range(lista):
    print(i, l)