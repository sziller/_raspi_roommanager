from SenseHatLedClock import Class_SenseHatLedClock as SHLC
from SenseHatSensors import Class_SenseHatSensors as SHSe
from SenseHatLedDisplay import Class_SenseHatLedDisplay as SHLD
import logging

from RoomManager import DataBaseAlchemy as DBAl

class RoomManagerEngine:
    """=== Class name: RoomManagerEngine ===============================================================================
    An object to be instantiated for physical status controll of a Room.
    By Room we refer to any built or naturarly originated closed area, space.
    ============================================================================================== by Sziller ==="""
    def __init__(self,
                 finite_looping: int,
                 schedule: list,
                 time_shift: dict or bool = False,
                 low_light: bool = True,
                 rotation: int = 0,
                 session_in: object or None = None,
                 **kwargs):
        self.finite_looping: int            = finite_looping  # 1- any int: actual int;
        self.low_light: bool                = low_light
        self.rotation: int                  = rotation
        self.session = session_in
        self.session = db_session_server = DBAl.createSession(db_path="./.room_01.db")
        if not time_shift:
            self.time_shift = {'delta_t_h': -1, 'delta_t_m': 0}
        else:
            self.time_shift = time_shift
        self.schedule = schedule

        self.initiate()
        
        
    def initiate(self):
        if not self.finite_looping:
            current_loop_count = 0
        else:
            current_loop_count = 1
        while current_loop_count <= self.finite_looping:
            print(self.finite_looping)
            for module in self.schedule:
                print(module)
                module['kwargs'].update(self.time_shift)
                getattr(self, module['function'])(**module['kwargs'])
            if self.finite_looping: current_loop_count += 1


    def run_led_display(self, **kwargs):
        print(" - LedDisplay                    === start ===")
        disp = SHLD.LedDisplay(**kwargs)
        disp.sense.low_light = self.low_light
        disp.sense.set_rotation(self.rotation)
        disp.run()
        print(" - LedDisplay                    === ended ===")


    def run_led_clock(self, **kwargs):
        print(" - LedClock                      === start ===")
        clock = SHLC.LedClock(**kwargs)
        clock.sense.low_light = self.low_light
        clock.sense.set_rotation(self.rotation)
        clock.run()
        print(" - LedClock                      === ended ===")


    def run_display_environmental_readings(self, **kwargs):
        print(" - DisplayEnvironmentalReadings  === start ===")
        env_disp = SHSe.EnvironmentalReadings(**kwargs)
        env_disp.sense.low_light = self.low_light
        env_disp.sense.set_rotation(self.rotation)
        env_disp.show_actual_data()
        print(" - DisplayEnvironmentalReadings  === ended ===")
    
    
    def run_write_environmental_readings(self, **kwargs):
        print(" - WriteEnvironmentalReadings    === start ===")
        env_toDB = SHSe.EnvironmentalReadings(**kwargs)
        read_out = env_toDB.return_data()
        print(read_out)
        DBAl.ADD_rows_to_table(primary_key="measurement_hash", data_list=[{"measurement_hash": "aa11",
                                                                           "measurement_locat": "TEST",
                                                                           "measurement_value": 100,
                                                                           "measurement_type": "test",
                                                                           "measurement_dim": "celcius",
                                                                           "timestamp": 100.11}], db_table="measurements",
                               session_in=self.session)
        print(" - WriteEnvironmentalReadings    === ended ===")
        return read_out
