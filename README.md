IoT-Based Smart Agriculture Monitoring System

Overview

This project is a simple IoT-based agriculture monitoring system that tracks soil moisture and temperature in real time. It also allows remote control of a water pump and provides basic irrigation recommendations based on sensor values.

The system uses a Python Flask backend to simulate sensor data and expose REST APIs. An Android application built using Kotlin consumes these APIs to display live data and control the system.

Features

- Real-time monitoring of soil moisture and temperature
- Remote control of water pump (ON/OFF)
- Live data updates from backend
- Basic rule-based recommendation for irrigation
- Graphical representation of soil moisture data in Android app
- REST API communication between backend and mobile application

System Architecture

Sensor Data Simulation (Python Flask Backend)
→ REST APIs
→ Android Mobile Application
→ User Interface for monitoring and control

Technology Stack

Backend:
- Python
- Flask
- Flask-CORS

Mobile Application:
- Kotlin (Android)
- Android Studio
- MPAndroidChart

API Endpoints

GET /data
Returns current sensor values including soil moisture, temperature, and pump status.

POST /pump
Used to turn the pump ON or OFF.

GET /recommend
Returns irrigation recommendation based on sensor values.

Android Application

The Android app displays:
- Soil moisture level
- Temperature
- Pump status
- Live updating graph of soil moisture

It also allows manual control of the pump and automatically refreshes data at regular intervals.

Setup Process
Backend Setup:
1. Install Flask and dependencies
   pip install flask flask-cors
2. Run the backend server
   python app.py

Android Setup:
1. Open project in Android Studio
2. Run the application on emulator or physical device
3. Ensure correct backend IP is configured:
   - Emulator: http://10.0.2.2:5000
   - Physical device: http://your-pc-ip:5000

Future Improvements
- Integration with real IoT sensors
- Machine learning-based crop prediction
- Cloud database integration
- Web dashboard for monitoring
- Historical data analysis
