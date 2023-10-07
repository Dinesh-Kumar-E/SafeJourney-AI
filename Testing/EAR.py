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

image_path = r"D:\Dinesh-Kumar\Pictures\Camera Roll\WIN_20231007_16_23_12_Pro.jpg"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

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

    print(f'Eye Aspect Ratio (EAR): {ear}')

for face in faces:
    for i in range(36, 48):  
        x, y = shape.part(i).x, shape.part(i).y
        cv2.circle(image, (x, y), 2, (0, 0, 255), -1)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()