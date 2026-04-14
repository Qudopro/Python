#timewithproperties.py
"""Class Time with read-write properties"""

class Time:
    """Class Time with read-write properties"""
    def __init__(self, hour=0, minute=0, second=0):
        """Initialize each attribute."""
        self.hour = hour
        self.minute = minute
        self.second = second

    #Get method
    @property
    def hour(self):
        """Return hour."""
        return self._hour

    #Set method
    @hour.setter
    def hour(self, hour):
        """Set hour."""
        if not(0 <= hour <= 23):
            raise ValueError(f'hour {hour} must be between 0 and 23')
        self._hour = hour

    @property
    def minute(self):
        """Return minute."""
        return self._minute

    @minute.setter
    def minute(self, minute):
        """Set minute."""
        if not(0 <= minute <= 59):
            raise ValueError(f'minute {minute} must be between 0 and 59')
        self._minute = minute

    @property
    def second(self):
        """Return second."""
        return self._second

    @second.setter
    def second(self, second):
        """Set second."""
        if not(0 <= second <= 59):
            raise ValueError(f'second {second} must be between 0 and 59')
        self._second = second

    def set_time(self, hour=0, minute=0, second=0):
        """Set values of hour, minute, second."""
        self.hour = hour
        self.minute = minute
        self.second = second

    #This method can be used by eval() to create and initialize an object containing values specified in the string
    def __repr__(self):
        """Return Time string for repr()"""
        return (f'Time(hour={self.hour}, minute={self.minute}, second={self.second})')      #Looks like a constructor expression

    def __str__(self):
        """Print Time in 12-hour clock format"""
        return (('12' if self.hour in (0, 12) else str(self.hour % 12)) +
                f':{self.minute:0>2}:{self.second:0>2}' +
                (' AM' if self.hour < 12 else ' PM')
                )
