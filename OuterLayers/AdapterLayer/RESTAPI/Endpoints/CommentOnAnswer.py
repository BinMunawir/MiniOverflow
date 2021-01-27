import json

from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.Title import Title
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.ApplicationUsecases.CommentUsecases import commentOnAnswer
from InnerLayers.UsecaseLayer.DataTrnsferObjects.AnswerDTO import AnswerDTO
from InnerLayers.UsecaseLayer.DataTrnsferObjects.CommentDTO import CommentDTO
from InnerLayers.UsecaseLayer.DataTrnsferObjects.AnswerDTO import AnswerDTO
from OuterLayers.AdapterLayer.RESTAPI.Endpoint import Endpoint
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


class CommentOnAnswer(Endpoint):
    def __init__(self, request: HttpRequest):
        super(CommentOnAnswer, self).__init__(request)

    def handle(self) -> HttpResponse:
        answerID = UUID(self.request.pathParams['answerID'])
        commentDTO = CommentDTO()
        commentDTO.body = Body(self.request.body['body'])
        commentOnAnswer(answerID, commentDTO)
        response: HttpResponse = HttpResponse(200, None, None)
        return response
