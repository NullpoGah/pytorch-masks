import numpy as np
import cv2


def run():
    capture = cv2.VideoCapture("rtsp://192.168.1.50:5554/camera", cv2.CAP_FFMPEG)
    while True:
        result, frame = capture.read()
        cv2.imshow('video', frame)

        if cv2.waitKey(16) == ord("q"):
            break