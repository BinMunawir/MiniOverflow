from InnerLayers.UsecaseLayer.services.Authentication import Authentication
from InnerLayers.UsecaseLayer.services.UUIDGenerator import UUIDGenerator


class Services:
    uuidGenerator: UUIDGenerator = None
    authentication: Authentication = None

    @staticmethod
    def initialize(uuidGenerator: UUIDGenerator, authentication: Authentication):
        Services.uuidGenerator = uuidGenerator
        Services.authentication = authentication
