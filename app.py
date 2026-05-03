from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Initial values
data = {
    "soil_moisture": 40,
    "temperature": 28,
    "pump_status": "OFF"
}

@app.route('/data', methods=['GET'])
def get_data():
    # 🔥 Simulate realistic changing sensor data
    data["soil_moisture"] += random.randint(-3, 3)
    data["temperature"] += random.randint(-1, 1)

    # Clamp values (keep within realistic range)
    data["soil_moisture"] = max(10, min(90, data["soil_moisture"]))
    data["temperature"] = max(20, min(45, data["temperature"]))

    return jsonify(data)

@app.route('/pump', methods=['POST'])
def control_pump():
    status = request.json.get("status")

    if status in ["ON", "OFF"]:
        data["pump_status"] = status
        return jsonify({
            "message": f"Pump turned {status}",
            "current_status": data["pump_status"]
        })

    return jsonify({"error": "Invalid status"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)