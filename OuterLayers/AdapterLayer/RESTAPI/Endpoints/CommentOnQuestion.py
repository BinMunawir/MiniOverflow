import json

from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.Title import Title
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.ApplicationUsecases.AnswerUsecases import answerQuestion
from InnerLayers.UsecaseLayer.ApplicationUsecases.CommentUsecases import commentOnQuestion
from InnerLayers.UsecaseLayer.ApplicationUsecases.QuestionUsecases import getQuestions, askQuestion
from InnerLayers.UsecaseLayer.DataTrnsferObjects.AnswerDTO import AnswerDTO
from InnerLayers.UsecaseLayer.DataTrnsferObjects.CommentDTO import CommentDTO
from InnerLayers.UsecaseLayer.DataTrnsferObjects.QuestionDTO import QuestionDTO
from OuterLayers.AdapterLayer.RESTAPI.Endpoint import Endpoint
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


class CommentOnQuestion(Endpoint):
    def __init__(self, request: HttpRequest):
        super(CommentOnQuestion, self).__init__(request)

    def handle(self) -> HttpResponse:
        questionID = UUID(self.request.pathParams['questionID'])
        commentDTO = CommentDTO()
        commentDTO.body = Body(self.request.body['body'])
        commentOnQuestion(questionID, commentDTO)
        response: HttpResponse = HttpResponse(200, None, None)
        return response
