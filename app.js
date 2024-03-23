// Define the URL of your Flask API endpoint
const url = 'https://cardetection.pythonanywhere.com/upload'; // Replace with your actual URL

// Function to detect cars in the image
async function detectCars(imageFile) {
    try {
        // Create a FormData object to send the image file
        const formData = new FormData();
        formData.append('image', imageFile);

        // Send a POST request to the Flask API endpoint
        const response = await fetch(url, {
            method: 'POST',
            body: formData
        });

        // Parse the JSON response
        const data = await response.json();

        // Update the car count
        const carCountElement = document.getElementById('carCount');
        carCountElement.textContent = data.car_count;

        // Display the image with bounding boxes
        const imgElement = document.getElementById('image');
        imgElement.src = 'data:image/jpeg;base64,' + data.image; // Assuming the response contains the image bytes as base64-encoded string
        imgElement.style.display = 'block'; // Show the image element
    } catch (error) {
        console.error('Error:', error);
    }
}

// Event listener for form submission
document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission behavior

    // Get the selected image file
    const imageFile = document.getElementById('imageInput').files[0];

    // Call the detectCars function with the image file
    detectCars(imageFile);
});
