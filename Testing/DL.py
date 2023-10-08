import cv2
import numpy as np
from tensorflow import keras
import time

# Load the trained model
model = keras.models.load_model(r"D:\Dinesh-Kumar\Downloads\model.h5")

# Define a dictionary to map class indices to class labels
class_labels = {0: "Closed", 1: "Open", 3: "no_yawn", 4: "yawn"}

# Initialize the camera capture
cap = cv2.VideoCapture(0)  # 0 for the default camera, you can change it if you have multiple cameras

# Set the window size
cv2.namedWindow("Real-time Blink Detection", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Real-time Blink Detection", 800, 600)  # Adjust the size as needed

# Define font parameters
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.5  # Adjust the font scale as needed
font_thickness = 1

# Initialize variables for FPS calculation
start_time = time.time()
frame_count = 0

while True:
    ret, frame = cap.read()  # Read a frame from the camera

    # Check if the frame was successfully read
    if not ret:
        print("Process breaked")
        break

    # Resize the frame to match the model's input shape
    frame = cv2.resize(frame, (150, 150))
    frame = frame / 255.0

    # Make a prediction using the model
    input_data = np.expand_dims(frame, axis=0)  # Add a batch dimension
    prediction = model.predict(input_data)
    predicted_class = int(np.round(prediction[0][0]))

    # Get the corresponding class label
    class_label = class_labels.get(predicted_class, "Unknown")

    # Calculate and display FPS
    frame_count += 1
    elapsed_time = time.time() - start_time
    fps = frame_count / elapsed_time
    cv2.putText(frame, f"FPS: {fps:.2f}", (5, 60), font, font_scale, (0, 0, 255), font_thickness)

    # Display the result on the frame with reduced font size
    cv2.putText(frame, f"Prediction: {class_label}", (5, 30), font, font_scale, (0, 255, 0), font_thickness)

    # Show the frame with the prediction
    cv2.imshow("Real-time Blink Detection", frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
