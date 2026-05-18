#bin/bash
#Author: Roisin Russell
#Program Description: Capture and save data

from picamera2 import Picamera2
import time
import json
import requests
from datetime import datetime

# Start camera
picam2 = Picamera2()
picam2.start()

while True:
    # Capture image
    image_path = "static/last_capture.jpg"
    picam2.capture_file(image_path)

    # Create event data
    data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "event": "image_captured"
    }

    # Save JSON data
    with open("data/data.json", "w") as f:
        json.dump(data, f)

    # Send data via HTTP
    try:
        requests.post("http://127.0.0.1:5000/data", json=data)
        print("Data sent successfully")
    except:
        print("Failed to send data")

    # Print output
    print(f"Captured image at {data['timestamp']}")

    # Wait 10 seconds
    time.sleep(10)
