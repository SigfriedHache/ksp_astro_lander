from datetime import datetime, timedelta
from time import sleep
from typing import Union

DurationTypes = (int, float, timedelta)


class Duration:

    def __init__(self, duration: Union[DurationTypes]):
        """
        This function initializes the duration property by invoking the @duration.setter
        :param duration:
        """
        self.duration = duration

    @property
    def duration(self) -> Union[DurationTypes]:
        """
        This function is the basic property getter.
        :return: Returns the "privately"-stored self._duration property in its original data format
                 (i.e. in DurationTypes; note that it can never be set as a datetime type.)
        """
        return self._duration

    @duration.setter
    def duration(self, duration: Union[DurationTypes]):
        """
        This function validates, then sets the duration property
        :param duration:
        :return:
        """
        if type(duration) not in DurationTypes:
            raise TypeError(f"Expected a type in {DurationTypes}. "
                            f"The entered value '{duration}' has type: {type(duration)}")

        self._duration = duration

    @duration.getter
    def int(self) -> int:
        return self.__int__()

    def __int__(self) -> int:
        """ This function returns the set duration as an int """
        if isinstance(self._duration, (int, float)):
            return int(self._duration)
        else:
            return int(self._duration.total_seconds())

    @duration.getter
    def float(self) -> float:
        return self.__float__()

    def __float__(self) -> float:
        """ This function returns the set duration as a float """
        if isinstance(self._duration, (int, float)):
            return float(self._duration)
        else:
            return float(self._duration.total_seconds())

    @duration.getter
    def timedelta(self) -> timedelta:
        """
        This function returns duration as datetime.timedelta
        :return:
        """
        if isinstance(self._duration, timedelta):
            return self._duration
        else:
            return timedelta(seconds=self._duration)

    def datetime(self) -> datetime:
        """
        This function returns a datetime.datetime, offset by the self._duration value (e.g. now + 5s)
        :return:
        """
        if isinstance(self._duration, timedelta):
            return datetime.now() + self._duration
        else:
            return datetime.now() + timedelta(seconds=self._duration)

    def wait(self):
        """
        This function sleeps for the self._duration value
        :return:
        """
        sleep(self.float)
