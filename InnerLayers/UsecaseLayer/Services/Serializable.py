class Serializable:

    def toMap(self) -> dict:
        pass

    @staticmethod
    def toListOfMap(aList: list) -> list:
        result = []
        for l in aList:
            result.append(l.toMap())
        return result
