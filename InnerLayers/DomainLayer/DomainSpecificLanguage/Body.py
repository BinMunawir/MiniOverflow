from InnerLayers.DomainLayer.DomainSpecificLanguage.TextContent import TextContent


class Body(TextContent):
    def __init__(self, content):
        super(Body, self).__init__(1000, content)