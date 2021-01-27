from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest


class Endpoint:
    def __init__(self, request: HttpRequest):
        self.request = request

    def handle(self):
        pass

