import cv2
import dlib
import numpy as np

# Load the face detector and shape predictor from dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"D:\Dinesh-Kumar\Downloads\shape_predictor_68_face_landmarks.dat")  # Replace with your path

# Function to calculate MAR for the mouth
def mouth_aspect_ratio(mouth):
    mouth = np.array(mouth, dtype=np.float32)
    # Calculate the distances between the landmarks for the mouth
    horizontal_1 = np.linalg.norm(mouth[0] - mouth[6])
    horizontal_2 = np.linalg.norm(mouth[3] - mouth[9])
    vertical = np.linalg.norm(mouth[2] - mouth[10])
    mar = (horizontal_1 + horizontal_2) / (2.0 * vertical)
    return mar

# Load the image
image_path = r"D:\Dinesh-Kumar\Pictures\Camera Roll\WIN_20231007_16_23_12_Pro.jpg"  # Replace with your image path
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = detector(gray)

# Loop over the detected faces
for face in faces:
    shape = predictor(gray, face)

    # Extract the coordinates of the mouth landmarks
    mouth_landmarks = []
    for i in range(48, 68):  # Mouth landmarks
        x, y = shape.part(i).x, shape.part(i).y
        mouth_landmarks.append((x, y))

    # Calculate the MAR for the mouth
    mar = mouth_aspect_ratio(mouth_landmarks)

    # Print the MAR
    print(f'Mouth Aspect Ratio (MAR): {mar}')

    # Draw facial landmarks for the mouth
    for (x, y) in mouth_landmarks:
        cv2.circle(image, (x, y), 2, (0, 0, 255), -1)

# Display the image with facial landmarks (optional)
cv2.imshow("Image with Facial Landmarks", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
