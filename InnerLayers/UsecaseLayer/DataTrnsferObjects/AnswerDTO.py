from time import time

from InnerLayers.DomainLayer.DomainModels.Answer import Answer
from InnerLayers.DomainLayer.DomainSpecificLanguage.AnswerStatus import AnswerStatus
from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.Time import Time
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.DomainLayer.DomainSpecificLanguage.Vote import Vote
from InnerLayers.UsecaseLayer.DataTrnsferObjects.CommentDTO import CommentDTO
from InnerLayers.UsecaseLayer.Services.Serializable import Serializable


class AnswerDTO(Serializable):
    def __init__(self):
        self.answerID: UUID = None
        self.body: Body = None
        self.createdAt: Time = None
        self.votes: Vote = None
        self.status: AnswerStatus = None
        self.comments: list = None

    def toMap(self) -> dict:
        result = {}

        if self.answerID: result[f'{self.answerID=}'.split('=')[0].split('.')[1]] = self.answerID.toRepresent()
        if self.body: result[f'{self.body=}'.split('=')[0].split('.')[1]] = self.body.toRepresent()
        if self.createdAt: result[f'{self.createdAt=}'.split('=')[0].split('.')[1]] = self.createdAt.toRepresent()
        if self.votes: result[f'{self.votes=}'.split('=')[0].split('.')[1]] = self.votes.toRepresent()
        if self.status: result[f'{self.status=}'.split('=')[0].split('.')[1]] = self.status.toRepresent()

        if self.comments is not None: result[f'{self.comments=}'.split('=')[0].split('.')[1]] = CommentDTO.toListOfMap(
            self.comments)

        return result

    @staticmethod
    def toDTO(answer: Answer):
        dto: AnswerDTO = AnswerDTO()

        dto.answerID = answer.answerID
        dto.body = answer.body
        dto.createdAt = answer.createdAt
        dto.votes = answer.votes
        dto.status = answer.status
        dto.comments = answer.comments

        return dto

    @staticmethod
    def toListOfDTO(answers: list):
        return [AnswerDTO.toDTO(a) for a in answers]
