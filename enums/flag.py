# https://docs.python.org/3/howto/enum.html

from datetime import date
from enum import Flag

class Weekday(Flag):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 4
    THURSDAY = 8
    FRIDAY = 16
    SATURDAY = 32
    SUNDAY = 64

weekend = Weekday.SATURDAY | Weekday.SUNDAY
print(weekend)
print(Weekday.SATURDAY in weekend)
