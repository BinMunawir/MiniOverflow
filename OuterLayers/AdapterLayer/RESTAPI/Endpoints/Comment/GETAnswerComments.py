import json

from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.UsecaseLayer.ApplicationUsecases.CommentUsecases import getAnswerComments
from InnerLayers.UsecaseLayer.DataTrnsferObjects.CommentDTO import CommentDTO
from InnerLayers.UsecaseLayer.DataTrnsferObjects.AnswerDTO import AnswerDTO
from OuterLayers.AdapterLayer.RESTAPI.Endpoint import Endpoint
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Exception import HttpException
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


class GETAnswerComments(Endpoint):
    method = "GET"
    path = "/api/questions/:questionID/answers/:answerID/comments"

    def __init__(self, request: HttpRequest):
        super(GETAnswerComments, self).__init__(request)

    def handle(self) -> HttpResponse:
        try:
            answerID = self.request.pathParams['answerID']
        except Exception as e:
            raise HttpException(1111, 'answerID are required')

        comments = getAnswerComments(UUID(answerID))
        commentsMap = CommentDTO.toListOfMap(comments)

        response: HttpResponse = HttpResponse(200, {'Content-Type': 'application/json'}, json.dumps(commentsMap))
        return response
