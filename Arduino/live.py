import cv2
import requests
import numpy as np
from io import BytesIO
import time

# Replace with the URL of your ESP32-CAM's MJPEG stream
url = "http://192.168.6.135"

# Initialize variables for FPS calculation
start_time = time.time()
frame_count = 0

while True:
    # Open a connection to the ESP32-CAM's MJPEG stream
    print("Connecting to the stream...")
    response = requests.get(url, stream=True)
    print("Connected to the stream.")

    if response.status_code == 200:
        print("Got a response from the stream.")
        bytes = bytes()
        for chunk in response.iter_content(chunk_size=1024):
            bytes += chunk
            a = bytes.find(b'\xff\xd8')
            b = bytes.find(b'\xff\xd9')
            if a != -1 and b != -1:
                jpg = bytes[a:b+2]
                bytes = bytes[b+2:]
                frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)

                # Calculate and print FPS
                frame_count += 1
                elapsed_time = time.time() - start_time
                if elapsed_time >= 1.0:  # Update FPS every 1 second
                    fps = frame_count / elapsed_time
                    print(f"FPS: {fps:.2f}")
                    frame_count = 0
                    start_time = time.time()

                # Display the frame
                cv2.imshow("ESP32-CAM Live Stream", frame)

                # Press 'q' to exit the stream
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    else:
        print("Failed to connect to the stream. Check the URL.")

# Release resources
cv2.destroyAllWindows()
