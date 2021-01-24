

from datetime import datetime

class Time:
    def __init__(self, unixTime):
        self.UNIX_TIME = unixTime
        time = datetime.fromtimestamp(unixTime)
        self.YEAR = time.year
        self.MONTH = time.month
        self.DAY = time.day
        self.HOUR = time.hour
        self.MINUTE = time.minute
        self.SECOND = time.second

    def isLessThan(self, another):
        return self.UNIX_TIME < another.UNIX_TIME

    def isEqualTo(self, another):
        return self.UNIX_TIME == another.UNIX_TIME

    def isMoreThan(self, another):
        return self.UNIX_TIME > another.UNIX_TIME
