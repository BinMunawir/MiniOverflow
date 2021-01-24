from InnerLayers.DomainLayer.DomainSpecificLanguage.TextContent import TextContent


class Name(TextContent):
    def __init__(self, content):
        super(Name, self).__init__(30, content)
