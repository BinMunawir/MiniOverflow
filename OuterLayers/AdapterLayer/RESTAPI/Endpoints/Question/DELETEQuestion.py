import json

from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.UsecaseLayer.ApplicationUsecases.QuestionUsecases import getQuestions, getQuestion, softDeleteQuestion, \
    hardDeleteQuestion
from InnerLayers.UsecaseLayer.DataTrnsferObjects.QuestionDTO import QuestionDTO
from OuterLayers.AdapterLayer.RESTAPI.Endpoint import Endpoint
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Exception import HttpException
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


class DELETEQuestion(Endpoint):
    method = "DELETE"
    path = "/api/questions/:questionID"

    def __init__(self, request: HttpRequest):
        super(DELETEQuestion, self).__init__(request)

    def handle(self) -> HttpResponse:
        try:
            questionID = self.request.pathParams['questionID']
        except Exception as e:
            raise HttpException(1111, 'questionID is required')

        if 'hard' in self.request.headers:
            hardDeleteQuestion(UUID(questionID))
        else:
            softDeleteQuestion(UUID(questionID))

        return HttpResponse(200, None, None)
