import ssl
import json
import paho.mqtt.client as mqtt

from config import *


def on_connect(client, userdata, flags, rc):
  print("Connected o broker")

  client.subscribe(
    "hydroficient/grandmarina/#"
  )

def on_message(client, userdata, msg):
  data = json.loads(
    msg.payload.decode()
  )

  print("\n========================")
  print(f"Topic: {msg.topic}")

  for key, value in data.items():
      print(f"{key}: {value}")

  print("========================")

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
clinet.on_message = on_message

client.connect(
  BROKER_HOST,
  BROKER_PORT
)

client.loop_forever()
