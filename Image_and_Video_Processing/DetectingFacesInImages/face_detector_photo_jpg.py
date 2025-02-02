import cv2  # Import the OpenCV library

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier("Image_and_Video_Processing\DetectingFacesInImages\haarcascade_frontalface_default.xml")

# Read the image from the specified path
img = cv2.imread("Image_and_Video_Processing\DetectingFacesInImages\photo.jpg")

# Convert the image to grayscale (required for Haar Cascade detection)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the grayscale image
faces = face_cascade.detectMultiScale(gray_img,
                                      scaleFactor=1.05,  # Specifies how much the image size is reduced at each image scale
                                      minNeighbors=5)  # Specifies how many neighbors each candidate rectangle should have to retain it

# Loop through all detected faces and draw rectangles around them
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)  # Green rectangle with thickness 3

# Print the type and coordinates of detected faces
print(type(faces))
print(faces)

# Resize the image to one-third of its original size to fit on the screen
resized = cv2.resize(img, (int(img.shape[1] / 3), int(img.shape[0] / 3)))

# Display the processed image with detected faces
cv2.imshow("Gray", resized)
cv2.waitKey(0)  # Wait indefinitely until a key is pressed
cv2.destroyAllWindows()  # Close all OpenCV windows