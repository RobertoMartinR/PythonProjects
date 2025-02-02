import cv2

img = cv2.imread("Image_and_Video_Processing\galaxy.jpg",0)

print(type(img))
print(img)


resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(0) # En este parámetro poniendo 0 la imagen se cerrará al pulsar una tecla, puedes poner 2000 y se cerrará a los 2 segundos ya que considera qeue son ms
cv2.destroyAllWindows()