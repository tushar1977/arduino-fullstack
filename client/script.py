import serial
import requests
import time


ser = serial.Serial("/dev/ttyACM0", 9600)

url = "http://84.247.185.93:70/sensor"

while True:
    try:
        if ser.in_waiting > 0:
            sensor_value = ser.readline().decode("utf-8").strip()
            print(f"Sensor Value: {sensor_value}")

            headers = {"Content-Type": "application/json"}
            response = requests.post(
                url, json={"sensor_value": sensor_value}, headers=headers
            )
            print(f"Server Response: {response.status_code} - {response.text}")

        time.sleep(1)

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
