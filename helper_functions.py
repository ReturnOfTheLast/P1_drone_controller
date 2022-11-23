from djitellopy import Tello
from time import sleep

def init_tello() -> Tello:
    tello = Tello()
    tello.connect()
    return tello

def fly_and_rotate(tello: Tello, distance: int) -> None:
    tello.move_forward(distance)
    sleep(1)
    tello.rotate_clockwise(90)
    sleep(1)

def get_flight_info(tello: Tello) -> dict:
    return {
        "time": tello.get_flight_time(),
        "battery": tello.get_battery(),
    }
