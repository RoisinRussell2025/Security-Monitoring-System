#/bin/bash
#Author:Roisin Russell
# Program Description: Import flask to recieve data

from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    print("Received data:", data)
    return {"status": "ok"}

app.run(host='0.0.0.0', port=5000)
