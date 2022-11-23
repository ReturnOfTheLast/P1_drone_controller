from helper_functions import init_tello, fly_and_rotate, get_flight_info

# Setup the tello and takeoff
tello = init_tello()
tello.takeoff()

# Dummy, the settings will come from the main interface
dimensions = [130, 130]
num_of_sides = 4*3

for i in range(num_of_sides):
    flight_info = get_flight_info(tello)
    print(f"""
        Time: {flight_info['time']}
        Battery: {flight_info["battery"]}%
    """)

    fly_and_rotate(tello, dimensions[i%2])

tello.land()
