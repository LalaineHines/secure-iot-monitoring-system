import random
from datetime import datetime


def generate_pool_data():
  return {
    "device": "pool_sensor",
    "temperature": round(random.uniform(70, 85), 2),
    "ph": round(random.uniform(7.0, 7.8), 2),
    "timestamp": datetime.now().isoformat()
  }


def generate_kitchen_data():
  return {
    "device": "kitchen_sensor",
    "temperature": round(random.uniform(35, 50), 2),
    "humidity": round(random.uniform(40, 75), 2),
    "timestamp": datetime.now().isoformat()
  }


def generate_spa_data():
  return {
    "device": "spa_sensor",
    "temperature": round(random.uniform(95, 105), 2),
    "chlorine": round(random.uniform(1, 4), 2),
    "timestamp": datetime.now().isoformat()
  }
