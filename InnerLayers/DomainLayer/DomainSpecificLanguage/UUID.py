
class UUID:
    def __init__(self, uuid):
        self.UUID = uuid

    def isSameAs(self, another):
        return self.UUID == another.UUID

    def toRepresent(self):
        return self.UUID
