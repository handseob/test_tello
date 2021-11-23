from djitellopy import Tello

tello = Tello()

tello.connect()

tello.takeoff()

# tello move
tello.move_up(200)
tello.move_forward(500)
tello.rotate_clockwise(360)
tello.move_back(500)

tello.land()

pass