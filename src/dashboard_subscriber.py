import ssl
import json
import os
import time
import logging
from datetime import datetime, timedelta

import paho.mqtt.client as mqtt

from config import (
   BROKER_HOST,
   BROKER_PORT,
   CA_CERT,
   CLIENT_CERT,
   CLIENT_KEY,
)

# ==========================
# LOGGING CONFIGURATION
# ==========================

os.makedirs("../logs", exist_ok=True)

logging.basicConfig(
   filename="../log/iot_monitor.log",
   level=logging.INFO,
   format="%(asctime)s | %(levelname)s | %(message)s"
)

# ==========================
# DASHBOARD STATE
# ==========================

latest_readings = {}

last_seen = {}

OFFLINE_THRESHOLD_SECONDS = 30

SENSORS = [
   "pool_sensor",
   "kitchen_sensor",
   "spa_sensor"
]

# ==========================
# ALERTING
# ==========================

def generate_alerts(device, data):
   alerts = []

   if device == "pool_sensor":
      temp = data.get("temperature")
      ph = data.get("ph")

      if temp and temp > 90:
         alerts.append(
           f"POOL ALERT: Temperature high ({temp}°F)" 
         )

      if ph and (ph < 7.0 or ph > 8.0):
         alerts.append(
            f"POOL ALERT: pH outside safe range ({ph})"
         )
   elif device == "kitchen_sensor":
      temp = data.get("temperature")
      humidity = data.get("humidity")

      if temp and temp > 50:
         alerts.append(
            f"KITCHEN ALERT: Temperature too high ({temp}°F)"
         )

      if humidity and humidity > 80:
         alerts.append(
            f"KITCHEN ALERT: Humidity too high ({humidity}%)"
         )

   elif device == "spa_sensor":
        temp = data.get("temperature")
        chlorine = data.get("chlorine")

        if temp and temp > 104:
            alerts.append(
                f"SPA ALERT: Overheating ({temp}°F)"
            )

        if chlorine and chlorine < 1:
            alerts.append(
                f"SPA ALERT: Chlorine too low ({chlorine})"
            )

   for alert in alerts:
        logging.warning(alert)

   return alerts

# ==========================
# DASHBOARD DISPLAY
# ==========================

def clear_screen():
   os.system("cls" if os.name == "nt" else "clear")

def sensor_status(sensor_name):
   if sensor_name not in last_seen:
      return "OFFLINE"
   
   elapsed = datetime.now() - last_seen[sensor_name]

   if elapsed > timedelta(seconds=OFFLINE_THRESHOLD_SECONDS):
      return "OFFLINE"
   
   return "ONLINE"

def draw_dashboard():
   
   clear_screen()

   print("=" * 60)
   print("     GRAND MARINA IoT SECURITY MONITORING DASHBOARD")
   print("=" * 60)
   print(f"Last Refresh: {datetime.now()}")
   print()

   for sensor in SENSORS:

        print("-" * 60)

        status = sensor_status(sensor)

        print(f"Sensor: {sensor}")
        print(f"Status: {status}")

        if sensor in latest_readings:

            data = latest_readings[sensor]

            for key, value in data.items():

                if key == "device":
                    continue

                print(f"{key}: {value}")

            print()

            alerts = generate_alerts(sensor, data)

            if alerts:
                print("ALERTS:")

                for alert in alerts:
                    print(f"  {alert}")

            else:
                print("Alerts: None")

        else:
            print("No data received")

        print()

   print("=" * 60)

# ==========================
# MQTT CALLBACKS
# ==========================

def on_connect(client, userdata, flags, rc):

    if rc == 0:

        print("Connected successfully.")

        logging.info(
            "Dashboard connected to MQTT broker."
        )

        client.subscribe(
            "hydroficient/grandmarina/#"
        )

        logging.info(
            "Subscribed to hydroficient/grandmarina/#"
        )

    else:

        logging.error(
            f"Broker connection failed. Return code={rc}"
        )

        print(
            f"Connection failed. Return code={rc}"
        )


def on_message(client, userdata, msg):

    try:

        payload = json.loads(
            msg.payload.decode()
        )

        device = payload.get("device")

        if not device:
            logging.warning(
                "Message received without device field."
            )
            return

        latest_readings[device] = payload

        last_seen[device] = datetime.now()

        logging.info(
            f"Received data from {device}"
        )

        draw_dashboard()

    except Exception as error:

        logging.error(
            f"Message processing error: {error}"
        )

# ==========================
# SENSOR HEALTH CHECK
# ==========================

def check_offline_sensors():

    for sensor in SENSORS:

        if sensor not in last_seen:
            continue

        elapsed = (
            datetime.now()
            - last_seen[sensor]
        )

        if elapsed.total_seconds() > OFFLINE_THRESHOLD_SECONDS:

            logging.warning(
                f"{sensor} offline for "
                f"{int(elapsed.total_seconds())} seconds"
            )

# ==========================
# MQTT CLIENT SETUP
# ==========================

client = mqtt.Client(
  client_id="dashboard_subscriber",
  protocol=mqtt.MQTTv311
)

client.tls_set(
  ca_certs=CA_CERT,
  certfile=CLIENT_KEY,
  keyfile=CLIENT_KEY,
  tls_version=ssl.PROTOCOL_TLS_CLIENT
)

client.on_connect = on_connect
client.on_message = on_message

# ==========================
# MAIN PROGRAM
# ==========================

try:

    client.connect(
        BROKER_HOST,
        BROKER_PORT
    )

    client.loop_start()

    while True:

        check_offline_sensors()

        draw_dashboard()

        time.sleep(5)

except KeyboardInterrupt:

    print("\nShutting down dashboard...")

    logging.info(
        "Dashboard shutdown initiated."
    )

    client.loop_stop()
    client.disconnect()

except Exception as error:

    logging.critical(
        f"Fatal dashboard error: {error}"
    )

    raise