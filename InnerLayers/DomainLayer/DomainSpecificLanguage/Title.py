from InnerLayers.DomainLayer.DomainSpecificLanguage.TextContent import TextContent


class Title(TextContent):
    def __init__(self, content):
        super(Title, self).__init__(70, content)