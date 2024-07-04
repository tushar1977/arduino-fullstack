import serial
import json
from time import time
from flask import render_template, make_response, Flask, jsonify,request
from flask_htmx import HTMX

print("hello")

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"

sensor_data=  []

htmx = HTMX()
htmx.init_app(app)

latest = None

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/sensor", methods=["POST", "GET"])
def get_sensor_value():
    global latest
    
    if request.method == "POST":
        try:
            data = request.get_json()
            if data is None:
                return jsonify({"error": "No JSON data received"}), 400
            sensor_value = data.get('sensor_value')
            if sensor_value is None:
                return jsonify({"error": "No sensor value received"}), 400
            print(f'Received sensor value: {sensor_value}')
            latest = sensor_value
            return jsonify({"sensor_value": sensor_value}), 200
        except Exception as e:
            print(f"Error processing request: {e}")
            return jsonify({"error": str(e)}), 500
    
    if request.method == "GET":
        return jsonify({"sensor_value": latest})
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=70)

