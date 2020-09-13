import cv2
import numpy as np
import os

def run():
    vcap = cv2.VideoCapture("rtsp://192.168.1.50:5554/camera", cv2.CAP_FFMPEG)
    while(1):
        ret, frame = vcap.read()
        if ret == False:
            print("Frame is empty")
            break;
        else:
            cv2.imshow('VIDEO', frame)
            cv2.waitKey(1)

if __name__ == '__main__':
    print(os.getenv("OPENCV_FFMPEG_CAPTURE_OPTIONS"))
    os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
    print(os.getenv("OPENCV_FFMPEG_CAPTURE_OPTIONS"))
    run()