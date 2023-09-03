from temperature_sensor_mock import simulate_temperature_sensor


def sensor_data():
    yield next(simulate_temperature_sensor)


def temperature_calculations():
    temp_data = (temp for temp in simulate_temperature_sensor())
    for i in range(0, 10000):
        pass


temperature_calculations()
