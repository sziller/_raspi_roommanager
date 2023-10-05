"""
Room manager module starting script template.
"""

from RoomManagerEngine import RoomManagerEngine as RMEn
from SenseHatLedClock.Class_SenseHatLedClock import LedClock
from SenseHatLedDisplay.Class_SenseHatLedDisplay import LedDisplay
from SenseHatSensors.Class_SenseHatSensors import EnvironmentalReadings


def app_room_manager(**data_passed):
    """=== Function name: app_room_manager =============================================================================
    
    ============================================================================================== by Sziller ==="""
    app = RMEn.RoomManager(**data_passed)
    app.initiate()


if __name__ == "__main__":
    _schedule = [
        {'function': "run_led_clock",                   'kwargs': {'duration': 5, 'heartbeat': 1}},
        {'function': "run_led_display",                 'kwargs': {'duration': 5, 'heartbeat': 0.1,
                                                                   'dyn': True, 'alias': 0}},
        {'function': "run_led_display",                 'kwargs': {'duration': 5, 'heartbeat': 0.1,
                                                                   'dyn': False, 'alias': 2}},
        
        # {'function': "run_environmental_readings",     'kwargs': {'code': 7, 'scroll_speed': 0.075}}
    ]
    _time_shift = \
        {}
        # {'delta_t_h': -1, 'delta_t_m': 0}
    app_room_manager(finite_looping=2, schedule=_schedule, time_shift=_time_shift)

