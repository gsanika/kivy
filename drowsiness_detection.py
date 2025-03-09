import cv2
import dlib
import numpy as np
from scipy.spatial import distance as dist

# Define eye aspect ratio function
def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

# Load face detector and predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("assets/shape_predictor_68_face_landmarks.dat")

# Eye landmarks
LEFT_EYE = list(range(42, 48))
RIGHT_EYE = list(range(36, 42))
EYE_AR_THRESH = 0.25
EYE_AR_CONSEC_FRAMES = 30
frame_counter = 0

def detect_drowsiness(gray, frame):
    """
    Detects drowsiness and eye closure.
    """
    global frame_counter
    faces = detector(gray)

    for face in faces:
        shape = predictor(gray, face)
        shape = np.array([[p.x, p.y] for p in shape.parts()])

        leftEye = shape[LEFT_EYE]
        rightEye = shape[RIGHT_EYE]

        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        avgEAR = (leftEAR + rightEAR) / 2.0

        if avgEAR < EYE_AR_THRESH:
            frame_counter += 1
            if frame_counter >= EYE_AR_CONSEC_FRAMES:
                cv2.putText(frame, "DROWSINESS DETECTED!", (30, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
        else:
            frame_counter = 0
