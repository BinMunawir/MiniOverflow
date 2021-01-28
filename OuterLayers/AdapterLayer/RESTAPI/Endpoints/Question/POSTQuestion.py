import json

from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.Title import Title
from InnerLayers.UsecaseLayer.ApplicationUsecases.QuestionUsecases import askQuestion
from InnerLayers.UsecaseLayer.DataTrnsferObjects.QuestionDTO import QuestionDTO
from OuterLayers.AdapterLayer.RESTAPI.Endpoint import Endpoint
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Exception import HttpException
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


class POSTQuestion(Endpoint):
    method = "POST"
    path = "/api/questions"

    def __init__(self, request: HttpRequest):
        super(POSTQuestion, self).__init__(request)

    def handle(self) -> HttpResponse:
        if 'title' not in self.request.body:
            raise HttpException(1111, 'title is required')
        if 'body' not in self.request.body:
            raise HttpException(1111, 'body is required')

        questionDTO = QuestionDTO()
        questionDTO.title = Title(self.request.body['title'])
        questionDTO.body = Body(self.request.body['body'])

        askQuestion(questionDTO)

        return HttpResponse(200, None, None)
