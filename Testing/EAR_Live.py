import cv2
import dlib
import numpy as np
import time

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"D:\Dinesh-Kumar\Downloads\shape_predictor_68_face_landmarks.dat")

def eye_aspect_ratio(eye):
    eye = np.array(eye, dtype=np.float32)
    vertical_1 = np.linalg.norm(eye[1] - eye[5])
    vertical_2 = np.linalg.norm(eye[2] - eye[4])
    horizontal = np.linalg.norm(eye[0] - eye[3])
    ear = (vertical_1 + vertical_2) / (2.0 * horizontal)
    return ear

cap = cv2.VideoCapture(0)

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

        left_eye = []
        right_eye = []

        for i in range(36, 42):  
            left_eye.append((shape.part(i).x, shape.part(i).y))
        for i in range(42, 48):  
            right_eye.append((shape.part(i).x, shape.part(i).y))

        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)

        ear = (left_ear + right_ear) / 2.0

        cv2.putText(frame, f'EAR: {ear:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Calculate and display FPS
    frame_count += 1
    elapsed_time = time.time() - start_time
    fps = frame_count / elapsed_time
    cv2.putText(frame, f'FPS: {fps:.2f}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Live Facial Landmarks", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
