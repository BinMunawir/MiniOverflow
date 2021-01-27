from time import time

from InnerLayers.DomainLayer.DomainModels.Comment import Comment
from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.CommentStatus import CommentStatus
from InnerLayers.DomainLayer.DomainSpecificLanguage.Time import Time
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.UsecaseLayer.Services.Serializable import Serializable


class CommentDTO(Serializable):
    def __init__(self):
        self.commentID: UUID = None
        self.body: Body = None
        self.createdAt: Time = None
        self.status: CommentStatus = None

    def toMap(self) -> dict:
        result = {}

        if self.commentID: result[f'{self.commentID=}'.split('=')[0].split('.')[1]] = self.commentID.toRepresent()
        if self.body: result[f'{self.body=}'.split('=')[0].split('.')[1]] = self.body.toRepresent()
        if self.createdAt: result[f'{self.createdAt=}'.split('=')[0].split('.')[1]] = self.createdAt.toRepresent()
        if self.status: result[f'{self.status=}'.split('=')[0].split('.')[1]] = self.status.toRepresent()

        return result

    @staticmethod
    def toDTO(comment: Comment):
        dto: CommentDTO = CommentDTO()

        dto.commentID = comment.commentID
        dto.body = comment.body
        dto.createdAt = comment.createdAt
        dto.status = comment.status

        return dto

    @staticmethod
    def toListOfDTO(comments: list):
        return [CommentDTO.toDTO(c) for c in comments]
