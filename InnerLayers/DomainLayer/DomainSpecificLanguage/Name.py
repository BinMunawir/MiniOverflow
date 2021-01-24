from InnerLayers.DomainLayer.DomainSpecificLanguage.TextContent import TextContent


class Name(TextContent):
    def __init__(self, name):
        super(Name, self).__init__(30, name)
