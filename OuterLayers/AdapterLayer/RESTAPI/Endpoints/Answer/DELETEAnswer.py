import json

from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.UsecaseLayer.ApplicationUsecases.AnswerUsecases import softDeleteAnswer, hardDeleteAnswer
from InnerLayers.UsecaseLayer.DataTrnsferObjects.AnswerDTO import AnswerDTO
from OuterLayers.AdapterLayer.RESTAPI.Endpoint import Endpoint
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Exception import HttpException
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


class DELETEAnswer(Endpoint):
    method = "DELETE"
    path = "/api/questions/:questionID/answers/:answerID"

    def __init__(self, request: HttpRequest):
        super(DELETEAnswer, self).__init__(request)

    def handle(self) -> HttpResponse:
        try:
            answerID = self.request.pathParams['answerID']
        except Exception as e:
            raise HttpException(1111, 'answerID is required')

        if 'hard' in self.request.headers:
            hardDeleteAnswer(UUID(answerID))
        else:
            softDeleteAnswer(UUID(answerID))

        return HttpResponse(200, None, None)
