import cv2
import numpy as np

def get_pupil_position(eye_region):
    """
    Detects the pupil position in the eye region.
    """
    gray_eye = cv2.cvtColor(eye_region, cv2.COLOR_BGR2GRAY)
    _, thresh_eye = cv2.threshold(gray_eye, 30, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresh_eye, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])  # X-coordinate of the pupil
            cy = int(M["m01"] / M["m00"])  # Y-coordinate of the pupil
            return cx, cy
    return None
