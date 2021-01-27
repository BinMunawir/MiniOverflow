from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.UsecaseLayer.Services.UUIDGenerator import UUIDGenerator
import uuid


class UUIDModel(UUIDGenerator):
    def generate(self) -> UUID:
        return UUID(str(uuid.uuid4())[:8])
