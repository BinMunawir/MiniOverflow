
from datetime import datetime
import time

from InnerLayers.DomainLayer.DomainSpecificLanguage.Time import Time
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID


class BestAnswer:
    def __init__(self, uuid):
        self.UUID: UUID(uuid)
        self.DATE: Time(time.time())