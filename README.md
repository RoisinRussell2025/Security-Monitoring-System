# Project Name: Smart Camera Monitor
## Student name: *Roisin Prendergast* Student ID: *02482126*

## Project Overview
This project is a Smart Camera Monitoring System developed using a Raspberry Pi, Python, and Flask. The system captures images automatically, sends structured data over HTTP, and displays the results on a web-based dashboard.

---

## Features
- Captures images using Raspberry Pi camera
- Generates structured JSON data
- Sends data using HTTP POST requests
- Flask server receives and processes data
- Web dashboard displays latest image and event
- Styled user interface with background image
- Automatic and manual refresh functionality

---

## Technologies Used
- Python
- Flask
- Raspberry Pi
- JSON
- HTTP
- 

## How It Works
1. The Raspberry Pi captures an image at timed intervals
2. A JSON object is created containing event data
3. The data is sent to a Flask server via HTTP POST
4. The server saves the data and updates the dashboard
5. The dashboard displays the latest image and event

---

## File Structure
 **smart-camera-monitor**
•	camera_capture.py 
•	server.py
•	data 	
      	data/json
•	static
      	last_capture.jpg
      	security.jpg (used for background image)
•	templates
        status.html

## Resources Used
notes from course
labs 9 & 10 
https://pypi.org/
google and co-pilot 
Note: As I have not yet completed the Web Development module, 
I used the resources referenced above to support the HTML and GitHub setup for this project.
