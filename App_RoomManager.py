from RoomManagerEngine import RoomManagerEngine as RMEn
from SenseHatLedClock.Class_SenseHatLedClock import LedClock
from SenseHatLedDisplay.Class_SenseHatLedDisplay import LedDisplay
from SenseHatSensors.Class_SenseHatSensors import EnvironmentalReadings


def app_room_manager(**data_passed):
    app = RMEn.RoomManager(**data_passed)
    app.initiate()


if __name__ == "__main__":
    _schedule = [
        {'function': LedClock,                  'kwargs': {'duration': 45, 'heartbeat': 1}},
        {'function': LedDisplay,                'kwargs': {'duration': 5, 'dyn': True, 'alias': 0, 'heartbeat': 0.1}},
        {'function': EnvironmentalReadings,     'kwargs': {'code': 7, 'scroll_speed': 0.075}}
    ]
    _time_shift = \
        {}
        # {'delta_t_h': -1, 'delta_t_m': 0}
    app_room_manager(finite_looping=2000, schedule=_schedule, time_shift=_time_shift)

