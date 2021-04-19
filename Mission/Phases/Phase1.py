from datetime import datetime

from krpc import Client

from Mission.Phases import BasePhase
from Mission.Vessel.SystemsCheck import systems_check
from System.Utilities.Logging import get_system_logger
from Mission.Vessel import Vessel


class Phase1(BasePhase):
    def __init__(self, connection: Client, vessel: Vessel):
        super().__init__(phase_name="Phase 1")
        self.start_time = None
        self.end_time = None
        self.logger = get_system_logger()
        self.run()

    def run(self):
        """  """
        self.start_time = datetime.now()
        self.logger.info(f"Commencing {self} at {self.start_time}")

        if not systems_check():
            self.logger.error("There was an issue with the systems check!")
            raise RuntimeError("There was an error with the")

        self.end_time = datetime.now()

    def report(self):
        """  """
        self.logger.info("")
