from time import time

from InnerLayers.DomainLayer.DomainSpecificLanguage.AnswerStatus import AnswerStatus
from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.Name import Name
from InnerLayers.DomainLayer.DomainSpecificLanguage.Time import Time
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.DomainLayer.DomainSpecificLanguage.Vote import Vote
from InnerLayers.UsecaseLayer.services.Serializable import Serializable


class TagDTO(Serializable):
    def __init__(self):
        self.taqID: UUID = None
        self.name: Name = None
        self.createdAt: Time = None

    def toMap(self) -> dict:
        result = {}

        if self.tagID: result[f'{self.taqID=}'.split('=')[0].split('.')[1]] = self.taqID.toRepresent()
        if self.name: result[f'{self.name=}'.split('=')[0].split('.')[1]] = self.name.toRepresent()
        if self.createdAt: result[f'{self.createdAt=}'.split('=')[0].split('.')[1]] = self.createdAt.toRepresent()

        return result
