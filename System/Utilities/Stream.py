from abc import ABC

from krpc.client import Client


class BaseStream(ABC):
    def __init__(self):
        """  """
        pass


class StreamA(BaseStream):
    def __init__(self):
        """  """
        super().__init__()
        pass


class StreamB(BaseStream):
    def __init__(self):
        """  """
        super().__init__()
        pass
