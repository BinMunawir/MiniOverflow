import json

from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.Title import Title
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.UsecaseLayer.ApplicationUsecases.CommentUsecases import commentOnAnswer
from InnerLayers.UsecaseLayer.DataTrnsferObjects.CommentDTO import CommentDTO
from InnerLayers.UsecaseLayer.DataTrnsferObjects.AnswerDTO import AnswerDTO
from OuterLayers.AdapterLayer.RESTAPI.Endpoint import Endpoint
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Exception import HttpException
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


class POSTAnswerComment(Endpoint):
    method = "POST"
    path = "/api/questions/:questionID/answers/:answerID/comments"

    def __init__(self, request: HttpRequest):
        super(POSTAnswerComment, self).__init__(request)

    def handle(self) -> HttpResponse:

        try:
            answerID = self.request.pathParams['answerID']
            commentDTO = CommentDTO()
            commentDTO.body = Body(self.request.body['body'])
        except Exception as e:
            raise HttpException(1111, 'answerID and body are required')

        commentOnAnswer(UUID(answerID), commentDTO)

        return HttpResponse(200, None, None)
