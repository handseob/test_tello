from djitellopy import Tello

tello = Tello()

tello.connect()

tello.streamon
frame_read = tello.get_frame_read()
# tello.takeoff()

import cv2
# tello video
while True:
    cv2.imshow('tello stream',frame_read.frame)
    key = cv2.waitKey()
    if key == ord('q'):
        break

tello.streamoff()

# tello.land()
pass