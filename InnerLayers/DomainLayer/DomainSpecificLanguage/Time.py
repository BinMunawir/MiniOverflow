from datetime import datetime
from time import time


class Time:
    def __init__(self, unixTime=time()):
        self.UNIX_TIME = float(unixTime)
        self.YEAR = datetime.fromtimestamp(self.UNIX_TIME).year
        self.MONTH = datetime.fromtimestamp(self.UNIX_TIME).month
        self.DAY = datetime.fromtimestamp(self.UNIX_TIME).day
        self.HOUR = datetime.fromtimestamp(self.UNIX_TIME).hour
        self.MINUTE = datetime.fromtimestamp(self.UNIX_TIME).minute
        self.SECOND = datetime.fromtimestamp(self.UNIX_TIME).second

    def isLessThan(self, another):
        return self.UNIX_TIME < another.UNIX_TIME

    def isEqualTo(self, another):
        return self.UNIX_TIME == another.UNIX_TIME

    def isMoreThan(self, another):
        return self.UNIX_TIME > another.UNIX_TIME

    def toRepresent(self):
        return str(self.UNIX_TIME)
