import os
import inspect
from dotenv import load_dotenv
from SenseHatLedClock import Class_SenseHatLedClock as SHLC
from SenseHatSensors import Class_SenseHatSensors as SHSe
from SenseHatLedDisplay import Class_SenseHatLedDisplay as SHLD
import logging

from shmc_sqlAccess import SQL_interface as SQLi
from shmc_sqlBases.sql_baseMeasurement import Measurement as sqlMeasurement

# LOGGING                                                                                   logging - START -
lg = logging.getLogger()
# LOGGING                                                                                   logging - ENDED -

load_dotenv()


class EngineRoomManager:
    """=== Class name: RoomManagerEngine ===============================================================================
    An object to be instantiated for physical status controll of a Room.
    By Room we refer to any built or naturarly originated closed area, space.
    ============================================================================================== by Sziller ==="""
    ccn = inspect.currentframe().f_code.co_name  # current class name
    
    def __init__(self,
                 schedule: list,
                 finite_looping: int        = 20,
                 session_name: str          = "",
                 session_style: str         = "SQLite",
                 room_id: str               = "room_01",
                 time_shift: (dict, bool)   = False,
                 low_light: bool            = True,
                 rotation: int              = 180,
                 hcdd: (dict, None)         = None,
                 **kwargs):
        lg.info("INIT : {:>85} <<<".format(self.ccn))
        # setting Hard Coded Default Data and updating IF incoming argument can be used.
        # Use this section to define Hard Coded information to enable you to later modify these.
        # NOTE: this data CANNOT be modified at runtime.
        self.hcdd_default = {
            "heartbeat": 20,
            "delta_t_h": 0,
            "delta_t_m": 0,  # TB-R: _dict is appropriate name
            "err_msg_path": "./"}
        if hcdd:  # if <hcdd> update is entered...
            self.hcdd_default.update(hcdd)  # updated the INSTANCE stored default!!!
        self.hcdd = self.hcdd_default
        
        self.room_id: str                   = room_id
        self.finite_looping: int            = finite_looping  # 1- any int: actual int;
        self.low_light: bool                = low_light
        self.rotation: int                  = rotation
        if not session_name:
            self.session_name = '.' + self.room_id + '.db'
        else: self.session_name = session_name
        self.session_style = session_style
        self.session = SQLi.createSession(db_fullname=self.session_name,
                                          tables=[sqlMeasurement.__table__],
                                          style=self.session_style)
        if not time_shift:
            self.time_shift = {'delta_t_h': -1, 'delta_t_m': 0}
        else:
            self.time_shift = time_shift
        self.schedule = schedule
        
        self.go()
        
    def go(self):
        """=== Method name: go =========================================================================================
        ========================================================================================== by Sziller ==="""
        if not self.finite_looping:
            current_loop_count = 0
        else:
            current_loop_count = 1
        while current_loop_count <= self.finite_looping:
            lg.info("{:>4}/{:>4}".format(current_loop_count, self.finite_looping))
            for module in self.schedule:
                lg.debug("module    : {}".format(module))
                module['kwargs'].update(self.time_shift)
                getattr(self, module['function'])(**module['kwargs'])
            if self.finite_looping: current_loop_count += 1

    def run_led_display(self, **kwargs):
        """=== Method name: run_led_display ============================================================================
        -- USED BY several Engines of the MyHomeMyCaste development framework. ---
        -- This is a Raspberry Pi - SenseHat related method. --
        Once parent Engine Class defined, these methods should be part of the Parent Engine class.
        Method runs the LedDisplay class as an instance.
        ========================================================================================== by Sziller ==="""
        lg.info(" - LedDisplay                    === start ===")
        disp = SHLD.LedDisplay(**kwargs)
        disp.sense.low_light = self.low_light
        disp.sense.set_rotation(self.rotation)
        disp.run()
        lg.info(" - LedDisplay                    === ended ===")

    def run_led_clock(self, **kwargs):
        """=== Method name: run_led_display ============================================================================
        -- USED BY several Engines of the MyHomeMyCaste development framework. ---
        -- This is a Raspberry Pi - SenseHat related method. --
        Once parent Engine Class defined, these methods should be part of the Parent Engine class.
        Method runs the LedClock class as an instance.
        ========================================================================================== by Sziller ==="""
        lg.info(" - LedClock                      === start ===")
        clock = SHLC.LedClock(**kwargs)
        clock.sense.low_light = self.low_light
        clock.sense.set_rotation(self.rotation)
        clock.run()
        lg.info(" - LedClock                      === ended ===")

    def run_display_environmental_readings(self, **kwargs):
        """=== Method name: run_led_display ============================================================================
        -- USED BY several Engines of the MyHomeMyCaste development framework. ---
        -- This is a Raspberry Pi - SenseHat related method. --
        Once parent Engine Class defined, these methods should be part of the Parent Engine class.
        Method runs the EnvironmentalReadings class as an instance.
        ========================================================================================== by Sziller ==="""
        lg.info(" - DisplayEnvironmentalReadings  === start ===")
        env_disp = SHSe.EnvironmentalReadings(**kwargs)
        env_disp.sense.low_light = self.low_light
        env_disp.sense.set_rotation(self.rotation)
        env_disp.show_actual_data()
        lg.info(" - DisplayEnvironmentalReadings  === ended ===")
    
    def run_write_environmental_readings(self, **kwargs):
        """=== Method name: run_led_display ============================================================================
        -- USED BY several Engines of the MyHomeMyCaste development framework. ---
        -- This is a Raspberry Pi - SenseHat related method. --
        Once parent Engine Class defined, these methods should be part of the Parent Engine class.
        Method runs the EnvironmentalReadings class as an instance.
        ========================================================================================== by Sziller ==="""
        lg.info(" - WriteEnvironmentalReadings    === start ===")
        env_toDB = SHSe.EnvironmentalReadings(**kwargs)
        read_out = env_toDB.return_data()
        datalist = [
            {
                "mea_loc": self.room_id,
                "mea_type": "temperature",
                "mea_dim": "c",
                "mea_val": read_out["temperature"],
                "mea_time": read_out["time"]},
            {
                "mea_loc": self.room_id,
                "mea_type": "humidity",
                "mea_dim": "%",
                "mea_val": read_out["humidity"],
                "mea_time": read_out["time"]},
            {
                "mea_loc": self.room_id,
                "mea_type": "air_pressure",
                "mea_dim": "bar",
                "mea_val": read_out["air_pressure"],
                "mea_time": read_out["time"]}
        ]
        SQLi.ADD_rows_to_table(primary_key="mea_hash",
                               data_list=datalist,
                               row_obj=sqlMeasurement,
                               session=self.session)
        lg.info(" - WriteEnvironmentalReadings    === ended ===")
        return read_out
