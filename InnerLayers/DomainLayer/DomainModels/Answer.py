from time import time

from InnerLayers.DomainLayer.DomainSpecificLanguage.AnswerStatus import AnswerStatus
from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.Time import Time
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.DomainLayer.DomainSpecificLanguage.Vote import Vote


class Answer:
    def __init__(self, answerID=None, body=None, createdAt=None, votes=None, status=None, comments=None):
        self.answerID: UUID = answerID
        self.body: Body = body
        self.createdAt: Time = createdAt
        self.votes: Vote = votes
        self.status: AnswerStatus = status
        self.comments: list = comments

    def editBody(self, newBody):
        self.body = Body(newBody)

    def changeStatus(self, newStatus):
        self.status = newStatus

    def voteFor(self):
        self.votes = self.votes.increase()

    def voteAgainst(self):
        self.votes = self.votes.decrease()

    def comment(self, comment):
        self.comments.append(comment)