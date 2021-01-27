
class Status:
    def __init__(self, name):
        self.NAME = name

    def isSameAs(self, another):
        return type(self) == type(another) & self.NAME == self.NAME

    def toRepresent(self):
        return self.NAME