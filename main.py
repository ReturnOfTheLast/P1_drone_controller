from djitellopy import Tello
from time import sleep

tello = Tello()
tello.connect()


#configure drone
tello.enable_mission_pads()
#tello.set_mission_pad_detection_direction(0)


tello.takeoff()

#distance = tello.query_distance_tof()
#print("The distance is:", distance, "cm")

pad = tello.get_mission_pad_id()  # -1 means mission pad not detected 
time = tello.get_flight_time()
battery = tello.get_battery()
print("battery lvl", battery, "%")

distance = 130
num_of_sides = 4*3

for _ in range(num_of_sides):
    time = tello.get_flight_time()

    print("Flight time is:", time)
    sleep(1)
    tello.move_forward(distance)
    sleep(1)
    tello.rotate_clockwise(90)
        
tello.land()