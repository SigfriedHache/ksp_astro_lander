from krpc.client import Client

from System.Utilities.Logging import get_system_logger, get_telemetry_logger
from System.Utilities.Stream import StreamA


class Telemetry:
    system_logger = get_system_logger()
    telemetry_logger = get_telemetry_logger()
    system_logger.info("Hello World!")

    def __init__(self, *, connection: Client = None):
        """
        :param connection:
        """
        # TODO: I want the actual data elements of the telemetry to be read-only properties.
        #  The things being telemetered should be accessible externally
        #  Telemetry should kick off at the beginning of the mission, and the method to call it should be passed around
        #

        # ping the client
        self.position, self.velocity = [None] * 2
        self.position_stream, self.velocity_stream = [StreamA(connection)] * 2


    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity = value

