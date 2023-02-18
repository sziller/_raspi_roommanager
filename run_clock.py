from SenseHatLedClock import Class_SenseHatLedClock as SHLC


def run(**kwargs):
    print(" - LedClock                  === start ===")
    clock = SHLC.LedClock()
    clock.sense.low_light = True
    clock.sense.set_rotation(0)
    clock.clock_style = 0
    clock.run(**kwargs)
    print(" - LedClock                  === ended ===")


if __name__ == "__main__":
    run()
