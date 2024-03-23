from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

# Define the paths to the Haar cascade XML file and the image file
haar_cascade = 'haarcascade_car.xml'


@app.route('/upload', methods=['POST'])
def detect_cars():
    # Check if an image file is present in the request
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
    
    # Load the Haar cascade for car detection
    car_cascade = cv2.CascadeClassifier(haar_cascade)

    # Read the image file from the request
    image = cv2.imdecode(
        np.fromstring(request.files['image'].read(), np.uint8),
        cv2.IMREAD_UNCHANGED
    )
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect cars in the image
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    # Draw bounding boxes around detected cars
    for (x, y, w, h) in cars:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Get the count of detected cars
    car_count = len(cars)

    # Convert the image to bytes
    _, img_encoded = cv2.imencode('.jpg', image)
    img_bytes = img_encoded.tobytes()

    # Create response JSON
    response = {
        'car_count': car_count
    }

    return jsonify(response), 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True)
