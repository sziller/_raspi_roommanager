from SenseHatLedClock import Class_SenseHatLedClock as SHLC
from SenseHatSensors import Class_SenseHatSensors as SHSe
from SenseHatLedDisplay import Class_SenseHatLedDisplay as SHLD


class RoomManager:
    def __init__(self,
                 finite_looping: int,
                 time_shift: dict = False,
                 schedule: list = False,
                 low_light: bool = True,
                 rotation: int = 0):
        self.finite_looping: int            = finite_looping  # 1- any int: actual int;
        self.low_light: bool                = low_light
        self.rotaton: int                   = rotation
        if not time_shift:
            self.time_shift = {'delta_t_h': -1, 'delta_t_m': 0}
        else:
            self.time_shift = time_shift
        if not schedule:
            self.schedule = [
                {'function': self.run_led_clock(),              'kwargs': {'duration': 30, 'heartbeat': 1}},
                {'function': self.run_led_display(),            'kwargs': {'duration': 4,
                                                                           'dyn': True,
                                                                           'alias': 0,
                                                                           'delay': 0.1}},
                {'function': self.run_environmental_readings(), 'kwargs': {'code': 7, 'scroll_speed': 0.1}}
                    ]
        else:
            self.schedule = schedule
        

    def initiate(self):
        if not self.finite_looping:
            current_loop_count = 0
        else:
            current_loop_count = 1
        while current_loop_count <= self.finite_looping:
            for module in self.schedule:
                module['kwargs'].update(self.time_shift)
                module['function'](**module['kwargs'])
            if self.finite_looping: current_loop_count += 1


    def run_led_display(self, **kwargs):
        print(" - LedDisplay                === start ===")
        disp = SHLD.LedDisplay()
        disp.sense.low_light = self.low_light
        disp.sense.set_rotation(self.rotaton)
        disp.run(**kwargs)
        print(" - LedDisplay                === ended ===")


    def run_led_clock(self, **kwargs):
        print(" - LedClock                  === start ===")
        clock = SHLC.LedClock()
        clock.sense.low_light = self.low_light
        clock.sense.set_rotation(self.rotaton)
        clock.clock_style = 0
        clock.run(**kwargs)
        print(" - LedClock                  === ended ===")


    def run_environmental_readings(self, **kwargs):
        print(" - EnvironmentalReadings     === start ===")
        env = SHSe.EnvironmentalReadings()
        env.sense.low_light = self.low_light
        env.sense.set_rotation(self.rotaton)
        env.show_actual_data(**kwargs)
        print(" - EnvironmentalReadings     === ended ===")
