from abc import ABC, abstractmethod
# from krpc.client import Client
# from Mission.Vessel.Telemetry import Telemetry


class BasePhase(ABC):
    def __init__(self, phase_name: str):
        """ Initialize the phase """
        self._name = phase_name
        pass

    def __str__(self):
        """ Return string name of the class """
        return self.__class__.__name__

    @abstractmethod
    def run(self):
        """  """
        pass

    @abstractmethod
    def execute(self):
        """  """
        pass

    @abstractmethod
    def logging(self):
        """  """
        pass
