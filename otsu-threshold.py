import cv2
image = cv2.imread('IMG_20220615_145150.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#image = cv2.GaussianBlur(image,(5, 5),0)

#equalize_image = cv2.equalizeHist(image)
#ret2,th2 = cv2.threshold(image,60,255,cv2.THRESH_BINARY)
ret2,th2 = cv2.threshold(image,200,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print(ret2)
cv2.imwrite("equalized.jpg",th2)