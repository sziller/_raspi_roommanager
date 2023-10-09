"""
Room manager module starting script template.
"""

from RoomManager import RoomManagerEngine as RMEn
from SenseHatLedClock.Class_SenseHatLedClock import LedClock
from SenseHatLedDisplay.Class_SenseHatLedDisplay import LedDisplay
from SenseHatSensors.Class_SenseHatSensors import EnvironmentalReadings


def app_room_manager(**data_passed):
    """=== Function name: app_room_manager =============================================================================
    
    ============================================================================================== by Sziller ==="""
    for k, v, in data_passed.items():
        print(k, v)
    app = RMEn.RoomManagerEngine(**data_passed)


if __name__ == "__main__":
    _schedule = [
        {'function': "run_led_clock",                   'kwargs': {'duration': 3, 'heartbeat': 0.1, "clock_style": 1}},
        {'function': "run_led_display", 'kwargs': {'duration': 3, 'heartbeat': 0.1, "dyn": True, "alias": 1}},
        {'function': "run_write_environmental_readings",     'kwargs': {'code': 7, 'scroll_speed': 0.075}}
    ]
    _time_shift = \
        {}
        # {'delta_t_h': -1, 'delta_t_m': 0}
    app_room_manager(finite_looping=20,
                     schedule=_schedule,
                     time_shift=_time_shift,
                     low_light=False,
                     session_name=".RoomManager.db")

