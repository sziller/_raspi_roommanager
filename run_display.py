from SenseHatLedDisplay import Class_SenseHatLedDisplay as SHLD


def run(**kwargs):
    print(" - LedDisplay                === start ===")
    disp = SHLD.LedDisplay()
    disp.sense.low_light = True
    disp.run(**kwargs)
    print(" - LedDisplay                === ended ===")


if __name__ == "__main__":
    run()
