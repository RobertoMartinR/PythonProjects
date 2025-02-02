import cv2
import glob

images = glob.glob("*.jpg")

for img in images:
    img = cv2.imread(img,0)
    resized_image = cv2.resize(img, (100, 100))
    cv2.imshow("Hey", resized_image)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_", + img, resized_image)

