from flask import Flask, jsonify
import multiprocessing

import drone_controller as dc

tello = dc.init_tello()

bg_process = None

app = Flask(__name__)

@app.get("/api/fly/<int:length>/<int:height>/<int:rounds>")
def fly(length: int, height: int, rounds: int):
    global bg_process
    state = dc.get_flight_info(tello)
    
    if state["time"] > 0:
        return jsonify({"status": 1, "message": "Drone is already flying"})

    tello.takeoff()
    bg_process = multiprocessing.process(
        target=dc.fly_and_rotate,
        args=[tello, [length, height], rounds]
    )
    bg_process.start()
    return jsonify({"status": 0, "message": "Drone flying initiated"})

@app.get("/api/land")
def land():
    global bg_process
    try:
        if bg_process != None:
            bg_process.terminate()
            bg_process = None
    except: pass
    
    tello.land()
    return jsonify({"status": 0, "message": "Drone landed"})

@app.get("/api/sos")
def emergency():
    global bg_process
    try:
        if bg_process != None:
            bg_process.terminate()
            bg_process = None
    except: pass
    
    tello.emergency()
    tello.end()
    exit(1)

if __name__ == "__main__":
    app.run("0.0.0.0", 8100)
