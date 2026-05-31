# System Architecture

Three sensors publish environmental readings:

- Pool Sensor
- Kitchen Sensor
- Spa Sensor

All sensor traffic is encrypted using TLS.

Data Flow:

Pool Sensor
Kitchen Sensor
Spa Sensor
      ↓
Mosquitto Broker
      ↓
Dashboard Subscriber
