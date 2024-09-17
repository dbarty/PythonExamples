# https://docs.python.org/3/howto/enum.html

from datetime import date
from enum import Enum, auto

class Weekday(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()

    @classmethod
    def from_date(cls, date):
        return cls(date.isoweekday())

weekday = Weekday.from_date(date.today())
print(weekday)
