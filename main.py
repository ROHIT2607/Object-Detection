import cv2

# Define the paths to the Haar cascade XML file and the image file
haar_cascade = 'haarcascade_car.xml'
image_path = 'car.jpg'

# Load the Haar cascade for car detection
car_cascade = cv2.CascadeClassifier(haar_cascade)

# Read the input image
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect cars in the image
cars = car_cascade.detectMultiScale(gray, 1.1, 1)

# Draw bounding boxes around detected cars
for (x, y, w, h) in cars:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

# Display the image with detected cars
cv2.imshow('Car Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
