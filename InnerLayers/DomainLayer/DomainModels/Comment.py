from time import time

from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.CommentStatus import CommentStatus
from InnerLayers.DomainLayer.DomainSpecificLanguage.Time import Time
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID


class Comment:
    def __init__(self, commentID, body):
        self.commentID = UUID(commentID)
        self.body = Body(body)
        self.createdAt = Time(time())
        self.status = CommentStatus.PENDING()

    def editBody(self, newBody):
        self.body = Body(newBody)

    def changeStatus(self, newStatus):
        self.status = newStatus
