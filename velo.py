import cv2 as cv
import numpy as np
cap = cv.VideoCapture('rstp://172.16.254.74:8080/h264_pcm.sdp')
while True:

    #print('About to start the Read command')
    ret, frame = cap.read()
    #print('About to show frame of Video.')
    cv.imshow("Capturing",frame)
    #print('Running..')

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
