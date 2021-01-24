from time import time

from InnerLayers.DomainLayer.DomainSpecificLanguage.AnswerStatus import AnswerStatus
from InnerLayers.DomainLayer.DomainSpecificLanguage.BestAnswer import BestAnswer
from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.QuestionStatus import QuestionStatus
from InnerLayers.DomainLayer.DomainSpecificLanguage.Time import Time
from InnerLayers.DomainLayer.DomainSpecificLanguage.Title import Title
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.DomainLayer.DomainSpecificLanguage.Vote import Vote


class Question:
    def __init__(self, questionID, title, body, tags=[]):
        self.questionID = UUID(questionID)
        self.title = Title(title)
        self.body = Body(body)
        self.createdAt = Time(time())
        self.votes = Vote(0)
        self.tags = tags
        self.bestAnswer = None
        self.status = QuestionStatus.PENDING()
        self.comments = []
        self.answers = []

    def editTitle(self, newTitle):
        self.title = Title(newTitle)

    def editBody(self, newBody):
        self.body = Body(newBody)

    def editTags(self, newTags):
        self.tags = newTags

    def changeStatus(self, newStatus):
        self.status = newStatus

    def voteFor(self):
        self.votes = self.votes.increase()

    def voteAgainst(self):
        self.votes = self.votes.decrease()

    def comment(self, comment):
        self.comments.append(comment)

    def answer(self, answer):
        self.answers.append(answer)

    def chooseAsBestAnswer(self, answerID):
        self.bestAnswer = BestAnswer(answerID)

    def isAnswered(self):
        if self.bestAnswer: True
        return False

