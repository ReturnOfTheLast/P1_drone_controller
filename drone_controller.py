from djitellopy import Tello
from time import sleep

def init_tello() -> Tello:
    tello = Tello()
    tello.connect()
    return tello

def fly_and_rotate(tello: Tello, distances: list[int], rounds: int) -> None:
    for i in range(4*rounds):
        tello.move_forward(distances[i%2])
        sleep(1)
        tello.rotate_clockwise(90)
        sleep(1)
    tello.land()

def get_flight_info(tello: Tello) -> dict:
    return {
        "time": tello.get_flight_time(),
        "battery": tello.get_battery(),
    }
