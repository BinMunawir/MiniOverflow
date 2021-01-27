from time import time

from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.CommentStatus import CommentStatus
from InnerLayers.DomainLayer.DomainSpecificLanguage.Time import Time
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID


class Comment:
    def __init__(self, commentID=None, body=None, createdAt=None, status=None):
        self.commentID: UUID = commentID
        self.body: Body = body
        self.createdAt: Time = createdAt
        self.status: CommentStatus = status

    def editBody(self, newBody):
        self.body = Body(newBody)

    def changeStatus(self, newStatus):
        self.status = newStatus
