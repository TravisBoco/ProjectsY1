import cv2
import time
import datetime

capture = cv2.VideoCapture(0)

while True:
    _, frame = capture.read()
    cv2.imshow("Camera", frame)

    if cv2.waitKey(3) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()