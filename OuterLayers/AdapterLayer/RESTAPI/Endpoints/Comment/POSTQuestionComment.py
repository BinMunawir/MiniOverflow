import json

from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.Title import Title
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.UsecaseLayer.ApplicationUsecases.CommentUsecases import commentOnQuestion
from InnerLayers.UsecaseLayer.ApplicationUsecases.QuestionUsecases import askQuestion
from InnerLayers.UsecaseLayer.DataTrnsferObjects.CommentDTO import CommentDTO
from InnerLayers.UsecaseLayer.DataTrnsferObjects.QuestionDTO import QuestionDTO
from OuterLayers.AdapterLayer.RESTAPI.Endpoint import Endpoint
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Exception import HttpException
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


class POSTQuestionComment(Endpoint):
    method = "POST"
    path = "/api/questions/:questionID/comments"

    def __init__(self, request: HttpRequest):
        super(POSTQuestionComment, self).__init__(request)

    def handle(self) -> HttpResponse:

        try:
            questionID = self.request.pathParams['questionID']
            commentDTO = CommentDTO()
            commentDTO.body = Body(self.request.body['body'])
        except Exception as e:
            raise HttpException(1111, 'questionID and body are required')

        commentOnQuestion(UUID(questionID), commentDTO)

        return HttpResponse(200, None, None)
