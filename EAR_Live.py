import cv2
import dlib
import numpy as np

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


def EAR():
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

            #cv2.putText(frame, f'EAR: {ear:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            #print(f'Eye Aspect Ratio (EAR): {ear}')
            #print(frame)
        return (ear,frame)

        #cv2.imshow("Live Facial Landmarks", frame)