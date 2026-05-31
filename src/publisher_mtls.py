import json
import ssl
import time
import paho.mqtt.client as mqtt

from sensor_data import (
    generate_pool_data,
    generate_kitchen_data,
    generate_spa_data
)

from config import *

client = mqtt.Client(
  client_id="sensor_publisher",
  protocol=mqtt.MQTTv311
)

client.tls_set(
  ca_certs=CA_CERT,
  certfile=CLIENT_CERT,
  keyfile=CLIENT_KEY,
  tls_version=ssl.PROTOCOL_TLS_CLIENT
)

client.connect(BROKER_HOST, BROKER_PORT)

while True:

  pool = generate_pool_data()
  kitchen = generate_kitchen_data()
  spa = generate_spa_data()

  client.publish(
    "hydroficient/grandmarina/pool",
    json.dump(pool)
  )

  client.publish(
    "hydroficient/grandmarina/kitchen",
    json.dump(kitchen)
  )

  client.publish(
    "hydroficient/grandmarina/spa",
    json.dump(spa)
  )

  print("Published sensor readings")

  time.sleep(5)
