import cv2
import numpy as np

cap = cv2.VideoCapture(0)

frame = None
hsv = None


def get_hsv(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:

        h, s, v = hsv[y, x]

        print("Clicked at:", x, y)
        print("HSV:", h, s, v)
        print("----------------")


cv2.namedWindow("HSV Sampler")
cv2.setMouseCallback("HSV Sampler", get_hsv)


while True:

    ret, frame = cap.read()

    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow("HSV Sampler", frame)

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()