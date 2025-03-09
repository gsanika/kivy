import cv2
import pygame
from eye_tracking import get_pupil_position
from drowsiness_detection import detect_drowsiness

# Initialize sound for alerts
pygame.mixer.init()
pygame.mixer.music.load("assets/alarm.mp3")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect drowsiness
    detect_drowsiness(gray, frame)

    # Show frame
    cv2.imshow("Drowsiness & Pupil Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
