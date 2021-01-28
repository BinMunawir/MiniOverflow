import json

from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.UsecaseLayer.ApplicationUsecases.CommentUsecases import getQuestionComments
from InnerLayers.UsecaseLayer.ApplicationUsecases.QuestionUsecases import getQuestions
from InnerLayers.UsecaseLayer.DataTrnsferObjects.CommentDTO import CommentDTO
from InnerLayers.UsecaseLayer.DataTrnsferObjects.QuestionDTO import QuestionDTO
from OuterLayers.AdapterLayer.RESTAPI.Endpoint import Endpoint
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Exception import HttpException
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


class GETQuestionComments(Endpoint):
    method = "GET"
    path = "/api/questions/:questionID/comments"

    def __init__(self, request: HttpRequest):
        super(GETQuestionComments, self).__init__(request)

    def handle(self) -> HttpResponse:
        try:
            questionID = self.request.pathParams['questionID']
        except Exception as e:
            raise HttpException(1111, 'questionID are required')

        comments = getQuestionComments(UUID(questionID))
        commentsMap = CommentDTO.toListOfMap(comments)

        response: HttpResponse = HttpResponse(200, {'Content-Type': 'application/json'}, json.dumps(commentsMap))
        return response
