class Vote:
    def __init__(self, counter):
        self.COUNTER = counter

    def increase(self):
        return Vote(self.COUNTER + 1)

    def decrease(self):
        return Vote(self.COUNTER - 1)

    def isLessThan(self, another):
        return self.COUNTER < another.COUNTER

    def isEqualTo(self, another):
        return self.COUNTER == another.COUNTER

    def isMoreThan(self, another):
        return self.COUNTER > another.COUNTER
