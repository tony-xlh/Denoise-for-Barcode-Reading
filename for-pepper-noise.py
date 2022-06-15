import cv2
img = cv2.imread("noise-sample.jpg")
medianBlur = cv2.medianBlur(img, 5)
cv2.imwrite("medianBlur.jpg",medianBlur)