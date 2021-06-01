import cv2

img = cv2.imread('VisaoComp/Imagens/mon.jpg', 0)

imgFiltrada = cv2.Laplacian(img, cv2.CV_8U)

imgRealcada = cv2.subtract(img, imgFiltrada)

cv2.imshow("Original", img)
cv2.imshow("Filtrada", imgFiltrada)
cv2.imshow("Realcada", imgRealcada)

cv2.waitKey(0)

cv2.destroyAllWindows()