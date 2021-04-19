from krpc import client

from Mission import Vessel
from Mission.Phases.Phase1 import Phase1
from System.Utilities.KrpcConnection import get_krpc_client
from System.Utilities.Logging import get_system_logger


def mission():
    current_phase = None
    log = get_system_logger()
    astrobotic_lander = Vessel()
    krpc_client = get_krpc_client()

    try:
        current_phase = Phase1()
    except (RuntimeError, Exception) as err:
        log.critical(f"Unhandled {type(err)} has been detected in {current_phase}:\n{err}")
        log.warning(f"Aborting mission")
        abort(krpc_client)
        # TODO: Kill gracefully


def abort(connection: client):
    exit(1)
