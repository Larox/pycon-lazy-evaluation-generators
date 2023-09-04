from temperature_sensor_mock import simulate_temperature_sensor


def sensor_data() -> list[int]:
    return [temp for temp in simulate_temperature_sensor()]


def temperature_calculations():
    temp_data = sensor_data()
    data = []
    for temp in temp_data:
        data.append(temp)
        print(temp)


try:
    temperature_calculations()
except MemoryError as e:
    print(f"Memory limit exceeded: {e}")
else:
    print("Memory allocation successful.")
