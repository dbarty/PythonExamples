# https://docs.python.org/3/howto/enum.html

from datetime import date
from enum import Enum, auto

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    @classmethod
    def from_date(cls, date):
        return cls(date.isoweekday())

weekday = Weekday.from_date(date.today())
print(weekday)
