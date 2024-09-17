# https://docs.python.org/3/howto/enum.html

from datetime import date
from enum import Flag, auto

class Weekday(Flag):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()

weekend = Weekday.SATURDAY | Weekday.SUNDAY
print(weekend)
print(Weekday.SATURDAY in weekend)
