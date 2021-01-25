from InnerLayers.UsecaseLayer.services.Authentication import Authentication
from InnerLayers.UsecaseLayer.services.UUIDGenerator import UUIDGenerator


class Services:
    def __init__(self):
        self.uuidGenerator: UUIDGenerator = None
        self.authentication: Authentication = None

    def initialize(self, uuidGenerator: UUIDGenerator, authentication: Authentication):
        self.uuidGenerator = uuidGenerator
        self.authentication = authentication
