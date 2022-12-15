import drone_controller as dc

tello = dc.init_tello()

length = 100
height = 100
rounds = 3

tello.takeoff()

dc.fly_and_rotate(tello, [length, height], rounds)
