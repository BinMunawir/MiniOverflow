

from datetime import datetime
from time import time

class Time:
    def __init__(self, unixTime=time()):
        self.UNIX_TIME = unixTime
        self.YEAR = datetime.fromtimestamp(unixTime).year
        self.MONTH = datetime.fromtimestamp(unixTime).month
        self.DAY = datetime.fromtimestamp(unixTime).day
        self.HOUR = datetime.fromtimestamp(unixTime).hour
        self.MINUTE = datetime.fromtimestamp(unixTime).minute
        self.SECOND = datetime.fromtimestamp(unixTime).second

    def isLessThan(self, another):
        return self.UNIX_TIME < another.UNIX_TIME

    def isEqualTo(self, another):
        return self.UNIX_TIME == another.UNIX_TIME

    def isMoreThan(self, another):
        return self.UNIX_TIME > another.UNIX_TIME

    def toRepresent(self):
        return str(self.UNIX_TIME)