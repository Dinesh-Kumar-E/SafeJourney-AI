import cv2
import dlib
import numpy as np

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"D:\Dinesh-Kumar\Downloads\shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)  

def eye_aspect_ratio(eye):
    eye = np.array(eye, dtype=np.float32)
    vertical_1 = np.linalg.norm(eye[1] - eye[5])
    vertical_2 = np.linalg.norm(eye[2] - eye[4])
    horizontal = np.linalg.norm(eye[0] - eye[3])
    ear = (vertical_1 + vertical_2) / (2.0 * horizontal)
    return ear

def mouth_aspect_ratio(mouth):
    mouth = np.array(mouth, dtype=np.float32)
    horizontal_1 = np.linalg.norm(mouth[0] - mouth[6])
    horizontal_2 = np.linalg.norm(mouth[3] - mouth[9])
    vertical = np.linalg.norm(mouth[2] - mouth[10])
    mar = (horizontal_1 + horizontal_2) / (2.0 * vertical)
    return mar

def EAR_MAR():
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = detector(gray)

        for face in faces:
            shape = predictor(gray, face)

            left_eye_landmarks = []
            right_eye_landmarks = []
            mouth_landmarks = []

            # Extract landmarks for the left and right eyes
            for i in range(36, 42):  # Left eye landmarks
                left_eye_landmarks.append((shape.part(i).x, shape.part(i).y))
            for i in range(42, 48):  # Right eye landmarks
                right_eye_landmarks.append((shape.part(i).x, shape.part(i).y))

            # Extract landmarks for the mouth
            for i in range(48, 68):  
                mouth_landmarks.append((shape.part(i).x, shape.part(i).y))

            left_ear = eye_aspect_ratio(left_eye_landmarks)
            right_ear = eye_aspect_ratio(right_eye_landmarks)
            mar = mouth_aspect_ratio(mouth_landmarks)

            # Draw facial landmarks for the eyes and mouth (optional)
            # for (x, y) in left_eye_landmarks + right_eye_landmarks + mouth_landmarks:
            #     cv2.circle(frame, (x, y), 2, (0, 0, 255), -1)

            # cv2.putText(frame, f'Left Eye EAR: {left_ear:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            # cv2.putText(frame, f'Right Eye EAR: {right_ear:.2f}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            # cv2.putText(frame, f'Mouth Aspect Ratio (MAR): {mar:.2f}', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # cv2.imshow("Live Facial Landmarks", frame)

        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
            avg = (left_ear+right_ear)/2.0
            return (avg, mar, frame)