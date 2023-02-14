from SenseHatSensors import Class_SenseHatSensors as SHSe


def run(**kwargs):
    print(" - EnvironmentalReadings     === start ===")
    env = SHSe.EnvironmentalReadings()
    env.sense.low_light = True
    env.show_actual_data(**kwargs)
    print(" - EnvironmentalReadings     === ended ===")


if __name__ == "__main__":
    run()
