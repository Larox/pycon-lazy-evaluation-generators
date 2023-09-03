from temperature_sensor_mock import simulate_temperature_sensor


def sensor_data():
    return [temp for temp in simulate_temperature_sensor()]


def temperature_calculations():
    temp_data = sensor_data()
    # some calculations with temp_data list


try:
    temperature_calculations()
except MemoryError as e:
    print(f"Memory limit exceeded: {e}")
else:
    print("Memory allocation successful.")
