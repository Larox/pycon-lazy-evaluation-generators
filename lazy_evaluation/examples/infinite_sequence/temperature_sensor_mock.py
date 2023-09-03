import random
import time


def simulate_temperature_sensor():
    while True:
        temperature = random.uniform(0, 100)
        yield temperature
