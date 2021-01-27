class TextContent:
    def __init__(self, maxCharacter, content):
        self.MAX_CHARACTER = maxCharacter
        self.CONTENT = content

    def _isSameAs(self, another):
        return type(self) == type(another) & self.CONTENT == another.CONTENT

    def toRepresent(self):
        return self.CONTENT
