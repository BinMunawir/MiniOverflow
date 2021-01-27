from time import time

from InnerLayers.DomainLayer.DomainModels.Question import Question
from InnerLayers.DomainLayer.DomainSpecificLanguage.AnswerStatus import AnswerStatus
from InnerLayers.DomainLayer.DomainSpecificLanguage.BestAnswer import BestAnswer
from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.QuestionStatus import QuestionStatus
from InnerLayers.DomainLayer.DomainSpecificLanguage.Time import Time
from InnerLayers.DomainLayer.DomainSpecificLanguage.Title import Title
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.DomainLayer.DomainSpecificLanguage.Vote import Vote
from InnerLayers.UsecaseLayer.DataTrnsferObjects.AnswerDTO import AnswerDTO
from InnerLayers.UsecaseLayer.DataTrnsferObjects.CommentDTO import CommentDTO
from InnerLayers.UsecaseLayer.DataTrnsferObjects.TagDTO import TagDTO
from InnerLayers.UsecaseLayer.Services.Serializable import Serializable


class QuestionDTO(Serializable):
    def __init__(self):
        self.questionID: UUID = None
        self.title: Title = None
        self.bestAnswer: BestAnswer = None
        self.body: Body = None
        self.createdAt: Time = None
        self.votes: Vote = None
        self.status: QuestionStatus = None
        self.tags: list = None
        self.answers: list = None
        self.comments: list = None

    def toMap(self) -> dict:
        result = {}

        if self.questionID: result[f'{self.questionID=}'.split('=')[0].split('.')[1]] = self.questionID.toRepresent()
        if self.title: result[f'{self.title=}'.split('=')[0].split('.')[1]] = self.title.toRepresent()
        if self.bestAnswer: result[f'{self.bestAnswer=}'.split('=')[0].split('.')[1]] = self.bestAnswer.toRepresent()
        if self.body: result[f'{self.body=}'.split('=')[0].split('.')[1]] = self.body.toRepresent()
        if self.createdAt: result[f'{self.createdAt=}'.split('=')[0].split('.')[1]] = self.createdAt.toRepresent()
        if self.votes: result[f'{self.votes=}'.split('=')[0].split('.')[1]] = self.votes.toRepresent()
        if self.status: result[f'{self.status=}'.split('=')[0].split('.')[1]] = self.status.toRepresent()

        print(33, self.tags)
        if self.tags is not None: result[f'{self.tags=}'.split('=')[0].split('.')[1]] = TagDTO.toListOfMap(self.tags)
        print(44, result['tags'])
        if self.answers is not None: result[f'{self.answers=}'.split('=')[0].split('.')[1]] = AnswerDTO.toListOfMap(self.answers)
        if self.comments is not None: result[f'{self.comments=}'.split('=')[0].split('.')[1]] = CommentDTO.toListOfMap(
            self.comments)

        return result

    @staticmethod
    def toDTO(question: Question):
        dto: QuestionDTO = QuestionDTO()

        dto.questionID = question.questionID
        dto.title = question.title
        dto.bestAnswer = question.bestAnswer
        dto.body = question.body
        dto.createdAt = question.createdAt
        dto.votes = question.votes
        dto.status = question.status
        dto.tags = question.tags
        dto.answers = question.answers
        dto.comments = question.comments

        return dto

    @staticmethod
    def toListOfDTO(questions: list):
        return [QuestionDTO.toDTO(q) for q in questions]
