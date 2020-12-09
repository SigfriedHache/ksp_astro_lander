import AstroUtilities
import krpc

class Vessel():
    def __init__(self, connection, vessel_name, telemetry_log_handle, system_log_handle):
        """
        Initialize different streamed/static elements of the vessel
        """
        self.telemetry_logger = AstroUtilities.getLogger(telemetry_log_handle)
        self.system_logger = AstroUtilities.getLogger(system_log_handle)
        self.system_logger.info(str(vessel_name) + " initializing...")
        self.velocity = True
        self.orbit = True
        self.control = True

    def start_telemetry(self):
        print "Logging started"

if __name__ == "__main__":
    raise Exception("There is no __main__ method to call for this file.")
