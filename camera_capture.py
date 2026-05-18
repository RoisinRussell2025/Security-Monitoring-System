

print("Project started")
print("Camera tested successfully")

from picamera2 import Picamera2
import time
import json
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

    # Print output 
    print(f"Captured image at {data['timestamp']}")

    # Wait 10 seconds
    time.sleep(10)
