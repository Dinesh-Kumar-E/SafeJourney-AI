import cv2
import dlib
import numpy as np
import time  # Import the time module

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"D:\Dinesh-Kumar\Downloads\shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)

def mouth_aspect_ratio(mouth):
    mouth = np.array(mouth, dtype=np.float32)
    horizontal_1 = np.linalg.norm(mouth[0] - mouth[6])
    horizontal_2 = np.linalg.norm(mouth[3] - mouth[9])
    vertical = np.linalg.norm(mouth[2] - mouth[10])
    mar = (horizontal_1 + horizontal_2) / (2.0 * vertical)
    return mar

# Initialize variables for FPS calculation
start_time = time.time()
frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)

    for face in faces:
        shape = predictor(gray, face)

        mouth_landmarks = []
        for i in range(48, 68):
            mouth_landmarks.append((shape.part(i).x, shape.part(i).y))

        mar = mouth_aspect_ratio(mouth_landmarks)

        # Draw facial landmarks for the mouth (optional)
        for (x, y) in mouth_landmarks:
            cv2.circle(frame, (x, y), 2, (0, 0, 255), -1)

        # Calculate and display FPS
        frame_count += 1
        elapsed_time = time.time() - start_time
        fps = frame_count / elapsed_time
        cv2.putText(frame, f'FPS: {fps:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame, f'Mouth Aspect Ratio (MAR): {mar:.2f}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Live Facial Landmarks", frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
