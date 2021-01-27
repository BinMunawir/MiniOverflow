import json

from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.Title import Title
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.ApplicationUsecases.CommentUsecases import getAnswerComments
from InnerLayers.UsecaseLayer.DataTrnsferObjects.CommentDTO import CommentDTO
from InnerLayers.UsecaseLayer.DataTrnsferObjects.AnswerDTO import AnswerDTO
from OuterLayers.AdapterLayer.RESTAPI.Endpoint import Endpoint
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


class GetCommentsOfAnswer(Endpoint):
    def __init__(self, request: HttpRequest):
        super(GetCommentsOfAnswer, self).__init__(request)

    def handle(self) -> HttpResponse:
        answerID = UUID(self.request.pathParams['answerID'])
        comments = getAnswerComments(answerID)
        comments = CommentDTO.toListOfMap(comments)
        response: HttpResponse = HttpResponse(200, {'Content-Type': 'application/json'}, json.dumps(comments))
        return response
