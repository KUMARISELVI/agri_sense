import requests
import json
import time
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# ESP8266 Web Server URL
url = "http://192.168.173.203/sensorData"  # Replace with your ESP8266 IP address

def get_sensor_data():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "humidity": data['humidity'],
                "temperature": data['temperature'],
                "temperatureF": data['temperatureF'],
                "moisture": data['moisture']
            }
        else:
            print("Failed to get sensor data. Status code:", response.status_code)
            return None
    except Exception as e:
        print("Exception:", e)
        return None

@app.route('/')
def index():
    return render_template('index11.html')

@app.route('/get_sensor_data')
def sensor_data():
    data = get_sensor_data()
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Failed to retrieve sensor data"})

if __name__ == "__main__":
    app.run(debug=True)
