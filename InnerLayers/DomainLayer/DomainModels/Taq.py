from time import time

from InnerLayers.DomainLayer.DomainSpecificLanguage.AnswerStatus import AnswerStatus
from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.Time import Time
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.DomainLayer.DomainSpecificLanguage.Vote import Vote


class Taq:
    def __init__(self, taqID, name):
        self.taqID = taqID
        self.name = name
        self.createdAt = Time(time())
        self.questions = []

    def addQuestion(self, question):
        self.questions.append(question)

    def doesContains(self, questionID):
        for q in self.questions:
            if questionID == q.questionID: return True
        return False
