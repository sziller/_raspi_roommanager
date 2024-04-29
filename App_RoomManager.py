"""=== App-interface to start RoomManager Application. =======================================
============================================================================ by Sziller ==="""

from time_format import TimeFormat as TiFo
from dotenv import load_dotenv
import logging
import inspect
import config as conf
from engine_RoomManager import Engine_RoomManager as EnRM


def app_room_manager(**data_passed):
    """=== Function name: app_room_manager =============================================================================
    Ust tihs code to run you Room Manager!
    ============================================================================================== by Sziller ==="""
    cfn = inspect.currentframe().f_code.co_name  # current class name
    lg.info("START: {:>85} <<<".format(cfn))
    lg.warning("          : ======================================")
    lg.warning({True: "          : =            LIVE SESSION            =",
                False: "          : =            DEV  SESSION            ="}[conf.isLIVE])
    lg.warning("          : ={:^36}=".format(__name__))
    lg.info("          : =         user languange: {}         =".format(LNG))
    lg.warning("          : ======================================")
    for p, a, in data_passed.items():
        lg.debug("{:>12}: {}".format(p, a))
    EnRM.EngineRoomManager(**data_passed)


if __name__ == "__main__":
    # READ BASIC SETTINGS                                                                   -   START   -
    # from .env:
    load_dotenv()
    # from config.py:
    # language settings:
    LNG                 = conf.LANGUAGE_CODE
    # path settings:
    root_path = conf.PATH_ROOT
    err_msg_path = conf.PATH_ERROR_MSG
    # log settings:
    log_format          = conf.LOG_FORMAT
    log_level           = getattr(logging, conf.LOG_LEVEL)
    log_ts              = "_{}".format(TiFo.timestamp()) if conf.LOG_TIMED else ""
    log_tf              = conf.LOG_TIMEFORMAT
    log_filename        = conf.LOG_FILENAME.format(root_path, log_ts)
    # app settings:
    app_id              = conf.APP_ID
    app_schedule        = conf.APP_SCHEDULE
    app_loop_n_times    = conf.APP_LOOP_N_TIMES
    app_is_low_light    = conf.APP_LOW_LIGHT
    app_time_shift      = conf.APP_TIME_SHIFT
    # DB settings:
    session_name        = conf.DB_SESSION_NAME
    # READ BASIC SETTINGS                                                                   -   ENDED   -

    # Setting up logger                                                                     -   START   -
    lg = logging.getLogger(__name__)
    # Using config.py data - configurate logger:
    logging.basicConfig(filename=log_filename, level=log_level, format=log_format, datefmt=log_tf, filemode="w")
    # initial messages:
    lg.warning("FILE: {:>86} <<<".format(__file__))
    lg.warning("LOGGER namespace: {:>74} <<<".format(__name__))
    lg.debug("listing   : config settings:")
    for k, v in {param: arg for param, arg in vars(conf).items() if not param.startswith('__')}.items():
        lg.debug("{:>20}: {}".format(k, v))
    # Setting up logger                                                                     -   ENDED   -
    
    # Run App:
    
    app_room_manager(finite_looping=app_loop_n_times,
                     room_id=app_id,
                     schedule=app_schedule,
                     time_shift=app_time_shift,
                     low_light=app_is_low_light,
                     session_name=session_name,
                     )
