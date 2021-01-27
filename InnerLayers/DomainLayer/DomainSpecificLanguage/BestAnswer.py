
from datetime import datetime
import time

from InnerLayers.DomainLayer.DomainSpecificLanguage.Time import Time
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID


class BestAnswer:
    def __init__(self, answerID):
        self.ANSWER_ID = UUID(answerID)
        self.DATE = Time(time.time())

    def toRepresent(self):
        return {
            f'{self.ANSWER_ID=}'.split('=')[0].split('.')[1].lower(): self.ANSWER_ID.toRepresent(),
            f'{self.DATE=}'.split('=')[0].split('.')[1].lower(): self.DATE.toRepresent()
        }
